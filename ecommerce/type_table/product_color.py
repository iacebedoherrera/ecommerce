
class Color:
    _color = {
        "white": "01",
        "black": "02",
        "beige": "03"
    }


    @classmethod
    def get_id(cls, color_str):
        return cls._color.get(color_str)
    
    @classmethod
    def get_size(cls, id):
        for key, val in cls._color.items():
            if val == id:
                return key
        return None