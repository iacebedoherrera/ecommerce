import reflex as rx
from ecommerce.routes import Route
import ecommerce.const as const
import ecommerce.utils as utils
from ecommerce.components.header import header
from ecommerce.components.footer import footer
from ecommerce.styles.styles import Size


@rx.page(
    route=Route.RETURNS.value,
    title=const.RETURNS
)
def returns() -> rx.Component:
    return rx.flex(
        utils.lang(),
        header(),
        returns_info(),
        footer(),
        direction="column",
        position="relative",
        min_height="100vh"
    )


def returns_info() -> rx.Component:
    return rx.flex(
        rx.flex(
            rx.text(
                "Devoluciones y Cambios",
                size="5",
                weight="bold"
            ),
            rx.text(
                f"¡En {const.SHOP_NAME}, queremos que estés completamente feliz con tu compra!"
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
                "¿Cómo hacer una devolución o cambio?",
                size="5",
                weight="bold"
            ),
            rx.text(
                "1. Inicia tu Devolución o Cambio:",
                size="3",
                weight="bold"
            ),
            rx.text(
                "Ve a nuestra página de Devoluciones y sigue las instrucciones para iniciar tu devolución o cambio."
            ),
            rx.text(
                "También puedes enviarnos un correo a devoluciones@inusual.com con tu número de pedido y los detalles de lo que quieres devolver o cambiar."
            ),
            rx.text(
                "2. Empaqueta tu Artículo:",
                size="3",
                weight="bold"
            ),
            rx.text(
                "Usa el embalaje original si es posible."
            ),
            rx.text(
                "Asegúrate de que el artículo esté en las mismas condiciones en que lo recibiste: sin usar, sin lavar, y con todas las etiquetas intactas."
            ),
            rx.text(
                "3. Envíalo de Vuelta:",
                size="3",
                weight="bold"
            ),
            rx.text(
                "Te proporcionaremos una etiqueta de envío de devolución."
            ),
            rx.text(
                "Lleva tu paquete a la oficina de Correos más cercana o programa una recogida con la empresa de mensajería."
            ),
            direction="column",
            align="center",
            spacing="2"
        ),
        rx.flex(
            rx.text(
                "Políticas de Devoluciones y Cambios",
                size="5",
                weight="bold"
            ),
            rx.text(
                "Plazo para devoluciones: Tienes 30 días desde la fecha de compra para devolver o cambiar cualquier artículo."
            ),
            rx.text(
                "Condición del artículo: Aceptamos devoluciones y cambios solo si los artículos están sin usar, sin lavar, y con todas las etiquetas originales."
            ),
            rx.text(
                "Artículos no retornables: Por razones de higiene, no podemos aceptar devoluciones ni cambios de ropa interior, trajes de baño, o artículos en oferta final."
            ),
            direction="column",
            align="center",
            spacing="2"
        ),
        rx.flex(
            rx.text(
                "Reembolsos",
                size="5",
                weight="bold"
            ),
            rx.text(
                "Procesamiento de Reembolsos: Una vez que recibamos tu devolución, procesaremos tu reembolso dentro de 5-7 días hábiles."
            ),
            rx.text(
                "Forma de Reembolso: Los reembolsos se emitirán a la forma de pago original. Si pagaste con tarjeta de crédito, puede tardar algunos días adicionales en aparecer en tu cuenta."
            ),
            direction="column",
            align="center",
            spacing="2"
        ),
        rx.flex(
            rx.text(
                "Cambios",
                size="5",
                weight="bold"
            ),
            rx.text(
                "Solicitar un cambio: Si quieres cambiar un artículo por una talla o color diferente, sigue el mismo proceso de devolución y especifica el cambio que deseas."
            ),
            rx.text(
                "Envío del nuevo artículo: Te enviaremos el nuevo artículo sin costo adicional una vez que recibamos el original."
            ),
            rx.text(
                "Retrasos inesperados: Aunque hacemos todo lo posible por cumplir los tiempos, a veces hay factores fuera de nuestro control (¡gracias, clima!)."
            ),
            direction="column",
            align="center",
            spacing="2"
        ),
        rx.flex(
            rx.text(
                "Problemas con tu Pedido",
                size="5",
                weight="bold"
            ),
            rx.text(
                "Artículo Dañado o Incorrecto: Si recibiste un artículo dañado o incorrecto, ¡lo sentimos mucho! Contáctanos a contacto@inusual.com dentro de los 7 días posteriores a la recepción del pedido. Nos encargaremos de solucionarlo de inmediato."
            ),
            direction="column",
            align="center",
            spacing="2"
        ),
        direction="column",
        align="center",
        spacing="9",
        text_align="center",
        margin_bottom=Size.BIG.value
    )