class Prece:
    all = []
    def __init__(self, name: str, price: float, quantity: int = 0):
        assert price >= 0, "Kļūda: cena nevar būt negatīva!" #assert pārliecinās, vai ir tāda vertība
        assert price >= 0, "Kļūda: daudzum nevar būt negatīvs!" 
        self.name = name
        self.price = price
        self.quantity = quantity
        Prece.all.append(self)

    def change_quantity(self, count):
        if count < 0:
            assert self.quantity >= count, "Kļūda: nevar pārdod vairāk nekā ir!"
        self.quantity += count
      
p1 = Prece("TV", 1300, 12)
p2 = Prece("Fridge", 700, 4)
p3 = Prece("Playstation 5", 600)

for prece in Prece.all:
    print(f'{prece.name}, {prece.price}, {prece.quantity}')

p1.change_quantity(-1000)