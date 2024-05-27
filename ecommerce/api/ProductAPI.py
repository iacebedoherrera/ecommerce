from ecommerce.dal.dao.ProductDAO import ProductDAO
from ecommerce.dal.models.product import Product




class ProductAPI:

    async def get_product_by_partnumber(self, partnumber: str):
        product: Product = ProductDAO.find_by_partnumber(partnumber)
        if not product:
            raise Exception("No existe el artículo en BBDD.")
        else:
            return product
        

    async def get_product_by_id(self, id: int):
        product: Product = ProductDAO.find_by_id(id)
        if not product:
            raise Exception("No existe el artículo en BBDD.")
        else:
            return product
        