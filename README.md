# CRUD-App-Project

## Data Anggota Tim
1. Nurhikam
2. Mizanulkhair
3. Fauzan 

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
![image](https://user-images.githubusercontent.com/92198564/173189726-8bab2718-d0ab-4f85-8d1a-6b2ca5b74368.png)
### Mencari Buku berdasarkan ISBN
![image](https://user-images.githubusercontent.com/92198564/173189778-809169cd-1a9b-494b-9578-65f03ed0aeab.png)
### Mencari Buku berdasarkan Judul Buku
![image](https://user-images.githubusercontent.com/92198564/173189839-3f8c2036-4c2b-4210-b03b-8ca327d2197f.png)
### Mencari Buku berdasarkan Nama Penulis
![image](https://user-images.githubusercontent.com/92198564/173189897-c341fc57-fb3f-40d5-acb5-92076d67d358.png)
### Mencari Buku berdasarkan Tahun Terbit
![image](https://user-images.githubusercontent.com/92198564/173189941-fcb20a97-acde-4fae-bf0d-f775909b99b2.png)
### Ketika Buku yang dicari tidak tersedia
![image](https://user-images.githubusercontent.com/92198564/173189987-ea54af82-125e-4e39-8c21-251c1bf8f946.png)
### Memilih Buku yang untuk diberikan Rating (Klik 2x pada Buku)
![image](https://user-images.githubusercontent.com/92198564/173190096-7a506e5b-55e3-42d6-80e3-cfb693c745cd.png)


## Referensi/Acknowledgement
https://react.rocks/tag/CRUD
https://www.kaggle.com/datasets/dylanjcastillo/7k-books-with-metadata

