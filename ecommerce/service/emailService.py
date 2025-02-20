from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
from typing import List

from ecommerce.dal.dto.product_email import ProductEmail
from ecommerce.dal.models.order import OrderItem
from ecommerce.dal.models.user import Address


class EmailService:

    # EMAIL
    EMAIL = os.environ.get("ECOMMERCE_EMAIL")
    EMAIL_PASSWORD = os.environ.get("ECOMMERCE_EMAIL_PASSWORD")
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    async def sendEmail(self, email: str, subject: str, mensaje: str):
        msg = MIMEMultipart()
        msg['From'] = self.EMAIL
        msg['To'] = email
        msg['Subject'] = subject
        msg.attach(MIMEText(mensaje, 'plain'))
        
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.EMAIL, self.EMAIL_PASSWORD)

            server.sendmail(self.EMAIL, msg['To'], msg.as_string())
            print("Correo enviado exitosamente!")

        except Exception as e:
            print(f"Error al enviar el correo: {e}")

        finally:
            server.quit()

    def email_body_order_created(self, username: str, order_id: int, order_items: List[ProductEmail], address: Address):
        productos_html = "".join(
            f"<li>{order_item.name} - Cantidad: {order_item.qty} - Precio: {order_item.price}€</li>" 
            for order_item in order_items
        )

        total_amount: float = 0.0
        for product in order_items:
            total_amount += float(product.price)

        cuerpo_html = f"""
        <html>
        <body>
            <h2>¡Gracias por tu pedido, {username}!</h2>
            <p>Tu pedido <strong>#{order_id}</strong> ha sido confirmado y está siendo procesado.</p>
            
            <h3>Detalles del pedido:</h3>
            <ul>
                {productos_html}
            </ul>
            
            <p><strong>Total:</strong> {total_amount}€</p>
            
            <h3>Dirección de envío:</h3>
            <p>{address.address}, {address.city}, {address.autonomous_community}.</p>
            
            <p>Te avisaremos cuando tu pedido haya sido enviado. Si tienes alguna pregunta, no dudes en contactarnos.</p>
            
            <p>¡Gracias por comprar con nosotros!</p>
            <p>Atentamente,<br>Inusual.</p>
        </body>
        </html>
        """
        
        return cuerpo_html
