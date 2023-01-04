def add(*args):
    output = 0
    for arg in args:
        output += arg
    return output


def calculate(**kwargs):
    my_sum = 0
    for key, value in kwargs.items():
        if key == "add":
            my_sum += value
        elif key == "multiply":
            my_sum *= value
    return my_sum


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")


print(add(3, 4, 5, 6, 7))
print(calculate(add=3, multiply=5))

car = Car(model="gti", make="Nissan")
print(car.model)
