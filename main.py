import pandas as pd

class Transaction:
    def __init__(self):
        self.items = {}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item_name, qty, item_price):
        self.items[item_name] = {"qty": qty, "item_price": item_price, "total_item_price": qty * item_price}

        self.check_order()

    def update_item_name(self, item_name, new_item_name):
        try:
            self.items[new_item_name] = self.items.pop(item_name)
        except KeyError:
            print(f"Oops! Tidak ada item {item_name} di keranjang")

        self.check_order()

    def update_item_qty(self, item_name, new_qty):
        try:
            self.items[item_name]['qty'] = new_qty
        except KeyError:
            print(f"Oops! Tidak ada item {item_name} di keranjang")

        self.check_order()

    def update_item_price(self, item_name, new_price):
        try:
            self.items[item_name]['item_price'] = new_price
        except KeyError:
            print(f"Oops! Tidak ada item {item_name} di keranjang")

        self.check_order()

    def delete_item(self, item_name):
        try:
            del self.items[item_name]
        except KeyError:
            print(f"Oops! Tidak ada item {item_name} di keranjang")

        self.check_order()

    def check_order(self):
        name = []
        qty = []
        item_price = []
        total_item_price = []

        for k, _ in self.items.items():
            name.append(k)
            qty.append(self.items[k]['qty'])
            item_price.append(self.items[k]['item_price'])
            total_item_price.append(self.items[k]['total_item_price'])

        data = {
            'Nama Item': name,
            'Qty': qty,
            'Harga per item': item_price,
            'Total harga item': total_item_price
        }

        trx_df = pd.DataFrame(data)
        trx_df.index += 1

        print(trx_df[['Nama Item', 'Qty', 'Harga per item', 'Total harga item']])

    def total_price_print(self):
        self.calculate_total_price()
        self.check_order()
        print("")
        print(f"HARGA: Rp {self.total_price}")
        print(f"DISKON: {self.discount}%")
        print(f"TOTAL: Rp {self.total_price - (self.total_price * self.discount / 100)}")

    def reset_transaction(self):
        self.items = {}
        print("Semua item berhasil didelete!")

    def calculate_total_price(self):
        for key, value in self.items.items():
            self.total_price += self.items[key]["total_item_price"]

        self.calculate_discount()

    def calculate_discount(self):
        if self.total_price > 200_000 and self.total_price <= 300_000:
            self.discount = 5
        elif self.total_price > 300_000 and self.total_price <= 500_000:
            self.discount = 8
        elif self.total_price > 500_000:
            self.discount = 10
        else:
            self.discount = 0