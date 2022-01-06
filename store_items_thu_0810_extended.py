class Prece:
    all = []
    def __init__(self, name: str, price: float, quantity: int = 0):               
        self.name = name
        self.price = price
        self.quantity = quantity
        Prece.all.append(self)

    def change_quantity(self, count):
        if count < 0:
            assert self.quantity >= abs(count), 'Kļūda: nevar pārdod vairāk nekā ir!'
        self.quantity += count

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        assert value >= 0, 'Kļuda: daudzums nevar būt negatīvs!'
        self._quantity = value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        assert value > 0, 'Kļuda: cena nevar būt negatīva vai nulle!'
        self._price = value

    @property
    def total_price(self):
        return self._total_price

    @total_price.getter
    def total_price(self):
        return self.price * self.quantity

p1 = Prece('Laptop', 560, 10)
p2 = Prece('Phone', 230, 5)
p3 = Prece('Table', 50)

for prece in Prece.all:
    print(f'{prece.name}, {prece.price}, {prece.quantity}')

p1.total_price = 8000
print(p1.total_price)