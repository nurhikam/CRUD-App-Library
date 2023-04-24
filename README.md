# Library Book's App

## Problem yang akan diselesaikan
Di sebuah perpustakaan nasional di daerah Jakarta, setiap harinya memiliki banyak pengunjung. Perputakaan tersebut memiliki banyak buku dan terkadang hal itu membuat para pengunjung kesulitan untuk mengetahui apakah buku yang sedang dicari tersedia di perpustakaan tersebut.  

## Solusi yang dibuat
Untuk menyelesaikan problem tersebut, maka dibuatlah sebuah aplikasi pencarian buku yang dapat digunakan oleh pelanggan di perpustakaan tersebut.
Fitur yang tersedia yaitu "search" yang memudahkan pengguna untuk mencari sebuah buku berdasarkan nama buku, tahun penerbitan, penulis buku, atau nomor ISBN. 
Selain itu, pelanggan perpustakaan juga dapat memberikan review (dalam range bintang 1 sampai bintang 5) terhadap sebuah buku dan penulis buku.

## Konsep / flowchart aplikasi
![CRUD APP FLOW drawio (1)](https://user-images.githubusercontent.com/92198564/173189474-f0c6336c-37a9-4e19-a0b2-a55f1191071b.png)

## Panduan menggunakan aplikasi
Cara menggunakan aplikasi ini yang pertama tentu saja membuka aplikasi tersebut. berikutnya pembaca dapat mencari sebuah judul buku, penulis, isbn buku, ataupun tahun terbit dari sebuah buku. setelah melakukan pencarian nantinya aplikasi ini akan menampilkan data yang sesuai dengan yang sebelumnya dicari. apabila buku yang dicari tidak ada dalam data, maka tampilan dari aplikasi ini akan kosong. sedangkan apabila ditemukan data yang sama antara buku yang dicari dengan data yang ada pada aplikasi ini. aplikasi ini akan langsung menampilkannya secara otomatis. data yang ditampilkan antara lain isbn, judul buku, penulis, tahun terbit, dan juga rating yang sudah masuk

setelah kita menemukan buku yang dicari, nantinya akan tersedia juga sebuah kolom untuk pembaca memberikan rating pada buku buku tersebut. rating yang diberikan antara 1 sampai 5. nantinya apabila rating itu sudah masuk akan langsung dieksekusi untuk memperbarui tabel rating dari buku tersebut.

## Demo atau screenshot aplikasi yang dibuat
### Menu utama aplikasi
![image](https://user-images.githubusercontent.com/92198564/173195347-1a86eede-47d6-4e26-876e-15a0eff45deb.png)
### Mencari Buku berdasarkan ISBN
![image](https://user-images.githubusercontent.com/92198564/173195332-8fa32756-aaa9-422f-bd2a-375e18fdc6a9.png)
### Mencari Buku berdasarkan Judul Buku
![image](https://user-images.githubusercontent.com/92198564/173195365-369adf83-2060-4335-855b-5c7c50b14cf8.png)
### Mencari Buku berdasarkan Nama Penulis
![image](https://user-images.githubusercontent.com/92198564/173195383-03a23e5c-5d87-4f3b-9ab7-fba530a24cfe.png)
### Mencari Buku berdasarkan Tahun Terbit
![image](https://user-images.githubusercontent.com/92198564/173195416-0ed4790d-823a-40ad-867b-b8e4e8e49e46.png)
### Ketika Buku yang dicari tidak tersedia
![image](https://user-images.githubusercontent.com/92198564/173195441-ef889e7c-3f4a-4df3-ba0a-0cb9b2a64556.png)
### Memilih Buku yang untuk diberikan Rating (Klik 2x pada Buku)
![image](https://user-images.githubusercontent.com/92198564/173195479-240618ff-f2ac-4c22-b2b1-65324b52c169.png)
### Ketika akan memberi rating pada buku
![image](https://user-images.githubusercontent.com/92198564/173195499-6cfdacac-f2cc-4e7a-8157-228aa3c8f0d4.png)
### Clear All (Membersihkan semua input dan output) 
![image](https://user-images.githubusercontent.com/92198564/173195649-cbaeb154-8a51-4122-b5d8-8ab48a686758.png)


## Referensi/Acknowledgement
https://react.rocks/tag/CRUD

https://www.kaggle.com/datasets/dylanjcastillo/7k-books-with-metadata

https://realpython.com/python-gui-tkinter/

https://www.datacamp.com/tutorial/gui-tkinter-python
