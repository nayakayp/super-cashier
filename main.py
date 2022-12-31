import pandas as pd

class Transaction:
    def __init__(self):
        self.items = []
        self.total_price = 0
        self.discount = 0

    def add_item(self, item):
        self.items.append(item)
        self.calculate_total_price()
        print(f"Item yang dibeli adalah {item[0]} sebanyak {item[1]}\n")
        self.check_order()

    def update_item_name(self, item_name, new_item_name):
        item_index = self.find_items_index(item_name)
        if item_index != None:
            self.items[item_index][0] = new_item_name
        else:
            print(f"Tidak ada item {item_name} di keranjang")

        self.check_order()

    def update_item_qty(self, item_name, new_qty):
        item_index = self.find_items_index(item_name)
        if item_index != None:
            self.items[item_index][1] = new_qty
            self.calculate_total_price()
        else:
            print(f"Tidak ada item {item_name} di keranjang")

        self.check_order()

    def update_item_price(self, item_name, new_price):
        item_index = self.find_items_index(item_name)
        if item_index != None:
            self.items[item_index][2] = new_price
            self.calculate_total_price()
        else:
            print(f"Tidak ada item {item_name} di keranjang")

        self.check_order()

    def delete_item(self, item_name):
        item_index = self.find_items_index(item_name)
        if item_index != None:
            self.items.pop(item_index)
        else:
            print(f"Tidak ada item {item_name} di keranjang")

        self.check_order()

    def check_order(self):
        trx_df = pd.DataFrame(self.items, columns=['Item Name', 'Quantity', 'Price', 'Total Price'])
        trx_df.index = trx_df.index + 1
        print(trx_df, '\n')

    def total_price_print(self):
        self.check_order()
        print(f"HARGA: {self.total_price}")
        print(f"DISKON: {self.discount}")
        print(f"TOTAL: {self.total_price - (self.total_price * self.discount / 100)}")

    def reset_transaction(self):
        self.items = []
        print("Semua item berhasil didelete!")

    def find_items_index(self, item_name):
        for idx, item in enumerate(self.items):
            if item_name == item[0]:
                return (idx)

    def calculate_total_price(self):
        for item in self.items:
            total_price_per_item = item[1] * item[2]
            self.total_price = self.total_price + total_price_per_item
            self.calculate_discount()
            if len(item) == 3:
                item.insert(3, total_price_per_item)
            else:
                item[3] = total_price_per_item

    def calculate_discount(self):
        if self.total_price > 200_000 and self.total_price <= 300_000:
            self.discount = 5
        elif self.total_price > 300_000 and self.total_price <= 500_000:
            self.discount = 8
        elif self.total_price > 500_000:
            self.discount = 10
        else:
            self.discount = 0