import reflex as rx


class ConfirmOrderState(rx.State):
    order_id: int

    async def get_order_id(self):
        self.order_id = self.router.page.params.get("order_id", "")