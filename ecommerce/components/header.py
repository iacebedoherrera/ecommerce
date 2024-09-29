import reflex as rx
import ecommerce.styles.styles as style
from ecommerce.routes import Route
from ecommerce.state.userState import LoginState, RegisterState
from ecommerce import const
import reflex_google_auth
from ecommerce.styles.styles import Size



def header() -> rx.Component:
    return rx.flex(
        # ! HEADER
        rx.flex(
            # TODO Icono de la tienda
            rx.flex(
                rx.link(
                    rx.image(
                        src="/icons/logo_left.png"
                    ),
                    href=Route.INDEX.value
                ),
                position="absolute",
                left="3em"
            ),
            rx.flex(
                rx.desktop_only(
                    rx.flex(
                        rx.link(
                            rx.image(
                                src="/icons/logo.png"
                            ), 
                            href=Route.INDEX.value
                        ),
                        align="center",
                        padding_x=style.Size.SMALL.value,
                    )
                )
            ),
            # Iconos de idioma, perfil y cesta
            rx.flex(
                # Icono del idioma
                rx.vstack(
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.image(
                                src="/icons/spainIcon.png",
                                width=style.Size.LARGE.value,
                                height=style.Size.LARGE.value,
                            )
                        )
                    ),
                ),
                # Nombre de usuario en caso de estar logueado
                rx.cond(
                    LoginState.username != "",
                    rx.vstack(
                        rx.text(LoginState.username)
                    ),
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
                                    "Cerrar sesión", on_click=[
                                        LoginState.log_out(),
                                        rx.remove_cookie(const.LOG_IN_COOKIE_NAME),
                                        rx.remove_cookie(const.USERNAME_COOKIE_NAME), 
                                        rx.redirect(Route.INDEX.value)
                                    ]
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
                            ),
                            rx.flex(
                                rx.divider(),
                                margin_top="20px",
                                margin_bottom="20px"
                            ),
                            rx.flex(
                                rx.box(
                                    reflex_google_auth.google_oauth_provider(
                                        reflex_google_auth.google_login(
                                            on_success=[
                                                reflex_google_auth.GoogleAuthState.on_success,
                                                LoginState.log_in_google
                                            ],
                                        ),
                                    ),
                                    box_shadow="rgba(0, 0, 0, 0.16) 0px 10px 36px 0px, rgba(0, 0, 0, 0.06) 0px 0px 0px 1px",  # noqa
                                    opacity="0.7",
                                    overflow="hidden",
                                    border_radius="10px",
                                    width="200px",
                                ),
                                direction="column",
                                align="center",
                            )
                        ),
                        open=LoginState.show
                    ),
                    rx.dialog.root(
                        rx.dialog.content(
                            rx.flex(
                                rx.center(
                                    rx.dialog.title(
                                        rx.icon("user-x", color="red", size=100)
                                    )
                                ),
                                rx.text("El usuario o contraseña no son correctos"),
                                rx.dialog.close(
                                    rx.flex(
                                        rx.button("Cancelar", color_scheme="red", on_click=LoginState.change_error_user_pass),
                                        direction="column"
                                    )
                                ),
                                direction="column",
                                align="center",
                                spacing="3"
                            ),
                        ),
                        open=LoginState.show_error_user_pass
                    ),
                    rx.dialog.root(
                        rx.dialog.content(
                            rx.flex(
                                rx.center(
                                    rx.dialog.title(
                                        rx.icon("users", color="red", size=100)
                                    )
                                ),
                                rx.text("El usuario ya está registrado en el sistema"),
                                rx.dialog.close(
                                    rx.flex(
                                        rx.button("Cancelar", color_scheme="red", on_click=LoginState.change_error_existing_user),
                                        direction="column"
                                    )
                                ),
                                direction="column",
                                align="center",
                                spacing="3"
                            ),
                        ),
                        open=LoginState.show_error_existing_user
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
                                direction="column"
                            ),
                        ),
                        open=RegisterState.show
                    ),
                    rx.dialog.root(
                        rx.dialog.content(
                            rx.flex(
                                rx.center(
                                    rx.dialog.title(
                                        rx.icon("circle-alert", color="red", size=100)
                                    )
                                ),
                                rx.text("Faltan parámetros obligatorios. Inténtelo de nuevo."),
                                rx.dialog.close(
                                    rx.flex(
                                        rx.button("Cancelar", color_scheme="red", on_click=RegisterState.change_error_missing_parameter),
                                        direction="column"
                                    )
                                ),
                                direction="column",
                                align="center",
                                spacing="3"
                            ),
                        ),
                        open=RegisterState.show_error_missing_parameter
                    ),
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
                        href=Route.SHOPPING_CART.value
                    ),
                ),
                direction="row",
                position="absolute",
                spacing="7",
                right="3em"
            ),
            direction="row",
            width="100%",
            justify="center",
            align="center",
            min_height="100px",
        ),
        rx.divider(border_color="black", width="100%"),
        # ! NAVBAR
        rx.flex(
            rx.mobile_and_tablet(
                rx.menu.root(
                    rx.menu.trigger(
                        rx.button("Productos", variant="soft", size="2", style=style.BUTTON),
                    ),
                    rx.menu.content(
                        rx.menu.item("Camisetas", on_click=rx.redirect(f"{Route.PRODUCTS.value}/tshirt")),
                        rx.menu.separator(),
                        rx.menu.item("Sudaderas", on_click=rx.redirect(f"{Route.PRODUCTS.value}/sweatshirt")),
                        rx.menu.separator(),
                        rx.menu.item("Pantalones"),
                        rx.menu.separator(),
                        rx.menu.item("Accesorios"),
                        size="2",
                    ),
                )
            ),
            rx.desktop_only(
                rx.flex(
                    rx.link(
                        rx.button("Camisetas", style=style.BUTTON),
                        href=f"{Route.PRODUCTS.value}/tshirt"
                    ),
                    rx.center(
                        rx.divider(orientation="vertical", border_color="black"),
                        height="2em",
                    ),
                    rx.link(
                        rx.button("Sudaderas", style=style.BUTTON),
                        href=f"{Route.PRODUCTS.value}/sweatshirt"
                    ),
                    rx.center(
                        rx.divider(orientation="vertical", border_color="black"),
                        height="2em",
                    ),
                    rx.link(
                        rx.button("Pantalones", style=style.BUTTON),
                    ),
                    rx.center(
                        rx.divider(orientation="vertical", border_color="black"),
                        height="2em",
                    ),
                    rx.link(
                        rx.button("Accesorios", style=style.BUTTON),
                    ),
                    direction="row",
                    align="center",
                    justify="center",
                    spacing="7",
                    width="100%"
                ),
            ),
            direction="row",
            align="center",
            justify="center",
            spacing="7",
            width="100%",
            min_height="50px"
        ),
        rx.divider(width="100%"),
        direction="column",
        margin_bottom = Size.BIG.value,
        width="100%"
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
                    required=True
                ),
                rx.input(
                    placeholder="Apellidos",
                    name="surname",
                    required=True
                ),
                rx.input(
                    placeholder="Teléfono",
                    name="phone_number",
                ),
                rx.input(
                    placeholder="Email",
                    name="email",
                    required=True
                ),
                rx.input(
                    placeholder="Contraseña",
                    name="password",
                    type="password",
                    required=True
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

