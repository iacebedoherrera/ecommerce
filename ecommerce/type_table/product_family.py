
class Family:
    _family = {
        "01": "tshirt",
        "02": "sweatshirt"
    }


    @classmethod
    def get_family(cls, id):
        return cls._family.get(id)
