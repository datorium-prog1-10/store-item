#klase Prece
#name (nosaukums)
#price (cena)
#quantity (daudzums)

class Prece:
    all = []
    store_name = "DaStore"
    def __init__(self, name: str, price: float, quantity: int = 0):
        self.name = name
        self.price = price
        self._quantity = quantity
        Prece.all.append(self)

    @property
    def quantity(self):
        return self._quantity
    
    # @quantity.setter
    # def quantity(self, value):
    #     assert value >= 0, 'Kļūda: daudzums nevar būt negatīvs'
    #     self._quantity = value
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        assert value > 0, 'Kļūda: cena nevar būt negatīvs skaitlis'
        self._price = value

    @property
    def total_price(self):
        return self._total_price

    @total_price.getter
    def total_price(self):
        return self.price * self.quantity

    def add_quantity(self, count):  
        self._quantity += count

    def reduce_quantity(self, count):
        assert self.quantity >= count, 'Kļūda: nevar pārdod vairāk nekā ir!'
        self._quantity -= count

    def get_total_price(self):
        return self.price * self.quantity

    
p1 = Prece("Laptop", 560, 10)
p2 = Prece("Phone", 120, 15)
p3 = Prece("Table", 60)

for prece in Prece.all:
    print(f'{prece.name}, {prece.price}, {prece.quantity}')

print(p2.total_price)