import reflex as rx
import os, dotenv
from ecommerce.routes import Route
import ecommerce.const as const
import ecommerce.utils as utils
from ecommerce.dal.models.product import Product
from ecommerce.api.ProductAPI import ProductAPI
from ecommerce.components.header import header
from ecommerce.components.footer import footer
from ecommerce.state.shoppingState import ShoppingState
from ecommerce.styles.styles import Size


dotenv.load_dotenv()
BACKEND_URL = os.environ.get("BACKEND_URL")

PRODUCT_API = ProductAPI()


class ProductState(rx.State):
    product: Product = Product()

    @rx.var(cache=True)
    def get_product_type(self) -> str:
        return self.router.page.params.get("product_type", "")
    
    async def update_product(self):
        if not self.product.name:
            partnumber: str = self.router.page.params.get("partnumber", "")
            self.product = await PRODUCT_API.get_product_by_partnumber(partnumber)

    @rx.background
    async def load_carousel(self):
        return rx.call_script("carousel();")


@rx.page(
    route=f"{Route.PRODUCTS.value}/[product_type]/[partnumber]",
    title=const.PRODUCTS.get(ProductState.get_product_type),
    on_load=[ProductState.update_product, ProductState.load_carousel]
)
def product_view() -> rx.Component:
    return rx.flex(
        utils.lang(),
        header(),
        rx.desktop_only(
            product_detail()
        ),
        rx.mobile_and_tablet(
            product_detail_for_mobile(),
            width="100%"
        ),
        footer(),
        direction="column",
        position="relative",
        min_height="100vh"
    )


def product_detail() -> rx.Component:
    return rx.flex(
        photos_carousel(),
        product_info(),
        direction="row",
        align="center",
        justify="center",
        padding_top=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        gap="10em",
        width="100%"
    )

def product_detail_for_mobile() -> rx.Component:
    return rx.flex(
        photos_carousel(),
        product_info(),
        direction="column",
        align="center",
        padding_top=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        width="90%"
    )

def product_info() -> rx.Component:
    return rx.flex(
        rx.flex(
            rx.text(ProductState.product.name, size="7", weight="bold"),
            rx.text(ProductState.product.price + " €", size="5"),
            direction="column",
            align="2"
        ),
        rx.flex(  
            rx.text("Talla: "),    
            rx.select(
                ShoppingState.sizes,
                default_value=ShoppingState.size,
                on_change=ShoppingState.set_size
            ),
            direction="row",
            align="center",
            spacing="6"
        ),
        rx.dialog.root(
            rx.dialog.trigger(
                rx.button(
                    rx.icon(tag="shopping-cart"),
                    "Añadir a la cesta",
                    color_scheme="green",
                    on_click= ShoppingState.add_product_to_shopping_cart(ProductState.product.partnumber)
                ),
                padding_top="3em"
            ),
            rx.dialog.content(
                rx.dialog.close(
                    rx.icon(tag="circle-x")
                ),
                rx.chakra.alert(
                    rx.chakra.alert_icon(),
                    rx.chakra.alert_title(
                        "Artículo añadido al carrito"
                    ),
                    status="success",
                ),
                size="1"
            )
        ),
        direction="column",
        spacing="5"
    )


def photos_carousel() -> rx.Component:
    return rx.flex(
        rx.html(
            """
            <div class="carousel-container">
                <div id="slideshow-container" class="slideshow-container"></div>
                <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
                <a class="next" onclick="plusSlides(1)">&#10095;</a>
            </div>
            """
        ),
        rx.script(
            src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"
        ),
        rx.script(
            """
            function carousel() {
                var pathname = window.location.pathname;
                
                var backendUrl = "http://localhost:8000";
                var rutaImagenes = backendUrl + pathname.replace('/products', '/images');
                console.log(rutaImagenes);
                
                $.get(rutaImagenes, function(data) {
                    if (data.image_paths) {
                        var imagePaths = data.image_paths;
                        var slideshowContainer = document.getElementById("slideshow-container");
                        slideshowContainer.innerHTML = ""; // Limpiar el contenedor antes de agregar imágenes nuevas
                        
                        imagePaths.forEach(function(path) {

                            var adjustedPath = '/products/' + path;
                            
                            var slide = document.createElement("div");
                            slide.className = "mySlides fade";
                            
                            var img = document.createElement("img");
                            img.src = adjustedPath;
                            img.style.width = "100%";
                            
                            slide.appendChild(img);
                            slideshowContainer.appendChild(slide);
                        });
                        
                        var slideIndex = 1;
                        showSlides(slideIndex);
                        
                        window.plusSlides = function(n) {
                            showSlides(slideIndex += n);
                        };
                        
                        function showSlides(n) {
                            var i;
                            var slides = document.getElementsByClassName("mySlides");
                            if (n > slides.length) {slideIndex = 1}    
                            if (n < 1) {slideIndex = slides.length}
                            for (i = 0; i < slides.length; i++) {
                                slides[i].style.display = "none";  
                            }
                            slides[slideIndex-1].style.display = "block";  
                        }
                    } else {
                        console.log("No image paths found in response");
                    }
                }).fail(function(jqXHR, textStatus, errorThrown) {
                    console.log("Error fetching images: ", textStatus, errorThrown);
                });
            }
            """
        )
    )