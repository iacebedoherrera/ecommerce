import reflex as rx
from ecommerce.routes import Route
import ecommerce.const as const
import ecommerce.utils as utils
from ecommerce.dal.models.product import Product
from ecommerce.api.ProductAPI import ProductAPI
from ecommerce.components.header import header
from ecommerce.components.footer import footer
from ecommerce.state.shoppingState import ShoppingState


PRODUCT_API = ProductAPI()


class ProductState(rx.State):
    product: Product = Product()

    @rx.var
    def get_product_type(self) -> str:
        return self.router.page.params.get("product_type", "")
    
    async def update_product(self):
        if not self.product.name:
            partnumber: str = self.router.page.params.get("partnumber", "")
            self.product = await PRODUCT_API.get_product_by_partnumber(partnumber)

    @rx.background
    async def load_carousel(self):
        return rx.call_script("carousel()")


@rx.page(
    route=f"{Route.PRODUCTS.value}/[product_type]/[partnumber]",
    title=const.PRODUCTS.get(ProductState.get_product_type),
    on_load=[ProductState.update_product, ProductState.load_carousel]
)
def product_view() -> rx.Component:
    return rx.vstack(
        utils.lang(),
        header(),
        rx.divider(border_color="black"),
        product_detail(),
        footer()
    )


def product_detail() -> rx.Component:
    return rx.hstack(
        photos_carousel(),
        product_info()
    )


def product_info() -> rx.Component:
    return rx.vstack(
        rx.text(ProductState.product.name),
        rx.text(ProductState.product.price + "€"),
        rx.dialog.root(
            rx.dialog.trigger(
                rx.button(
                    rx.icon(tag="shopping-cart"),
                    "Añadir a la cesta",
                    on_click= ShoppingState.add_product_to_shopping_cart(ProductState.product.id)
                )
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
        )
    )


def photos_carousel() -> rx.Component:
    return rx.vstack(
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
                console.log(pathname);
                
                var backendUrl = "http://localhost:8000";
                var rutaImagenes = backendUrl + pathname.replace('/products', '/images');
                
                console.log("Fetching images from: ", rutaImagenes);

                $.get(rutaImagenes, function(data) {
                    console.log("Response received: ", data);
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