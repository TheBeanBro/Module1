from stock import Stock


def add_stock():
    stock = Stock()
    stock.add_stock()


def allocate_stock():
    allocate = Stock()
    allocate.allocate_stock()


def review_stock():
    review = Stock()
    review.review_stock()


def program():
    print("0: add stock")
    print("1: allocate stock")
    print("2: review stock")
    print("3: exit program")
    choice = int(input("Answer: "))
    if choice == 0:
        add_stock()
        program()
    elif choice == 1:
        allocate_stock()
        program()
    elif choice == 2:
        review_stock()
        program()
    elif choice == 3:
        exit()
    else:
        print("ERR: please give a number which is relavent to your choice")


program()
