import reflex as rx
from ecommerce.routes import Route
import ecommerce.const as const
import ecommerce.utils as utils
from ecommerce.components.header import header
from ecommerce.components.footer import footer
from ecommerce.styles.styles import Size


@rx.page(
    route=Route.SHIPPINGS.value,
    title=const.SHIPPINGS
)
def shippings() -> rx.Component:
    return rx.flex(
        utils.lang(),
        header(),
        rx.center(
            shippings_info(),
        ),
        footer(),
        direction="column",
        position="relative",
        min_height="100vh"
    )


def shippings_info() -> rx.Component:
    return rx.flex(
        rx.flex(
            rx.text(
                "Envíos",
                size="5",
                weight="bold"
            ),
            rx.text(
                f"¡Hola, fashionistas! En {const.SHOP_NAME}, queremos que tus nuevas prendas lleguen rápido y sin complicaciones."
            ),
            rx.text(
                "Aquí tienes todo lo que necesitas saber sobre nuestros envíos."
            ),
            direction="column",
            align="center",
            spacing="2"
        ),
        rx.flex(
            rx.text(
                "Opciones de envío",
                size="5",
                weight="bold"
            ),
            rx.text(
                "Porque sabemos que quieres tus looks lo antes posible, ofrecemos varias opciones:"
            ),
            rx.text(
                "Envío Estándar: Llega en 3-5 días hábiles."
            ),
            rx.text(
                "Envío Súper Rápido: Llega en 1-2 días hábiles."
            ),
            direction="column",
            align="center",
            spacing="2"
        ),
        rx.flex(
            rx.text(
                "Gastos de envío",
                size="5",
                weight="bold"
            ),
            rx.text(
                "Envío Estándar: 5 € (¡Gratis si tu compra es mayor a 50 €!)."
            ),
            rx.text(
                "Envío Súper Rápido: 7,50 €."
            ),
            direction="column",
            align="center",
            spacing="2"
        ),
        rx.flex(
            rx.text(
                "Procesamiento de pedidos",
                size="5",
                weight="bold"
            ),
            rx.text(
                "¿Listo para recibir tu pedido? Aquí está cómo funciona:"
            ),
            rx.text(
                "Tiempo de Procesamiento: Enviamos todo dentro de 1-2 días hábiles desde que recibimos tu pago."
            ),
            rx.text(
                "Confirmación y Seguimiento: Te enviaremos un correo con tu número de seguimiento una vez que tu pedido esté en camino."
            ),
            direction="column",
            align="center",
            spacing="2"
        ),
        rx.flex(
            rx.text(
                "Políticas de envío",
                size="5",
                weight="bold"
            ),
            rx.text(
                "Dirección correcta: Asegúrate de escribir bien tu dirección para evitar retrasos. No podemos hacernos responsables de direcciones incorrectas."
            ),
            rx.text(
                "Días festivos y fines de semana: No hacemos envíos en días festivos ni fines de semana, así que tenlo en cuenta."
            ),
            rx.text(
                "Retrasos inesperados: Aunque hacemos todo lo posible por cumplir los tiempos, a veces hay factores fuera de nuestro control (¡gracias, clima!)."
            ),
            rx.text(
                "Agradecemos tu paciencia."
            ),
            direction="column",
            align="center",
            spacing="2"
        ),
        direction="column",
        align="center",
        spacing="9",
        text_align="center",
        margin_bottom=Size.BIG.value,
        width="80%"
    )