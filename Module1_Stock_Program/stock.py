class Stock:
    def __init__(self):
        pass

    def add_stock(self):
        choice = input("Choose branch b1/b2: ")
        choice.lower()
        branch1 = {}
        if choice == 'b1':
            print("branch1: ")
            for i in range(1):
                name = str(input("Name of item: "))
                price = float(input("Allocate Price: "))
                quantity = int(input("Allocate Quantity: "))

                branch1[name] = {"Price: ": [price], "Quantity": [quantity]}
            print(branch1)
        elif choice == 'b2':
            print("branch2: ")
        else:
            print("ERR: not a valid branch")
