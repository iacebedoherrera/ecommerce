
class Size:
    _size = {
        "XS": "01",
        "S": "02",
        "M": "03",
        "L": "04",
        "XL": "05"
    }


    @classmethod
    def get_id(cls, size_str):
        return cls._size.get(size_str)
    
    @classmethod
    def get_size(cls, id):
        for key, val in cls._size.items():
            if val == id:
                return key
        return None