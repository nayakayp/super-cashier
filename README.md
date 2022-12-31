# Tentang
Self-service cashier sederhana dengan menggunakan bahasa pemrograman Python.

## Latar Belakang
- Ketika berjualan barang akan sangat menyita waktu jika harus mencatat barang pembelian dan menghitung keseluruhan harga yang harus dibayar dari pembeli secara manual, misalnya di selembar kertas.
- Ketika banyak pembeli yang datang sedangkan pelayanan yang tersedia untuk melayani sangat terbatas, maka pembeli harus menunggu terlebih dahulu agar bisa dilayani. Ini tentunya akan membuat kepuasan pembeli menjadi menurun
- Diperlukannya sebuah sistem kasir yang dapat secara cepat dan tepat mencatat dan menghitung barang pembelian dari pembeli secara otomatis dan mandiri.

## Requirements/Objective
- Membuat proses menyelesaikan permasalahan kasir self-service untuk membantu pedagang berjualan.
- Membuat proses untuk `menambahkan barang` belanjaan.
- Membuat proses untuk `menghapus barang` belanjaan.
- Membuat proses untuk `edit nama` barang belanjaan.
- Membuat proses untuk `edit jumlah` barang belanjaan. 
- Membuat proses untuk `edit harga` barang belanjaan.
- Membuat proses untuk `menghitung total harga` barang belanjaan.
- Membuat proses untuk `menghitung diskon` barang belanjaan.
- Membuat proses untuk `mengosongkan barang` belanjaan.
- Mengecek barang belanjaan dengan `menampilkan seluruh barang belanjaan`.

