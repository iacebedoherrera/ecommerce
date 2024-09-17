import reflex as rx
from ecommerce.routes import Route
from ecommerce.components.header import header
from ecommerce.state.userState import LoginState
import ecommerce.utils as utils
from ecommerce.components.footer import footer
from ecommerce.styles.styles import Size
from ecommerce.dal.models.user import User, Address



@rx.page(
    route=Route.MY_ACCOUNT.value,
    title="Mi cuenta",
    on_load=LoginState.refresh_user
)
def my_account() -> rx.Component:
    return rx.flex(
        utils.lang(),
        header(),
        user_info(),
        footer(),
        margin="0",
        direction="column",
        min_height="100vh"
    )


def user_info() -> rx.Component:
    return rx.flex(
        #! TITULO
        rx.flex(
            rx.heading("Mi cuenta"),
        ),
        rx.flex(
            rx.divider(height="2px", color_scheme="mint"),
            width="60%"
        ),
        #! USUARIO
        rx.flex(
            user_data_form(LoginState.user),
            spacing="5",
            align="center",
            width="60%"
        ),
        rx.flex(
            rx.divider(height="2px", color_scheme="mint"),
            width="40%"
        ),
        #! DIRECCION
        rx.flex(
            address_data_form(LoginState.address, LoginState.user.id),
            spacing="5",
            align="center",
            width="60%"
        ),
        direction="column",
        align="center",
        spacing="5",
        width="100%",
        padding_top=Size.MEDIUM.value,
        padding_bottom=Size.BIG.value
    )


def user_data_form(user: User):
    return rx.form(
        rx.flex(
            rx.flex(
                #! Nombre
                rx.flex(
                    rx.text("Nombre: "),
                    rx.input(
                        placeholder=user.name,
                        name="name",
                    ),
                    direction="column",
                    spacing="2"
                ),
                #! Apellidos
                rx.flex(
                    rx.text("Apellidos: "),
                    rx.input(
                        placeholder=user.surname,
                        name="surname",
                    ),
                    direction="column",
                    spacing="2"
                ),
                direction="row",
                spacing="9"
            ),
            rx.flex(
                #! Email
                rx.flex(
                    rx.text(f"Email: "),
                    rx.input(
                        value=user.email
                    ),
                    direction="column",
                    spacing="2"
                ),
                #! Contraseña
                rx.flex(
                    rx.text("Contraseña: "),
                    rx.cond(
                        user.password != "",
                        rx.input(
                            placeholder="************",
                            name="password",
                        ),
                        rx.input()
                    ),
                    direction="column",
                    spacing="2"
                ),
                direction="row",
                spacing="9"
            ),
            rx.flex(
                #! Teléfono
                rx.text("Teléfono: "),
                rx.input(
                    placeholder=user.phone_number,
                    name="phone_number",
                ),
                direction="column",
                spacing="2"
            ),
            rx.flex(
                rx.button("Guardar datos", type="submit"),
                direction="column"
            ),
            direction="column",
            align="center",
            spacing="6"
        ),
        on_submit=lambda form_data: LoginState.update_user(form_data, user.id),
        reset_on_submit=True,
    )


def address_data_form(address: Address, user_id: int):
    return rx.form(
        rx.flex(
            rx.flex(
                #! Direccion
                rx.flex(
                    rx.text("Dirección: "),
                    rx.input(
                        placeholder=address.address,
                        name="address",
                    ),
                    direction="column",
                    spacing="2"
                ),
                #! Ciudad
                rx.flex(
                    rx.text("Ciudad: "),
                    rx.input(
                        placeholder=address.city,
                        name="city",
                    ),
                    direction="column",
                    spacing="2"
                ),
                direction="row",
                spacing="9"
            ),
            rx.flex(
                #! Comunidad
                rx.flex(
                    rx.text(f"Comunidad: "),
                    rx.input(
                        placeholder=address.autonomous_community,
                        name="autonomous_community"
                    ),
                    direction="column",
                    spacing="2"
                ),
                #! Codigo postal
                rx.flex(
                    rx.text("Código postal: "),
                    rx.input(
                        placeholder=address.postal_code,
                        name="postal_code",
                    ),
                    direction="column",
                    spacing="2"
                ),
                direction="row",
                spacing="9"
            ),
            rx.flex(
                rx.button("Guardar dirección", type="submit"),
                direction="column"
            ),
            direction="column",
            align="center",
            spacing="6"
        ),
        on_submit=lambda form_data: LoginState.update_address(form_data, address.id, user_id),
        reset_on_submit=True,
    )