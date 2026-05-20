**HAVIDZ ANDRIAN-23111189-IF-C PAGI**
# SHA-256 Avalanche Effect Checker
Repositori ini berisi program berbasis Python untuk mendemonstrasikan dan membuktikan Avalanche Effect pada algoritma hashing SHA-256. Proyek ini dibuat sebagai bentuk eksperimen kriptografi dasar dan penerapan prinsip eksplorasi NKYC (Never Kill Your Curiosity).

# Apa itu Avalanche Effect?
Dalam kriptografi, Avalanche Effect adalah sifat ideal di mana perubahan sekecil apa pun pada input, misalnya hanya mengubah 1 bit, akan menghasilkan perubahan yang sangat drastis pada output. Pada SHA-256, perubahan ideal berada di kisaran 50% atau sekitar 128 bit dari total 256 bit output hash. Hal ini menunjukkan bahwa algoritma hashing memiliki pola yang sulit diprediksi dan tahan terhadap analisis sederhana.

# Fitur Program
* Konversi otomatis dari teks input dan output hash hexadecimal menjadi representasi biner 256-bit.
* Perhitungan presisi jumlah perbedaan bit (bit difference) antara Input X dan Input Y, serta antara Hash(X) dan Hash(Y).
* Fleksibilitas input melalui mode NKYC, sehingga pengguna dapat menguji input dengan perbedaan 1 bit maupun perbedaan ekstrem secara bebas.
* Interactive CLI berbasis terminal yang sederhana dan mudah digunakan.

# Persyaratan Sistem
Program ini hanya menggunakan modul bawaan Python tanpa library eksternal tambahan.
* Python 3.6 atau versi yang lebih baru.
# Cara Menjalankan Program
1. Clone repositori ke komputer Anda:
```bash
git clone https://github.com/x-kzy/SHA-256-Avalanche-Effect-Checker.git
cd SHA-256-Avalanche-Effect-Checker
```
2. Jalankan program Python:
```bash
python main.py
```
3. Pastikan nama file `main.py` sesuai dengan nama file program Anda apabila berbeda.
4. Pilih opsi 1 pada menu program untuk mulai melakukan eksperimen.
5. Masukkan dua teks sebagai Input X dan Input Y dengan panjang karakter yang sama.

# Contoh Penggunaan dan Output
# 1. Eksperimen Wajib (Perbedaan 1 Bit)
Input:
```text
Input X : b
Input Y : c
```

# 2. Eksperimen Ekstrem NKYC (Perbedaan Puluhan Bit)
Input:
```text
Input X : Siang
Input Y : Malam
```

**# Contoh OUTPUT**
```text
=============================================
        Avalanche Effect SHA-256
=============================================
Pilih salah 1:
1. Mulai Eksperimen
2. Selesai
     Made by Havidz Andrian-231111899
=============================================
Masukkan pilihan (1/2): 1

=== Mulai Eksperimen Avalanche Effect SHA-256 ===
Masukkan X: Havidz23
Masukkan Y: havidz23

=== DATA INPUT ===
X                : 'Havidz23'
Y                : 'havidz23'
Biner X          : 01001000 01100001 01110110 01101001 01100100 01111010 00110010 00110011
Biner Y          : 01101000 01100001 01110110 01101001 01100100 01111010 00110010 00110011
Perbedaan input  : 1 bit

=== HASH SHA-256 ===
h(X) hex         : d893fef2dd8fab42b25950a55ca5733008d057b7fbf1da7005a5bfafed754f6f
h(Y) hex         : 0d1ec4ab4b85d47d8c1c1768fa9f80a30684ad9aeb8841b9c51412859b8a1f76
h(X) biner 256   : 11011000 10010011 11111110 11110010 11011101 10001111 10101011 01000010 10110010 01011001 01010000 10100101 01011100 10100101 01110011 00110000 00001000 11010000 01010111 10110111 11111011 11110001 11011010 01110000 00000101 10100101 10111111 10101111 11101101 01110101 01001111 01101111
h(Y) biner 256   : 00001101 00011110 11000100 10101011 01001011 10000101 11010100 01111101 10001100 00011100 00010111 01101000 11111010 10011111 10000000 10100011 00000110 10000100 10101101 10011010 11101011 10001000 01000001 10111001 11000101 00010100 00010010 10000101 10011011 10001010 00011111 01110110

=== HASIL PERBANDINGAN ===
Jumlah bit beda (jBeda) : 134 bit dari 256 bit
Persentase beda         : 52.34%

=== KESIMPULAN ===
Pada percobaan ini, perubahan 1 bit pada input menghasilkan
134 bit berbeda (52.34%) pada output hash SHA-256.
Hasil ini menunjukkan adanya avalanche effect, karena perubahan
kecil pada input (1 bit) menghasilkan perubahan besar pada output.
Secara teori, nilai ideal avalanche effect pada SHA-256 adalah
sekitar 128 dari 256 bit (50%). Hasil percobaan ini sebesar
134 bit (52.34%) masih berada dalam kisaran yang wajar,
mengingat sifat probabilistik dari fungsi hash.
```
