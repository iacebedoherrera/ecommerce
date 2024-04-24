import reflex as rx
import ecommerce.styles.styles as style
from ecommerce.routes import Route
from ecommerce.state.userState import LoginState, RegisterState



def header() -> rx.Component:
    return rx.vstack(
        # ! HEADER
        rx.hstack(
            # TODO Icono de la tienda
            rx.vstack(rx.text("Icono"), position="absolute", left="4em"),
            # TODO Letras chulas con el nombre de la tienda
            rx.vstack(
                rx.link(
                    rx.heading("I&N Shop"), padding_x=style.Size.SMALL.value,
                    href=Route.INDEX.value
                )
            ),
            # Iconos de idioma, perfil y cesta
            rx.hstack(
                # Icono del idioma
                rx.vstack(
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.chakra.image(
                                src="/icons/spainIcon.png",
                                width=style.Size.LARGE.value,
                                height=style.Size.LARGE.value,
                            )
                        )
                    ),
                    padding_right=style.Size.MEDIUM.value,
                ),
                # Nombre de usuario en caso de estar logueado
                rx.vstack(
                    rx.text(LoginState.username)
                ),
                # Icono de inicio de sesion
                rx.vstack(
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.image(
                                src="/icons/userIcon.png",
                                width=style.Size.LARGE.value,
                                height=style.Size.LARGE.value,
                            )
                        ),
                        rx.cond(
                            LoginState.login_cookie == "",
                            rx.menu.content(
                                rx.menu.item(
                                    "Iniciar sesión", on_click=LoginState.change
                                ),
                                rx.menu.item(
                                    "Registrarme", on_click=RegisterState.change
                                )
                            ),
                            rx.menu.content(
                                rx.menu.item(
                                    "Mi cuenta", on_click=rx.redirect(Route.MY_ACCOUNT.value)
                                ),
                                rx.menu.item(
                                    "Cerrar sesión", on_click=LoginState.log_out
                                )
                            ),
                        ),
                    ),
                    rx.dialog.root(
                        rx.dialog.content(
                            rx.center(
                                rx.dialog.title("Iniciar sesión")
                            ),
                            log_in(),
                            rx.flex(
                                rx.dialog.close(
                                    rx.flex(
                                        rx.button("Cancelar", color_scheme="red", on_click=LoginState.change),
                                        direction="column"
                                    )
                                ),
                                direction="column"
                            )
                        ),
                        open=LoginState.show
                    ),
                    rx.dialog.root(
                        rx.dialog.content(
                            rx.center(
                                rx.dialog.title("Registrarme")
                            ),
                            register(),
                            rx.flex(
                                rx.dialog.close(
                                    rx.flex(
                                        rx.button("Cancelar", color_scheme="red", on_click=RegisterState.change),
                                        direction="column"
                                    )
                                ),
                                direction="row"
                            ),
                        ),
                        open=RegisterState.show
                    ),
                    padding_x=style.Size.MEDIUM.value,
                ),
                # Icono de la cesta
                rx.vstack(
                    rx.link(
                        rx.image(
                            src="/icons/shoppingIcon.png",
                            width=style.Size.LARGE.value,
                            height=style.Size.LARGE.value,
                        ),
                        variant="ghost",
                    ),
                    padding_x=style.Size.MEDIUM.value,
                ),
                position="absolute",
                right="4em",
            ),
            width="100%",
            justify="center",
            padding_top=style.Size.LARGE.value,
            padding_bottom=style.Size.MEDIUM.value,
        ),
        rx.divider(border_color="black", width="100%"),
        # ! NAVBAR
        rx.hstack(
            rx.vstack(
                rx.button(
                    "Camisetas", style=style.BUTTON,
                    on_click=rx.redirect(f"{Route.PRODUCTS.value}/tshirt")
                ),
                padding_x=style.Size.BIG.value,
            ),
            rx.center(
                rx.divider(orientation="vertical", border_color="black"),
                height="2em",
            ),
            rx.vstack(
                rx.button("Pantalones", style=style.BUTTON),
                padding_x=style.Size.BIG.value,
            ),
            justify="center",
            width="100%"
        ),
        width="100%",
    )


# Method showing the login form
def log_in() -> rx.Component:
    return rx.form(
        rx.flex(
            rx.flex(
                rx.input(
                    placeholder="Email",
                    name="username",
                    required=True,
                ),
                rx.input(
                    placeholder="Contraseña",
                    name="password",
                    required=True,
                    type="password"
                ),
                direction="column",
                spacing="3"
            ),
            rx.flex(
                rx.button("Iniciar sesión", type="submit", on_click=LoginState.change),
                direction="column"
            ),
            direction="column",
            spacing="6"
        ),
        on_submit=LoginState.log_in,
        reset_on_submit=True,
    )


# Method showing the register form
def register() -> rx.Component:
    return rx.form(
        rx.flex(
            rx.flex(
                rx.input(
                    placeholder="Nombre",
                    name="name",
                ),
                rx.input(
                    placeholder="Apellidos",
                    name="surname",
                ),
                rx.input(
                    placeholder="Teléfono",
                    name="phone_number",
                ),
                rx.input(
                    placeholder="Email",
                    name="email",
                ),
                rx.input(
                    placeholder="Contraseña",
                    name="password",
                    type="password"
                ),
                rx.input(
                    placeholder="Calle",
                    name="address",
                ),
                rx.flex(
                    rx.input(
                        placeholder="Ciudad",
                        name="city",
                    ),
                    rx.input(
                        placeholder="Comunidad",
                        name="autonomous_community",
                    ),
                    rx.input(
                        placeholder="Código postal",
                        name="postal_code",
                    ),
                    spacing="3",
                    direction="row"
                ),
                direction="column",
                spacing="3"
            ),
            rx.flex(
                rx.button("Registrarme", type="submit", on_click=RegisterState.change),
                direction="column"
            ),
            direction="column",
            spacing="6"
        ),
        on_submit=RegisterState.handle_submit,
        reset_on_submit=True,
    )

