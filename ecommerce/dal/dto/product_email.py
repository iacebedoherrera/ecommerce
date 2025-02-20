
class ProductEmail:
    
    name: str
    qty: int
    price: str


    def __init__(self, name: str, qty: int, price: float):
        self.name = name
        self.qty = qty
        self.price = price
