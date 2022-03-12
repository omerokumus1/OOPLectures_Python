class DBManager:

    def __init__(self, connection_code):
        self.connection_code = connection_code


class HtmlParser:

    # def __init__(self, link):
    #     self.link = link

    def send_request(self, link):
        pass

    def get_response(self):
        pass

    def parse_json(self):
        pass

    # def set_new_link(self, link):
    #     self.link = link


class Person:
    age = None

    def __init__(self, age):
        self.set_age(age) # methodlarla logic implement edilir. property'lere kısıtlama getirilebilir. Örn; age 0'dan büyük eşit olmalı

    def set_age(self, age):
        if age >= 0:
            self.age = age


p = Person(-5)
print(p.age)


class Mouse:
    """
        Objeler 2 karakteristiğe sahiptir.
                1. Özellikler (data field): durağan özelliklerdir. renk, ağırlık, şekil vb şeylerdir. Değişkenlerde tutulur
                2. Yapabilecekleri (behaviors): hareketli özelliklerdir. db bağlantısı kurma, istek atma vs. methodlarla tanımlanır.
    """
    def __init__(self, color, brand, price, weight, shape):
        # data field, properties, attributes
        self.color = color
        self.brand = brand
        self.price = price
        self.weight = weight
        self.shape = shape

    # behaviors, methods
    def move_right(self):
        print("Moving right")

    def move_left(self):
        print("Moving left")

    def move_up(self):
        print("Moving up")

    def move_down(self):
        print("Moving down")

    def left_click(self):
        print("left clicked")

    def right_click(self):
        print("right clicked", self.color)

"""
    method: obje olmadan kullanılamaz. self kelimesini barındırır.
    function: obje olmadan kullanılabilir. self kelimesini barındırmaz.
"""