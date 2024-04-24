import reflex as rx
from ecommerce.styles.styles import Size
from ecommerce import const
from ecommerce.styles.colors import Color, TextColor
import ecommerce.styles.styles as Styles

def footer() -> rx.Component:
    return rx.vstack(
        # Contacto
        rx.hstack(
            rx.chakra.button(
                "Envíos",
                variant="unstyled"
            ),
            rx.chakra.button(
                "Devoluciones",
                variant="unstyled"
            ),
            rx.chakra.button(
                "Contacto",
                variant="unstyled"
            ),
            direction="row",
            spacing="9"
        ),
        #TODO Icono
        rx.hstack(
            rx.chakra.text("Icono")
        ),
        # Legal
        rx.hstack(
            rx.chakra.text(
                f"© 2023-2024 {const.SHOP_NAME}"
            )
        ),
        align="center",
        bg = Color.FOOTER_BACKGROUND.value,
        width = "100%",
        color = TextColor.FOOTER.value
    )
