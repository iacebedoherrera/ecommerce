import reflex as rx
from ecommerce import const
from ecommerce.styles.colors import Color, TextColor
from ecommerce.routes import Route


def footer() -> rx.Component:
    return rx.flex(
        # Contacto
        rx.flex(
            rx.button(
                "Envíos",
                color="white",
                variant="ghost",
                on_click=rx.redirect(Route.SHIPPINGS.value)
            ),
            rx.button(
                "Devoluciones",
                color="white",
                variant="ghost",
                on_click=rx.redirect(Route.RETURNS.value)
            ),
            rx.button(
                "Contacto",
                color="white",
                variant="ghost",
                on_click=rx.redirect(Route.CONTACT.value)
            ),
            direction="row",
            spacing="9",
            margin_top="15px",
            bg = Color.FOOTER_BACKGROUND.value,
        ),
        # Iconos
        rx.flex(
            # Icono
            rx.image(
                src="/icons/logo_footer.png"
            ),
            rx.image(
                src="/icons/paypal.png",
                on_click=rx.redirect(Route.PAYPAL.value, external=True)
            ),
            rx.image(
                src="/icons/reflex.png",
                on_click=rx.redirect(Route.REFLEX.value, external=True)
            ),
            direction="row",
            spacing="9",
            bg = Color.FOOTER_BACKGROUND.value,
        ),
        # Legal
        rx.flex(
            rx.text(
                f"© 2023-2024 {const.SHOP_NAME}"
            ),
            margin_bottom="15px",
            bg = Color.FOOTER_BACKGROUND.value,
        ),
        direction = "column",
        spacing="6",
        align="center",
        bg = Color.FOOTER_BACKGROUND.value,
        color = TextColor.FOOTER.value,
        margin_top="auto",
        width = "100%"
    )
