import reflex as rx
from ecommerce.styles.styles import Size
import ecommerce.api.userAPI as userAPI
from ecommerce import const
from fastapi.security import OAuth2PasswordRequestForm


def header() -> rx.Component:
    return rx.vstack(
        # ! HEADER
        rx.center(
            rx.hstack(
                # TODO Icono de la tienda
                rx.vstack(rx.text("Icono"), position="fixed", left="4em"),
                # TODO Letras chulas con el nombre de la tienda
                rx.vstack(rx.heading("I&N Shop"), padding_x=Size.SMALL.value),
                # Iconos de idioma, perfil y cesta
                rx.hstack(
                    # Icono del idioma
                    rx.vstack(
                        rx.menu(
                            rx.menu_button(
                                rx.image(
                                    src="/icons/spainIcon.png",
                                    width=Size.LARGE.value,
                                    height=Size.LARGE.value,
                                )
                            )
                        ),
                        padding_right=Size.MEDIUM.value,
                    ),
                    # Icono de inicio de sesion
                    rx.vstack(
                        rx.menu(
                            rx.menu_button(
                                rx.image(
                                    src="/icons/userIcon.png",
                                    width=Size.LARGE.value,
                                    height=Size.LARGE.value,
                                )
                            ),
                            rx.menu_list(
                                rx.menu_item(
                                    "Iniciar sesión", on_click=LogInState.change_log_in
                                ),
                                rx.modal(
                                    rx.modal_overlay(
                                        rx.modal_content(
                                            rx.modal_header("Iniciar Sesión"),
                                            rx.modal_body(log_in()),
                                            rx.modal_footer(
                                                rx.button(
                                                    "Cerrar",
                                                    on_click=LogInState.change_log_in,
                                                )
                                            ),
                                        )
                                    ),
                                    is_open=LogInState.show_log_in,
                                ),
                                rx.menu_item(
                                    "Registrarme", on_click=RegisterState.change
                                ),
                                rx.modal(
                                    rx.modal_overlay(
                                        rx.modal_content(
                                            rx.modal_header("Registrarme"),
                                            rx.modal_body(register()),
                                            rx.modal_footer(
                                                rx.button(
                                                    "Cerrar",
                                                    on_click=RegisterState.change,
                                                )
                                            ),
                                        )
                                    ),
                                    is_open=RegisterState.show,
                                ),
                                rx.menu_item("Mi cuenta"),
                            ),
                        ),
                        padding_x=Size.MEDIUM.value,
                    ),
                    # Icono de la cesta
                    rx.vstack(
                        rx.button(
                            rx.image(
                                src="/icons/shoppingIcon.png",
                                width=Size.LARGE.value,
                                height=Size.LARGE.value,
                            ),
                            variant="unstyled",
                        ),
                        padding_x=Size.MEDIUM.value,
                    ),
                    position="absolute",
                    right="4em",
                ),
                width="100%",
                padding_top=Size.LARGE.value,
                padding_bottom=Size.MEDIUM.value,
            )
        ),
        rx.divider(border_color="black", width="100%"),
        # ! NAVBAR
        rx.hstack(
            rx.vstack(
                rx.menu(
                    rx.menu_button("Camisetas"),
                    rx.menu_list(
                        rx.menu_item("Manga corta"), rx.menu_item("Manga larga")
                    ),
                ),
                padding_x=Size.BIG.value,
            ),
            rx.center(
                rx.divider(orientation="vertical", border_color="black"),
                height="2em",
            ),
            rx.vstack(
                rx.menu(
                    rx.menu_button("Pantalones"),
                    rx.menu_list(rx.menu_item("Jogger"), rx.menu_item("Skinny")),
                ),
                padding_x=Size.BIG.value,
            ),
        ),
        width="100%",
    )


class OauthForm(rx.Base):
    username: str
    password: str


# Class that manages the login pop-up
class LogInState(rx.State):
    show_log_in: bool = False
    custom_cookie: str = rx.Cookie(name="jwt", max_age=const.ACCESS_TOKEN_DURATION)

    def change_log_in(self):
        self.show_log_in = not (self.show_log_in)

    async def handle_submit(self, form_data: dict):
        oauth_form = OauthForm(
            username=form_data.get("username"), password=form_data.get("password")
        )
        try:
            self.custom_cookie = await userAPI.login_for_access_token(oauth_form)
        except Exception as e:
            return rx.window_alert("Usuario o contraseña incorrectos")


# Method showing the login form
def log_in() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.input(
                placeholder="Email",
                name="username",
            ),
            rx.input(
                placeholder="Contraseña",
                name="password",
            ),
            rx.button("Iniciar sesión", type_="submit", on_click=LogInState.change_log_in),
        ),
        on_submit=LogInState.handle_submit,
        reset_on_submit=True,
    )


# Class that manages the register pop-up
class RegisterState(rx.State):
    show: bool = False
    form_data: dict = {}

    def change(self):
        self.show = not (self.show)

    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        userAPI.register_user(self.form_data)


# Method showing the register form
def register() -> rx.Component:
    return rx.form(
        rx.vstack(
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
            ),
            rx.button("Registrarme", type_="submit", on_click=RegisterState.change),
        ),
        on_submit=RegisterState.handle_submit,
        reset_on_submit=True,
    )
