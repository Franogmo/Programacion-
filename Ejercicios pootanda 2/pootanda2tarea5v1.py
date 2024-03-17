"""
Goal of the program: A stack and a pile, both made with OOP.
by Fran Ogallas
Development start date: 29th of January 2024. Last modification date: 29th of January 2024.
"""


class Stack:

    def __init__(self, value=[]):
        if type(value) is list:
            self.__load = value
        elif type(value) is Stack:
            self.__load = value.__load
        elif type(value) is tuple:
            self.__load = []
            for n in range(len(value)):
                self.__load.append(value[n])
        else:
            self.__load = [value]

    def __str__(self):
        return str(self.__load)

    def __len__(self):
        return len(self.__load)

    def is_empty(self):
        if len(self.__load) == 0:
            return True
        else:
            return False

    def empty(self):
        self.__load = []

    def push(self, item):
        self.__load.insert(0, item)

    def pop(self):
        item = self.__load[0]
        self.__load = self.__load[1:]
        return item

    def see_top_element(self):
        return self.__load[0]


class Queue:

    def __init__(self, value=[]):
        if type(value) is list:
            self.__load = value
        elif type(value) is Queue:
            self.__load = value.__load
        elif type(value) is tuple:
            self.__load = []
            for n in range(len(value)):
                self.__load.append(value[n])
        else:
            self.__load = [value]

    def __str__(self):
        return str(self.__load)

    def __len__(self):
        return len(self.__load)

    def is_empty(self):
        if len(self.__load) == 0:
            return True
        else:
            return False

    def empty(self):
        self.__load = []

    def enqueue(self, item):
        self.__load.append(item)

    def dequeue(self):
        item = self.__load[0]
        self.__load = self.__load[1:]
        return item

    def see_top_element(self):
        return self.__load[0]


def main():
    stack1 = Stack((1, 2, 3, 4))
    queue1 = Queue((1, 2, 3, 4))
    print(f"El tamaño de la pila es de {len(stack1)} elementos")
    print(f"El tamaño de la cola es de {len(queue1)} elementos")
    stack1.push(7)
    queue1.enqueue(7)
    print(f"Se ha extraído el primer elemento de la pila. Que era este: {stack1.pop()}")
    print(f"Se ha extraído el primer elemento de la cola. Que era este: {queue1.dequeue()}")
    print(f"Elemento superior actual de la pila: {stack1.see_top_element()}")
    print(f"Elemento superior actual de la cola: {queue1.see_top_element()}")
    print("Creando una nueva pila y cola, a las que se le añadirán un 8")
    stack2 = Stack(stack1)
    queue2 = Queue(queue1)
    stack1.push(8)
    queue1.enqueue(8)
    print(f"Segunda pila: {stack2}")
    print(f"Segunda cola: {queue2}")


if __name__ == "__main__":
    main()
