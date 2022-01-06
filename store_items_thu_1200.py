#Item 
#name (vārds)
#price (cena)
#quantity (daudzums)

class Prece:
    all = []
    def __init__(self, name: str, price: float, quantity: int = 0):
        assert price > 0, 'Kļuda: cena nevarbūt negatīva!'
        assert quantity >= 0, 'Kļuda: daudzums nevarbūt negatīvs!'
        
        self.name = name
        self.price = price
        self.quantity = quantity
        Prece.all.append(self)

    def change_quantity(self, count):
        if count < 0:
            assert self.quantity >= abs(count), 'Kļūda: nevar pārdod vairāk nekā ir!'
        self.quantity += count

p1 = Prece('Laptop', 600, 10)
p2 = Prece('Phone', 230, 5)
p3 = Prece('Table', 50)

for prece in Prece.all:
    print(f'{prece.name}, {prece.price}, {prece.quantity}')

p1.change_quantity(-12)

for prece in Prece.all:
    print(f'{prece.name}, {prece.price}, {prece.quantity}')
