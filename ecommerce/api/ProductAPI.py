from ecommerce.dal.dao.ProductDAO import ProductDAO
from ecommerce.dal.models.product import Product




class ProductAPI:

    async def get_product_by_partnumber(self, partnumber: str):
        user: Product = ProductDAO.find_by_partnumber(partnumber)
        if not user:
            raise Exception("No existe el artículo en BBDD.")
        else:
            return user