from enum import Enum


class Family:
    _family = {
        "01": "tshirt"
    }


    @classmethod
    def get_family(cls, id):
        return cls._family.get(id)
