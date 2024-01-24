import reflex as rx
from ecommerce.styles.styles import Size

def header() -> rx.Component:
    return rx.vstack(
        # ! HEADER
        rx.hstack(
            # TODO Icono de la tienda

            # TODO Letras chulas con el nombre de la tienda
            rx.heading(
                "I&N Shop"
            ),
            # TODO Icono del idioma

            # TODO Icono de inicio de sesion

            # TODO Icono de la cesta

        ),
        # ! NAVBAR
        rx.hstack(
            rx.vstack(
                rx.menu(
                    rx.menu_button("Camisetas",
                        rx.menu_list(
                            rx.menu_item("Manga corta"),
                            rx.menu_item("Manga larga")
                        )
                    )
                ),
                padding_x=Size.BIG.value
            ),
            rx.vstack(
                rx.menu(
                    rx.menu_button("Camisetas",
                        rx.menu_list(
                            rx.menu_item("Manga corta"),
                            rx.menu_item("Manga larga")
                        )
                    )
                )
            )
        )
    )