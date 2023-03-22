from stock import Stock


def add():
    stock = Stock()
    stock.add_stock()


def program():
    print("0: add stock")
    print("1: remove stock")
    print("2: review stock")
    print("3: exit program")
    choice = int(input("Answer: "))
    if choice == 0:
        add()
        program()
    elif choice == 1:
        pass
    elif choice == 2:
        review_list = Stock()
        review_list.review()
        program()
    elif choice == 3:
        exit()
    else:
        print("ERR: please give the corresponding number which is relavent to your choice")


program()
