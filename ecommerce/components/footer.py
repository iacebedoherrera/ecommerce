import reflex as rx
from ecommerce.styles.styles import Size
from ecommerce import const
from ecommerce.styles.colors import Color, TextColor
import ecommerce.styles.styles as Styles

def footer() -> rx.Component:
    return rx.vstack(
        # Contacto
        rx.hstack(
            rx.button(
                "Envíos",
                variant="unstyled"
            ),
            rx.button(
                "Devoluciones",
                variant="unstyled"
            ),
            rx.button(
                "Contacto",
                variant="unstyled"
            )
        ),
        #TODO Icono
        rx.hstack(
            rx.text("Icono")
        ),
        # Legal
        rx.hstack(
            rx.text(
                f"© 2023-2024 {const.SHOP_NAME}"
            )
        ),
        bg = Color.FOOTER_BACKGROUND.value,
        width = "100%",
        color = TextColor.FOOTER.value
    )
