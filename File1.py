class MyRestaurent():
    def  __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = []

    def add_item_to_menu(self, item, price):
        self.menu_items[item] = price

    def book_tables(self,table_number):
        if table_number not in self.book_table:
            self.book_table.append(table_number)

    def customer_order(self, table_number, order):
        order_details = {'table_number': table_number, 'order': order}
        self.customer_orders.append(order_details)

    def print_menu(self):
        for item,price in self.menu_items.items():
            print('{}: {}'.format(item, price))

    def print_table_reservations(self):
        for table in self.book_table:
            print('Table : {}'.format(table))

    def print_customer_orders(self):
        for order in self.customer_orders:
            print('Table {}: {}'.format(order['table_number'], order['order']))


restaurant = MyRestaurent()
restaurant.add_item_to_menu('Kottu', 500)
restaurant.add_item_to_menu('Berger', 650)
restaurant.add_item_to_menu('Rice', 350)
restaurant.add_item_to_menu('Yogut', 100)

restaurant.print_menu()
print()
restaurant.book_tables(1)
restaurant.book_tables(2)
restaurant.book_tables(3)

restaurant.print_table_reservations()
print()
restaurant.customer_order(1, ['Kottu','Hoppers', 'Fish Kottu', 'Nann Rotti', 'Fish Curry'])
restaurant.customer_order(4, 'Fish Kottu')
restaurant.customer_order(2, 'Egg Kottu')
restaurant.customer_order(3, 'Cheese Kottu')

restaurant.print_customer_orders()