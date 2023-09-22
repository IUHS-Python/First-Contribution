class Restaurant:
    def __init__(self):
        self.add_menu={}
        self.book_tabel=[]
        self.customer_order=[]

    def add_item_to_menu(self,item,price):
        self.add_menu[item]=price
    def book_tabels(self,tabel_numbur):
        self.book_tabel.append(tabel_numbur)

    def customer_orders(self,tabel_number,order):
        order_details={'tabel_number':tabel_number,'order':order}
        self.customer_order.append(order_details)

    def print_menu(self):
        for item,price in self.add_menu.items():
            print("{} : {}".format(item,price))
    def print_tabel_number(self):
        for table in self.book_tabel :
            print("tabel {}".format(table))

    def print_customer_orders(self):
        for order in self.customer_order:
            print("table {} : {}".format(order['tabel_number'],order['order']))

restaurant=Restaurant()

restaurant.add_item_to_menu("Cheeseburger", 9.99)
restaurant.add_item_to_menu("Caesar Salad", 8)
restaurant.add_item_to_menu("Grilled Salmon", 19.99)
restaurant.add_item_to_menu("French Fries", 3.99)
restaurant.add_item_to_menu("Fish & Chips:", 15)

restaurant.book_tabels(1)
restaurant.book_tabels(2)
restaurant.book_tabels(3)
restaurant.book_tabels(4)

restaurant.customer_orders(1, "Cheeseburger")
restaurant.customer_orders(1, "Grilled Salmon")
restaurant.customer_orders(2, "Fish & Chips")
restaurant.customer_orders(2, "Grilled Salmon")

restaurant.print_menu()
print()
restaurant.print_tabel_number()
print()
restaurant.print_customer_orders()