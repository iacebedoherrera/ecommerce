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
        rx.desktop_only(
            user_info(),
        ),
        rx.mobile_and_tablet(
            user_info_for_mobile()
        ),
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
            width="80%"
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
            width="80%"
        ),
        rx.dialog.root(
            rx.dialog.content(
                rx.flex(
                    rx.center(
                        rx.dialog.title(
                            rx.icon("user-round-check", color="green", size=100)
                        )
                    ),
                    rx.text("Cambios guardados con éxito"),
                    rx.dialog.close(
                        rx.flex(
                            rx.button("Hecho", color_scheme="blue", on_click=LoginState.change_success_changes),
                            direction="column"
                        )
                    ),
                    direction="column",
                    align="center",
                    spacing="3"
                ),
            ),
            open=LoginState.show_success_changes
        ),
        rx.dialog.root(
            rx.dialog.content(
                rx.flex(
                    rx.center(
                        rx.dialog.title(
                            rx.icon("map-pinned", color="red", size=100)
                        )
                    ),
                    rx.text("Debe completar la dirección completa"),
                    rx.dialog.close(
                        rx.flex(
                            rx.button("Cancelar", color_scheme="red", on_click=LoginState.change_error_address),
                            direction="column"
                        )
                    ),
                    direction="column",
                    align="center",
                    spacing="3"
                ),
            ),
            open=LoginState.show_error_address
        ),
        direction="column",
        align="center",
        spacing="5",
        width="100%",
        padding_top=Size.MEDIUM.value,
        padding_bottom=Size.BIG.value
    )


def user_info_for_mobile() -> rx.Component:
    return rx.flex(
        #! TITULO
        rx.flex(
            rx.heading("Mi cuenta"),
        ),
        rx.flex(
            rx.divider(height="2px", color_scheme="mint"),
            width="80%"
        ),
        #! USUARIO
        rx.flex(
            user_data_form_for_mobile(LoginState.user),
            spacing="5",
            align="center",
            width="80%"
        ),
        rx.flex(
            rx.divider(height="2px", color_scheme="mint"),
            width="80%"
        ),
        #! DIRECCION
        rx.flex(
            address_data_form_for_mobile(LoginState.address, LoginState.user.id),
            spacing="5",
            align="center",
            width="80%"
        ),
        rx.dialog.root(
            rx.dialog.content(
                rx.flex(
                    rx.center(
                        rx.dialog.title(
                            rx.icon("user-round-check", color="green", size=100)
                        )
                    ),
                    rx.text("Cambios guardados con éxito"),
                    rx.dialog.close(
                        rx.flex(
                            rx.button("Hecho", color_scheme="blue", on_click=LoginState.change_success_changes),
                            direction="column"
                        )
                    ),
                    direction="column",
                    align="center",
                    spacing="3"
                ),
            ),
            open=LoginState.show_success_changes
        ),
        rx.dialog.root(
            rx.dialog.content(
                rx.flex(
                    rx.center(
                        rx.dialog.title(
                            rx.icon("map-pinned", color="red", size=100)
                        )
                    ),
                    rx.text("Debe completar la dirección completa"),
                    rx.dialog.close(
                        rx.flex(
                            rx.button("Cancelar", color_scheme="red", on_click=LoginState.change_error_address),
                            direction="column"
                        )
                    ),
                    direction="column",
                    align="center",
                    spacing="3"
                ),
            ),
            open=LoginState.show_error_address
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
            #! Nombre
            rx.flex(
                rx.text("Nombre: "),
                rx.cond(
                    user.is_google_user,
                    rx.input(
                        value=user.name
                    ),
                    rx.input(
                        placeholder=user.name,
                        name="name",
                    ),
                ),
                direction="column",
                spacing="2",
                width="35%"
            ),
            #! Apellidos
            rx.flex(
                rx.text("Apellidos: "),
                rx.cond(
                    user.is_google_user,
                    rx.input(
                        value=user.surname
                    ),
                    rx.input(
                        placeholder=user.surname,
                        name="surname",
                    ),
                ),
                direction="column",
                spacing="2",
                width="35%"
            ),
            #! Email
            rx.flex(
                rx.text(f"Email: "),
                rx.input(
                    value=user.email
                ),
                direction="column",
                spacing="2",
                width="35%"
            ),
            #! Contraseña
            rx.cond(
                user.is_google_user is False,
                rx.flex(
                    rx.text("Contraseña: "),
                    rx.cond(
                        user.password is not None and user.password != "",
                        rx.input(
                            placeholder="************",
                            name="password",
                        ),
                        rx.input(
                            name="password"
                        )
                    ),
                    direction="column",
                    spacing="2",
                    width="35%"
                ),
            ),
            rx.flex(
                #! Teléfono
                rx.text("Teléfono: "),
                rx.input(
                    placeholder=user.phone_number,
                    name="phone_number",
                ),
                direction="column",
                spacing="2",
                width="35%"
            ),
            rx.flex(
                rx.button("Guardar datos", type="submit"),
                direction="column"
            ),
            direction="column",
            align="center",
            spacing="6",
            width="100%"
        ),
        on_submit=lambda form_data: LoginState.update_user(form_data, user.id),
        reset_on_submit=True
    )

