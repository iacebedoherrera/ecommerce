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
from rx_carousel.carousel import carousel
from typing import List


dotenv.load_dotenv()

PRODUCT_API = ProductAPI()


class ProductState(rx.State):
    product: Product = Product()
    images: List[str] = []
    page_loading: bool = True

    @rx.var(cache=True)
    def get_product_type(self) -> str:
        return self.router.page.params.get("product_type", "")
    
    def change_page_loading(self, value: bool):
        self.page_loading = value
    
    async def update_product(self):
        partnumber: str = self.router.page.params.get("partnumber", "")
        self.product = await PRODUCT_API.get_product_by_partnumber(partnumber + "01")

    async def get_product_images(self):
        product_type = self.router.page.params.get("product_type", "")
        partnumber = self.router.page.params.get("partnumber", "")
        path = os.path.join("assets/products", product_type, partnumber)
        base_image_path = os.path.join("/products", product_type, partnumber)
        images_path = []
        for image in os.listdir(path):
            images_path.append(os.path.join(base_image_path, image))

        self.images = images_path

    def update_page_name(self):
        self.change_page_loading(False)
        return rx.call_script(f"document.title = '{self.product.name}';")


@rx.page(
    route=f"{Route.PRODUCTS.value}/[product_type]/[partnumber]",
    title="Productos",
    on_load=[ProductState.update_product, ProductState.get_product_images, ProductState.update_page_name]
)
def product_view() -> rx.Component:
    return rx.flex(
        utils.lang(),
        header(),
        rx.desktop_only(
            rx.skeleton(
                product_detail(),
                loading=ProductState.page_loading
            )
        ),
        rx.mobile_and_tablet(
            rx.center(
                product_detail_for_mobile(),
            )
        ),
        rx.dialog.root(
            rx.dialog.content(
                rx.flex(
                    rx.center(
                        rx.dialog.title(
                            rx.icon("shirt", color="red", size=100)
                        )
                    ),
                    rx.text("No hay stock de este artículo. Pruebe en otro momento."),
                    rx.dialog.close(
                        rx.flex(
                            rx.button("Cerrar", color_scheme="red", on_click=ShoppingState.change_no_stock_message),
                            direction="column"
                        )
                    ),
                    direction="column",
                    align="center",
                    spacing="3"
                ),
            ),
            open=ShoppingState.show_no_stock_message
        ),
        rx.dialog.root(
            rx.dialog.content(
                rx.flex(
                    rx.center(
                        rx.dialog.title(
                            rx.icon("shirt", color="green", size=100)
                        )
                    ),
                    rx.text("Añadido al carrito."),
                    rx.dialog.close(
                        rx.flex(
                            rx.button("OK", color_scheme="blue", on_click=ShoppingState.change_show_success_added),
                            direction="column"
                        )
                    ),
                    direction="column",
                    align="center",
                    spacing="3"
                ),
            ),
            open=ShoppingState.show_success_added
        ),
        footer(),
        direction="column",
        position="relative",
        min_height="100vh"
    )


def product_detail() -> rx.Component:
    return rx.flex(
        carousel(
            rx.foreach(ProductState.images, create_image_carousel),
            width="40%",
            height="auto"
        ),
        product_info(),
        direction="row",
        align="center",
        justify="center",
        padding_top=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        margin_left="1em",
        gap="10em",
        width="100%"
    )

def product_detail_for_mobile() -> rx.Component:
    return rx.flex(
        carousel(
            rx.foreach(ProductState.images, create_image_carousel),
            width="80%",
            height="auto"
        ),
        product_info_for_mobile(),
        direction="column",
        align="center",
        padding_top=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        margin_left="1em",
        margin_right="1em",
        width="90%"
    )

def create_image_carousel(image_path: str):
    return rx.image(
        src=image_path
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
        rx.flex(
            rx.button(
                rx.icon(tag="shopping-cart"),
                "Añadir a la cesta",
                color_scheme="green",
                on_click= ShoppingState.add_product_to_shopping_cart(ProductState.product.partnumber)
            ),
            padding_top="2em"
        ),
        direction="column",
        spacing="5"
    )

def product_info_for_mobile() -> rx.Component:
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
        rx.center(
            rx.flex(
                rx.button(
                    rx.icon(tag="shopping-cart"),
                    "Añadir a la cesta",
                    color_scheme="green",
                    on_click= ShoppingState.add_product_to_shopping_cart(ProductState.product.partnumber)
                ),
                padding_top="2em"
            )
        ),
        direction="column",
        spacing="5",
        width="80%"
    )
