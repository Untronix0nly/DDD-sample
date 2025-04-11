class Title:
    __value: str

    __limit_size: int = 200

    def __init__(self, value: str):
        if len(value) > self.__limit_size:
            raise ValueError("Maximum title size is 200 characters")
        self.__value = value

    def __str__(self):
        return self.__value
