class Stock:
    def __init__(self, branch={}):
        self.branch = branch

    def add_stock(self):
        choice = input("Choose branch b1/b2: ")
        choice.lower()
        branch1 = {}
        branch2 = {}
        if choice == 'b1':
            print("branch1: ")
            for i in range(1):
                name = str(input("Name of item: "))
                price = float(input("Allocate Price: "))
                quantity = int(input("Allocate Quantity: "))

                branch1[name] = {"Price: ": [price], "Quantity": [quantity]}
                self.branch.update(branch1)
            print(self.branch)
        elif choice == 'b2':
            print("branch2: ")
            for i in range(1):
                name = str(input("Name of item: "))
                price = float(input("Allocate Price: "))
                quantity = int(input("Allocate Quantity: "))

                branch2[name] = {"Price: ": [price], "Quantity": [quantity]}
            print(branch2)

        else:
            print("ERR: not a valid branch")
