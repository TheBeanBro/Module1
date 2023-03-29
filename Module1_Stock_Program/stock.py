class Stock:
    def __init__(self, stock=[], my_items={}) -> None:
        self.stock = stock
        self.my_items = my_items

    def add_stock(self):
        stock = input('Stock: ')
        stock.lower()

        self.stock.append(stock)
        for element in self.stock:
            print(element)

    def allocate_stock(self):
        for item in self.stock:
            self.my_items = {item: []}
            print(self.my_items)

            price = float(input('Price: '))
            self.my_items[item].append(price)

    def remove_stock(self):
        for item in self.stock:
            print(self.my_items)

    def review_stock(self):
        print()
