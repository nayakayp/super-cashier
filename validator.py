
def validate_add_item(item_name, qty, item_price):
    if type(item_name) is not str:
        print("Nama item harus berupa string, terdapat ''!")
        return False
    if type(qty) is not int:
        print("Qty harus berupa angka!")
        return False
    if type(item_price) is not int:
        print("Harga item harus berupa angka!")
        return False
    if qty <= 0:
        print("Qty tidak boleh negatif atau 0!")
        return False
    if item_price < 0:
        print("Harga item tidak boleh negatif!")
        return False
    return True

def validate_update_item_name(item_name, new_item_name):
    if type(item_name) is not str:
        print("Nama item harus berupa string, terdapat ''!")
        return False
    if type(new_item_name) is not str:
        print("Nama item baru harus berupa string, terdapat ''!")
        return False
    return True

def validate_update_item_qty(item_name, new_qty):
    if type(item_name) is not str:
        print("Nama item harus berupa string, terdapat ''!")
        return False
    if type(new_qty) is not int:
        print("Qty baru harus berupa angka!")
        return False
    if new_qty <= 0:
        print("Qty baru tidak boleh negatif atau 0!")
        return False
    return True

def validate_update_item_price(item_name, new_price):
    if type(item_name) is not str:
        print("Nama item harus berupa string, terdapat ''!")
        return False
    if type(new_price) is not int:
        print("Harga item baru harus berupa angka!")
        return False
    if new_price < 0:
        print("Harga item baru tidak boleh negatif!")
        return False
    return True