def user_data_form_for_mobile(user: User):
    return rx.form(
        rx.flex(
            #! Nombre
            rx.flex(
                rx.text("Nombre: "),
                rx.cond(
                    user.is_google_user,
                    rx.input(
                        value=user.name
                    ),
                    rx.input(
                        placeholder=user.name,
                        name="name",
                    ),
                ),
                direction="column",
                spacing="2",
                width="80%"
            ),
            #! Apellidos
            rx.flex(
                rx.text("Apellidos: "),
                rx.cond(
                    user.is_google_user,
                    rx.input(
                        value=user.surname
                    ),
                    rx.input(
                        placeholder=user.surname,
                        name="surname",
                    ),
                ),
                direction="column",
                spacing="2",
                width="80%"
            ),
            #! Email
            rx.flex(
                rx.text(f"Email: "),
                rx.input(
                    value=user.email
                ),
                direction="column",
                spacing="2",
                width="80%"
            ),
            #! Contraseña
            rx.cond(
                user.is_google_user is False,
                rx.flex(
                    rx.text("Contraseña: "),
                    rx.cond(
                        user.password is not None and user.password != "",
                        rx.input(
                            placeholder="************",
                            name="password",
                        ),
                        rx.input(
                            name="password"
                        )
                    ),
                    direction="column",
                    spacing="2",
                    width="80%"
                ),
            ),
            rx.flex(
                #! Teléfono
                rx.text("Teléfono: "),
                rx.input(
                    placeholder=user.phone_number,
                    name="phone_number",
                ),
                direction="column",
                spacing="2",
                width="80%"
            ),
            rx.flex(
                rx.button("Guardar datos", type="submit"),
                direction="column"
            ),
            direction="column",
            align="center",
            spacing="6",
            width="100%"
        ),
        on_submit=lambda form_data: LoginState.update_user(form_data, user.id),
        reset_on_submit=True
    )


def address_data_form(address: Address, user_id: int):
    return rx.form(
        rx.flex(
            #! Direccion
            rx.flex(
                rx.text("Dirección: "),
                rx.cond(
                    address is not None,
                    rx.input(
                        placeholder=address.address,
                        name="address",
                    ),
                    rx.input(
                        name="address",
                    )
                ),
                direction="column",
                spacing="2",
                width="35%"
            ),
            #! Ciudad
            rx.flex(
                rx.text("Ciudad: "),
                rx.cond(
                    address is not None,
                    rx.input(
                        placeholder=address.city,
                        name="city",
                    ),
                    rx.input(
                        name="city",
                    )
                ),
                direction="column",
                spacing="2",
                width="35%"
            ),
            #! Comunidad
            rx.flex(
                rx.text(f"Comunidad: "),
                rx.cond(
                    address is not None,
                    rx.input(
                        placeholder=address.autonomous_community,
                        name="autonomous_community",
                    ),
                    rx.input(
                        name="autonomous_community",
                    )
                ),
                direction="column",
                spacing="2",
                width="35%"
            ),
            #! Codigo postal
            rx.flex(
                rx.text("Código postal: "),
                rx.cond(
                    address is not None,
                    rx.input(
                        placeholder=address.postal_code,
                        name="postal_code",
                    ),
                    rx.input(
                        name="postal_code",
                    )
                ),
                direction="column",
                spacing="2",
                width="35%"
            ),
            rx.flex(
                rx.button("Guardar dirección", type="submit"),
                direction="column"
            ),
            direction="column",
            align="center",
            spacing="6",
            width="100%"
        ),
        on_submit=lambda form_data: LoginState.update_address(form_data, address.id, user_id),
        reset_on_submit=True
    )

def address_data_form_for_mobile(address: Address, user_id: int):
    return rx.form(
        rx.flex(
            #! Direccion
            rx.flex(
                rx.text("Dirección: "),
                rx.cond(
                    address is not None,
                    rx.input(
                        placeholder=address.address,
                        name="address",
                    ),
                    rx.input(
                        name="address",
                    )
                ),
                direction="column",
                spacing="2",
                width="80%"
            ),
            #! Ciudad
            rx.flex(
                rx.text("Ciudad: "),
                rx.cond(
                    address is not None,
                    rx.input(
                        placeholder=address.city,
                        name="city",
                    ),
                    rx.input(
                        name="city",
                    )
                ),
                direction="column",
                spacing="2",
                width="80%"
            ),
            #! Comunidad
            rx.flex(
                rx.text(f"Comunidad: "),
                rx.cond(
                    address is not None,
                    rx.input(
                        placeholder=address.autonomous_community,
                        name="autonomous_community",
                    ),
                    rx.input(
                        name="autonomous_community",
                    )
                ),
                direction="column",
                spacing="2",
                width="80%"
            ),
            #! Codigo postal
            rx.flex(
                rx.text("Código postal: "),
                rx.cond(
                    address is not None,
                    rx.input(
                        placeholder=address.postal_code,
                        name="postal_code",
                    ),
                    rx.input(
                        name="postal_code",
                    )
                ),
                direction="column",
                spacing="2",
                width="80%"
            ),
            rx.flex(
                rx.button("Guardar dirección", type="submit"),
                direction="column"
            ),
            direction="column",
            align="center",
            spacing="6",
            width="100%"
        ),
        on_submit=lambda form_data: LoginState.update_address(form_data, address.id, user_id),
        reset_on_submit=True
    )