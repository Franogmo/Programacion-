"""
Goal of the program: A shopping cart.
By Fran Ogallas
Project start date: 18th of March 2024. Last update: 18th of March 2024.
"""
from __future__ import annotations
from typeguard import typechecked


@typechecked()
class Element:

    def __init__(self, name: str, prize: float, amount: int):
        self.__name = name
        self.__prize = prize
        self.__amount = self.__errorcheck_amount(amount)

    @property
    def name(self):
        return self.__name

    @property
    def prize(self):
        return self.__prize

    @property
    def amount(self):
        return self.__amount

    def __hash__(self):
        return hash(str(self.__name) + str(self.__prize))

    def __errorcheck_amount(self, amount):
        if amount < 1:
            raise ValueError("Elements cannot have negative nor null amounts")
        return amount

    def change_amount(self, change: int):
        self.__amount = self.__errorcheck_amount(self.__amount + change)

    def __str__(self):
        return f"{self.name}"

    def __eq__(self, other: Element):
        return (self.__name, self.__prize) == (other.__name, other.__prize)


@typechecked()
class ShoppingCart:

    def __init__(self):
        self.__content = set()

    def add(self, product: Element):
        if product in self.__content:
            content_list = list(self.__content)
            for n in range(self.size):
                if content_list[n] == product:
                    content_list[n].change_amount(product.amount)
        else:
            self.__content.add(product)

    def remove(self, product_name: str, amount: int):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        content_list = list(self.__content)
        for n in range(self.size):
            if content_list[n].name == product_name:
                if content_list[n].amount - amount == 0:
                    content_list[n].remove()
                else:
                    content_list[n].change_amount(amount)

    @property
    def size(self):
        return len(self.__content)

    def subamount(self, product: Element):
        return product.prize * product.amount

    def total_prize(self):
        total_prize = 0
        content_list = list(self.__content)
        for n in range(self.size):
            total_prize += self.subamount(content_list[n])
        return total_prize

    def __str__(self):
        content_list = list(self.__content)
        x = f"Contenido del carrito\n=====================\n"
        for n in range(self.size):
            x += (f"{content_list[n].name} PVP: "
                  f"{content_list[n].prize} Subtotal: {self.subamount(content_list[n])}\n")
        return x


def main():
    mi_carrito = ShoppingCart()
    mi_carrito.add(Element("Tarjeta SD 64Gb", 19.95, 2))
    mi_carrito.add(Element("Canon EOS 2000D", 449, 1))
    print(mi_carrito)
    print(f"Hay {mi_carrito.size} productos en la cesta.")
    print(f"El total asciende a {mi_carrito.total_prize():.2f}  euros")

    print("\nContinúa la compra...\n")
    mi_carrito.add(Element("Samsung Galaxy Tab", 199, 3))
    mi_carrito.add(Element("Tarjeta SD 64Gb", 19.95, 1))
    print(mi_carrito)
    print(f"Ahora hay {mi_carrito.size} productos en la cesta.")
    print(f"El total asciende a {mi_carrito.total_prize():.2f}  euros")


if __name__ == "__main__":
    main()
