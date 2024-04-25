import reflex as rx
from ecommerce.styles.styles import Size


def products_index() -> rx.Component:
    return rx.chakra.hstack(
        rx.chakra.vstack(
            rx.chakra.button(
                rx.chakra.image(
                    src="/icons/men.avif",
                    height=Size.ULTRA_BIG.value
                ),
                variant="unstyled"
            )
        ),
        rx.chakra.vstack(
            rx.chakra.button(
                rx.chakra.image(
                    src="/icons/women.avif",
                    height=Size.ULTRA_BIG.value
                ),
                variant="unstyled",

            )
        ),
        padding_top=Size.BIG.value,
        padding_bottom=Size.ULTRA_BIG.value,
    )
