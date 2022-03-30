# Utwórz klasy do reprezentacji Produktu, Zamówienia, Jabłek i Ziemniaków.
# Stwórz po kilka obiektów typu jabłko i ziemniak i wypisz ich typ za pomocą funkcji wbudowanej type.
# Stwórz listę zawierającą 5 zamówień oraz słownik, w którym kluczami będą nazwy produktów, a wartościami instancje klasy produkt.

class Product:
    pass

class Order:
    pass

class Apple:
    pass

class Ziemniaki:
    pass

if __name__ == '__main__':

    green_apple = Apple()
    red_apple = Apple()
    print(f"green apple type : {type(green_apple)}")

    old_potato = Ziemniaki()
    young_potato = Ziemniaki()
   
    print(f"young potato type : {type(young_potato)}")

    orders = [Order(), Order(), Order()]
    print(orders)

    products = {
        'Apple' : Product(),
        'Potatto' : Product(),
        'Carrot' : Product()
    }
    print(products)