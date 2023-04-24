# Stock class
class Stock:
    # Make a dictionary that represents the branches
    def __init__(self):
        self.branches = {}

    # A function that adds the 'branch_name' to the branches, each having it's own dictionary
    def add_branch(self, branch_name):
        self.branches[branch_name] = {}

    # A function that adds items to a valid branch stored in the branches dictionary
    def add_items(self, branch_name, item_name, price, qty):
        # Check if the branch name exists within the branches dictionary
        if branch_name not in self.branches:
            # Tell the user that the branch they entered doesn't exist in branches
            print(f"The branch: {branch_name} does not exist.")
            # Tell computer result of function is None
            return
        # The branches dictionary is equivilant to {Name of branch: {Item: price, quantity}}
        self.branches[branch_name][item_name] = price, qty

    # A function that destroys items from the desired branch
    def destroy_item(self, branch_name, item_name):
        # Make sure the branch name exists within the branches dictionary
        if branch_name not in self.branches:
            # Tell the user the branch does not exist
            print(f"The branch: {branch_name} does not exist.")
            # Tell computer result of function is None
            return
        # Make sure item exists within the branch chosen
        if item_name not in self.branches[branch_name]:
            # Tell the user the item does not exist within the branch chosen
            print(f"There is no item: {item_name} in the branch: {branch_name}")
            # Tell the computer that the result of the function is None
            return
        # After the computer checks the users answers it will make sure to delete the item
        del self.branches[branch_name][item_name]

    # Function to show the user their branches and items
    def review_stock(self):
        # Check if the branch name and the items in the branches are within the branches dictionary
        for branch_name, branch_items in self.branches.items():
            # Print the name of the branch
            print(f"\nBranch: {branch_name}")
            # For every item that is found within the branch, print the item and it's price
            for item_name, price in branch_items.items():
                print(f"\t{item_name}: {price}")

# Insantiate an object of stock
stock = Stock()

# Infinite loop
while True:
    print("\n1. Add branch\n2. Add item\n3. Remove item\n4. Print stock\n5. Exit")
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        branch_name = input("Enter branch name: ")
        stock.add_branch(branch_name)
        print(f"{branch_name} branch added | successful.")

    elif choice == "2":
        try:
            branch_name = input("Enter branch name that you want to add to: ")
            item_name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            qty = int(input("Enter quantity of item: "))
        except ValueError:
            print("unsuccessful (not a valid value)\nbranch_name must be characters\nitem_name must be characters\nprice must be a integer/integer with decimal\nquantity must be an integer\n")
        stock.add_items(branch_name, item_name, price, qty)
        if branch_name not in stock.branches:
            print(f"{item_name} added to branch: {branch_name} | unsuccessful. (branch does not exist).")
        elif item_name in stock.branches[branch_name]:
            print(f"There is no item {item_name} in the branch: {branch_name}")
        else:
            print(f"{item_name} added to branch: {branch_name} | successfull.")

    elif choice == "3":
        branch_name = input("Enter the name of the branch which you want to remove an item from: ")
        item_name = input("Enter item name: ")
        stock.destroy_item(branch_name, item_name)
        if branch_name not in stock.branches:
            print(f"{item_name} removed from the branch: {branch_name} | unsuccessful (branch does not exist).")
        else:
            print(f"{item_name} removed from the branch: {branch_name} branch | successful.")

    elif choice == "4":
        stock.review_stock()

    elif choice == "5":
        print("Goobye!")
        break

    else:
        print("Invalid choice. Please try again.")
