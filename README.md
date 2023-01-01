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

#### Modul
- `validate_add_item`. Validasi sebelum item ditambahkan. Meliputi format penulisan dan harga barang/qty tidak boleh negatif.
- `validate_update_item_name`. Validasi sebelum item diganti namanya. Meliputi format penulisan nama item baru dan nama item lama.
- `validate_update_item_qty`. Validasi sebelum qty item diupdate. Meliputi format penulisan dan qty tidak boleh negatif.
- `validate_update_item_price`. Validasi sebelum harga item diupdate. Meliputi format penulisan dan harga tidak boleh negatif.

## Demonstrasi Code
Membuat Customer1 dengan code `Customer1 = Transaction()`
![7cdd6702-2a16-4135-b6e8-1da2e99d8932](https://user-images.githubusercontent.com/24706517/210150937-b8ca9f67-2b97-4bab-bae6-39cd9c7cb746.png)

### Test 1: add_item()
Customer ingin menambahkan dua item baru menggunakan method `add_item()`. Item yang ditambahkan adalah sebagai berikut:
- Nama Item: Ayam Goreng, Qty: 2, Harga: 20000
- Nama Item: Pasta Gigi, Qty: 3, Harga: 15000

**Output:**
![6d594746-c5e6-414f-8357-fae10ef5187a](https://user-images.githubusercontent.com/24706517/210166197-f7d170f6-aae2-499d-b6bf-63bfc65b0c35.png)
![1b8948eb-ac69-4593-91d6-39a6a10d5b4a](https://user-images.githubusercontent.com/24706517/210166208-3c0358f9-60c4-4207-abf5-16879a89f7b9.png)


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
![63a730b1-a5b8-4e7e-88f3-d3a3aa8e5bac](https://user-images.githubusercontent.com/24706517/210166274-41cacc23-09e7-451c-bf09-355c6d6c6c83.png)
![9faf5655-d056-413f-b701-a510c254824c](https://user-images.githubusercontent.com/24706517/210166275-8dccabfb-6689-4b44-b3a2-85dacb7fb000.png)
![f8030d9c-a799-409a-b259-1cc4f6b98aa9](https://user-images.githubusercontent.com/24706517/210166276-a28641ed-7004-44d5-be9a-00e9b1d9798a.png)



### Test 5: update_item_name()
Item yang ditambahkan adalah sebagai berikut:
- Nama Item: Ayam Goreng, Qty: 2, Harga: 20000
Customer ingin mengganti nama **Ayam Goreng** yang terlanjur ditambahkan menggunakan metode `update_item_name()` sehingga nama item tersebut menjadi **Ayam Goreng Balado**

**Output:**
![75c37fed-c122-4270-b09e-f4a9877f657a](https://user-images.githubusercontent.com/24706517/210166311-c87cef71-d664-4ac7-8de0-2410c782c0be.png)
_Setelah nama diupdate_
![e41d9ffc-480d-4637-a68a-5877ef56000a](https://user-images.githubusercontent.com/24706517/210166313-302e0226-422e-4dd5-aa43-7b09325b1ca7.png)


### Test 6: update_item_qty()
Customer ingin mengganti Quantity dari **Ayam Goreng Balado** yang sebelumnya 2 buah menjadi 10 buah dengan metode `update_item_qty()`

**Output:**
![image](https://user-images.githubusercontent.com/24706517/210166894-34972f6a-d3f7-4dad-a940-9c75bd198628.png)
_Setelah qty diupdate_
![image](https://user-images.githubusercontent.com/24706517/210166907-b0fd9a26-e577-459d-a4f0-2de72bb8ae1b.png)

### Test 7: update_item_price()
Customer ingin mengganti harga per item dari **Ayam Goreng Balado** yang sebelumnya 20000 menjadi 25000 per item-nya dengan metode `update_item_price()`.

**Output**:
![image](https://user-images.githubusercontent.com/24706517/210166936-a67c7892-0700-4dda-a43b-7e1be2b4abd4.png)
_Setelah harga diupdate_
![image](https://user-images.githubusercontent.com/24706517/210166949-012bd4f0-00cf-4a14-870f-2fe5163c9f66.png)

### Test 8: Validasi sebelum menambahkan item
![image](https://user-images.githubusercontent.com/24706517/210167540-0839e7b0-4550-4486-8fb4-259598ad7952.png)
![image](https://user-images.githubusercontent.com/24706517/210167544-32f469cf-1dc1-4651-b731-c267a6d60235.png)
![image](https://user-images.githubusercontent.com/24706517/210167548-59950894-8d1d-4f87-af0e-9b10341a1b51.png)
![image](https://user-images.githubusercontent.com/24706517/210167554-24df2bdc-9132-4ff3-9e6e-219290f88f03.png)
![image](https://user-images.githubusercontent.com/24706517/210167558-6dcca693-291d-443a-b7f4-dc52f2a3717a.png)

### Test 9: Validasi sebelum nama item diganti
![image](https://user-images.githubusercontent.com/24706517/210167574-b367c387-c296-426a-a20d-f976e9acc5ba.png)
![image](https://user-images.githubusercontent.com/24706517/210167583-0de036b9-9f32-4380-83ac-0ceeb24ddde4.png)
![image](https://user-images.githubusercontent.com/24706517/210167592-86360c7e-ab47-466f-81a7-1a897b382a0e.png)

### Test 10: Validasi sebelum qty item diganti
![image](https://user-images.githubusercontent.com/24706517/210167618-7b8df7fd-659b-4ad1-b289-7c03a69e9cf3.png)
![image](https://user-images.githubusercontent.com/24706517/210167625-45149a4c-36eb-47e3-8424-864fc16e0e96.png)

### Test 11: Validasi sebelum harga item diganti
![image](https://user-images.githubusercontent.com/24706517/210167643-5ccfec0a-ba19-4051-91fd-18406ffc4038.png)
![image](https://user-images.githubusercontent.com/24706517/210167653-14a92ad8-fe32-4185-bb45-665c3c0d6b9a.png)

## Kesimpulan
- Super cashier adalah program sederhana yang membantu penjual untuk menjual produknya secara efektif dan efisien.
- Terdapat fitur menambahkan barang, mengedit barang (nama, quantity, harga per item), menghapus barang, dan menjumlahkan keseluruhan harga barang beserta diskonnya secara cepat dan tepat.
- Keseluruhan fitur tersebut dapat memudahkan dan mempercepat pembeli untuk membeli barangnya secara mandiri.

## Future Work
- Membuat GUI (_Graphical User Interface_)
- Membuat sistem pembayaran yang terintegrasi dengan sistem kasir
