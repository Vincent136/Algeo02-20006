# Smol Image
  Smol image adalah website yang dapat digunakan untuk kompresi file gambar jpg dan png dengan bantuan algoritma SVD. Program ini dibuat untuk memenuhi salah satu tugas pada mata kuliah IF2123 Aljabar Linier dan Geometri yaitu aplikasi nilai eigen dan vektor eigen dalam kompresi gambar.

## Penjelasan Singkat mengenai Algoritma SVD
Algoritma SVD didasarkan pada teorema dalam aljabar
linier yang menyatakan bahwa sebuah matriks dua dimensi dapat dipecah menjadi hasil
perkalian dari 3 sub-matriks yaitu matriks ortogonal U, matriks diagonal S, dan transpose
dari matriks ortogonal V. Dekomposisi matriks ini dapat dinyatakan sesuai persamaan
berikut.

![image](https://user-images.githubusercontent.com/74034061/141672391-2b07fac3-1589-4b5d-a660-9a35d34ed193.png)

Matriks U adalah matriks yang kolomnya terdiri dari vektor eigen ortonormal dari matriks
AA<sup>T</sup>
. Matriks ini menyimpan informasi yang penting terkait baris-baris matriks awal, dengan
informasi terpenting disimpan di dalam kolom pertama. Matriks S adalah matriks diagonal
yang berisi akar dari nilai eigen matriks U atau V yang terurut menurun. Matriks V adalah
matriks yang kolomnya terdiri dari vektor eigen ortonormal dari matriks A<sup>T</sup>A. Matriks ini
menyimpan informasi yang penting terkait kolom-kolom matriks awal, dengan informasi
terpenting disimpan dalam baris pertama.

![image](https://user-images.githubusercontent.com/74034061/141672615-f9121fa1-d49f-4c87-8d9e-19e59fa77da8.png)

Dilihat dari gambar di atas, dapat direkonstruksi gambar dengan banyak _singular
values_ k dengan mengambil kolom dan baris sebanyak k dari U dan V serta _singular value_
sebanyak k dari S atau Σ terurut dari yang terbesar. Kita dapat mengaproksimasi suatu
gambar yang mirip dengan gambar aslinya dengan mengambil k yang jauh lebih kecil dari
jumlah total singular value karena kebanyakan informasi disimpan di _singular values_ awal
karena _singular values_ terurut mengecil. Nilai k juga berkaitan dengan rank matriks karena
banyaknya _singular value_ yang diambil dalam matriks S adalah rank dari matriks hasil, jadi
dalam kata lain k juga merupakan rank dari matriks hasil. Maka itu matriks hasil rekonstruksi
dari SVD akan berupa informasi dari gambar yang terkompresi dengan ukuran yang lebih
kecil dibanding gambar awal.

## Library
Program ini dibuat dengan bahasa pemrograman Python dan menggunakan HTML untuk tampilan frontend website.
Library yang digunakan sebagai berikut
1. Flask  (2.0.2) -> Untuk pembuatan _web application_
2. imageio (2.10.1) -> Untuk mengubah gambar menjadi array
3. numpy (1.21.3) -> Untuk mengolah array dan matriks
4. Pillow (8.4.0) -> Untuk merekonstruksi array menjadi gambar
5. Werkzeug (1.0.1) -> Untuk menghasilkan filename yang secure
6. Bootstrap 5 -> Framework CSS

## Cara Menggunakan Program
1. jalankan perintah ```flask run``` pada terminal
2. copy link yang muncul ke browser atau tekan ctrl+ click jika menggunakan vscode
3. upload foto yang ingin dikompres
4. masukkan tingkat kompresi yang diinginkan 
5. hasil kompresi gambar akan ditampilkan pada website dan dapat di unggah

## Fitur 
Website ini dapat mengkompres file gambar jpg dan png. Gambar yang diterima dapat berupa gambar _full color_, _grayscale_, maupun gambar png dengan _background_ transparan.

## Referensi
1. https://informatika.stei.itb.ac.id/~rinaldi.munir/AljabarGeometri/2020-2021/Algeo-18-Nilai-Eigen-dan-Vektor-Eigen-Bagian1.pdf
2. http://www.math.utah.edu/~goller/F15_M2270/BradyMathews_SVDImage.pdf
3. https://youtu.be/I9BBGulrOmo
4. https://ristohinno.medium.com/qr-decomposition-903e8c61eaab
  
