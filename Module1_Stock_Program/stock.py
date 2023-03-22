class Stock:
    def __init__(self, branch1={}, branch2={}, itm=""):
        self.branch1 = branch1
        self.branch2 = branch2
        self.itm = itm

    def add_stock(self):
        choice = input("Choose branch b1/b2: ")
        choice.lower()

        # If choice ==>
        if choice == 'b1':

            # Branch 1
            print("branch1: ")
            for i in range(1):
                # Ask for name
                itm = str(input("Name of item: "))

                # Add name to list and print it
                self.branch1[itm] = {}
            print(self.branch1)

        # If choice == 'b2'
        elif choice == 'b2':

            # Branch 2
            print("branch2: ")
            for i in range(1):
                # Ask for name
                itm = str(input("Name of item: "))

                # Add name to list and print it
                self.branch2[itm] = {}
            print(self.branch2)

        else:
            print("ERR: not a valid branch")

    def review(self):
        choice = input("Choose branch b1/b2: ")
        choice.lower()
        if choice == 'b1':
            print(self.branch1)
        elif choice == 'b2':
            print(self.branch2)
        else:
            print("ERR: please choose b1/b2")
