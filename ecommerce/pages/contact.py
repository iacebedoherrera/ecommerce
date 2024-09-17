import reflex as rx
from ecommerce.routes import Route
import ecommerce.const as const
import ecommerce.utils as utils
from ecommerce.components.header import header
from ecommerce.components.footer import footer
from ecommerce.styles.styles import Size


@rx.page(
    route=Route.CONTACT.value,
    title=const.CONTACT
)
def contact() -> rx.Component:
    return rx.flex(
        utils.lang(),
        header(),
        contact_info(),
        footer(),
        direction="column",
        position="relative",
        min_height="100vh"
    )


def contact_info() -> rx.Component:
    return rx.flex(
        rx.flex(
            rx.text(
                "Hablemos",
                size="5",
                weight="bold"
            ),
            rx.text(
                "¿Tienes alguna duda o necesitas ayuda con tu devolución o cambio? Nuestro equipo de soporte está aquí para ti. Contáctanos a soporte@inusual.com."
            ),
            rx.text(
                f"Gracias por elegir {const.SHOP_NAME}. ¡Queremos que ames tus nuevas prendas tanto como nosotros!"
            ),
            direction="column",
            align="center",
            spacing="2"
        ),
        direction="column",
        align="center",
        spacing="9",
        text_align="center",
        margin_bottom=Size.BIG.value
    )