## Flowchart
![Untitled Diagram](https://user-images.githubusercontent.com/24706517/210150924-1bea1e4e-c470-417c-9b0a-7e93188c96c8.jpg)

## Penjelasan Fungsi
Semua fungsi berikut terdapat di dalam class bernama `Transaction` pada file `main.py`:

#### Method
- `add_item`. Menambahkan barang dengan format `add_item([item_name, quantity, price_per_item])` ke dalam variable `items` di dalam class. Contoh: `add_item(['Ayam', 12, 15_000])`
- `delete_item`. Menghapus barang berdasarkan nama di dalam `items` jika tersedia dengan format `delete_item(item_name)`. Contoh: `delete_item('Ayam')`
- `update_item_name`. Mengganti nama barang saat ini dengan nama barang yang baru jika barang yang disebutkan tersedia dengan format `update_item_name(old_name, new_name)`. Contoh: `update_item_name('Ayam', 'Ayam Goreng')`
- `update_item_qty`. Mengganti jumlah pesanan barang jika barang yang disebutkan tersedia dengan format `update_item_name(item_name, new_qty)`. Contoh: `update_item_qty('Ayam', 20)`.
- `update_item_price`. Mengganti harga per item barang jika barang yang disebutkan tersedia dengan format `update_item_price(item_name, new_price)`. Contoh `update_item_price('Ayam', 30_000)`
- `calculate_total_price`. Menghitung harga total semua barang.
- `check_order`. Menampilkan semua barang yang telah ditambahkan beserta dengan total harga keseluruhan.
- `reset_transaction`. Mengosongkan semua barang sekaligus yang telah ditambahkan.
- `total_price_print`. Menampilkan seluruh barang beserta total harga tiap barang, discount, dan total setelah diskon.

#### Generic Function
- `__init__`. Menginisiasi variable utama pada sebuah class. Dalam hal ini adalah variable `items` yang dinisiasi.
- `calculate_discount`. Menghitung jika total keseluruhan harga barang memenuhi syarat diskon. Syarat diskon adalah sebagai berikut:
	1. Jika di atas Rp 200.000 diskon sebesar 5%
	2. Jika di atas Rp 300.000 diskon sebesar 8%
	3. Jika di atas Rp 500.000 diskon sebesar 10%
- `find_items_index`. Mencari ada di index ke berapa sebuah nama barang pada barang-barang yang sudah ditambahkan.

## Demonstrasi Code
Membuat Customer1 dengan code `Customer1 = Transaction()`
![7cdd6702-2a16-4135-b6e8-1da2e99d8932](https://user-images.githubusercontent.com/24706517/210150937-b8ca9f67-2b97-4bab-bae6-39cd9c7cb746.png)

### Test 1: add_item()
Customer ingin menambahkan dua item baru menggunakan method `add_item()`. Item yang ditambahkan adalah sebagai berikut:
- Nama Item: Ayam Goreng, Qty: 2, Harga: 20000
- Nama Item: Pasta Gigi, Qty: 3, Harga: 15000

**Output:**
![af6367f8-fc1b-4812-8737-61371bd02cab](https://user-images.githubusercontent.com/24706517/210150963-e800e75a-c65e-4387-816d-628d746e6045.png)
![88d2953e-9810-44fd-8079-f9ccbdf82d5e](https://user-images.githubusercontent.com/24706517/210150970-996887d5-7136-4b6a-a874-3aad202ece9b.png)


### Test 2: delete_item()
Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka Customer menggukan method `delete_item()` untuk menghapus item. Item yang ingin dihapuskan adalah **Pasta Gigi**.

**Output:**
![76f8318e-6382-4730-983e-f7a965e91609](https://user-images.githubusercontent.com/24706517/210150989-d088f6dc-b84a-4d03-a4e0-58fcba2efe8c.png)


### Test 3: reset_transaction()
Ternyata setelah dipikir-pikir, Customer salah memasukkan item yang ingin dibelanjakan! Daripada menghapusnya satu - satu, maka Customer cukup menggunakan method `reset_transaction()` untuk menghapus semua item yang sudah ditambahkan.

**Output:**
![968e3200-3384-4b00-908c-408cdf120261](https://user-images.githubusercontent.com/24706517/210151004-7595102c-2295-4c95-aa2b-d371ee05f86b.png)


### Test 4: total_price_print()
Setelah Customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan method `total_price_print()`. Sebelum mengeluarkan output total belanja akan menampilkan item - item yang dibeli. Item yang ditambahkan adalah sebagai berikut:
- Nama Item: Ayam Goreng, Qty: 2, Harga: 20000
- Nama Item: Pasta Gigi, Qty: 3, Harga: 15000

**Output:**
![af6367f8-fc1b-4812-8737-61371bd02cab](https://user-images.githubusercontent.com/24706517/210151020-c3fa620b-f6ad-4daa-8585-ca674e7bf5ab.png)
![88d2953e-9810-44fd-8079-f9ccbdf82d5e](https://user-images.githubusercontent.com/24706517/210151025-119c5f17-9b46-4753-9791-073efe76f673.png)
![b0120508-12f2-4a94-a756-8b575d4fc43c](https://user-images.githubusercontent.com/24706517/210151035-85c815ce-e420-4000-8891-e1407219fa50.png)


### Test 5: update_item_name()
Item yang ditambahkan adalah sebagai berikut:
- Nama Item: Ayam Goreng, Qty: 2, Harga: 20000
Customer ingin mengganti nama **Ayam Goreng** yang terlanjur ditambahkan menggunakan metode `update_item_name()` sehingga nama item tersebut menjadi **Ayam Goreng Balado**

**Output:**
![f97c103c-8ef9-4151-bb91-f0433c0b7d87](https://user-images.githubusercontent.com/24706517/210151089-3ff9bcd4-6b70-4eeb-a132-8516163b8d73.png)
_Setelah nama diupdate_
![aa4e06d1-295b-4094-ad3f-3b1d522b8d10](https://user-images.githubusercontent.com/24706517/210151096-a6526741-3654-48ed-8f8b-03592630462a.png)


### Test 6: update_item_qty()
Customer ingin mengganti Quantity dari **Ayam Goreng Balado** yang sebelumnya 2 buah menjadi 10 buah dengan metode `update_item_qty()`

**Output:**
![3a2f22d7-7f76-4bf0-8ef9-886f9d411e75](https://user-images.githubusercontent.com/24706517/210151107-ad15c629-ee50-4117-81b1-71a114647466.png)
_Setelah qty diupdate_
![df029b88-1602-440c-85b8-567e5a8f6724](https://user-images.githubusercontent.com/24706517/210151112-0cdbbe87-1dad-491e-8add-1dc2558a3ee7.png)

### Test 7: update_item_price()
Customer ingin mengganti harga per item dari **Ayam Goreng Balado** yang sebelumnya 20000 menjadi 25000 per item-nya dengan metode `update_item_price()`.

**Output**:
![df029b88-1602-440c-85b8-567e5a8f6724](https://user-images.githubusercontent.com/24706517/210151119-8ff07d98-9a3e-4898-8c3d-340e39dc7226.png)
_Setelah harga diupdate_
![21169f22-9f74-4902-a162-dc2d7ddb1a69](https://user-images.githubusercontent.com/24706517/210151124-e7e08787-210d-4372-a462-c21b977b6e17.png)


## Kesimpulan
- Super cashier adalah program sederhana yang membantu penjual untuk menjual produknya secara efektif dan efisien.
- Terdapat fitur menambahkan barang, mengedit barang (nama, quantity, harga per item), menghapus barang, dan menjumlahkan keseluruhan harga barang beserta diskonnya secara cepat dan tepat.
- Keseluruhan fitur tersebut dapat memudahkan dan mempercepat pembeli untuk membeli barangnya secara mandiri.

## Future Work
- Membuat GUI (_Graphical User Interface_)
- Membuat sistem pembayaran yang terintegrasi dengan sistem kasir
