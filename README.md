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

Hasil yang diharapkan:
* Output hash mengalami perubahan besar di kisaran ±128 bit atau sekitar 50%.
# 2. Eksperimen Ekstrem NKYC (Perbedaan Puluhan Bit)
Input:
```text
Input X : Siang
Input Y : Malam
```
Walaupun input berubah secara drastis, hasil hash tetap menunjukkan distribusi perubahan yang stabil di sekitar 50%, bukan berubah total menjadi 100%.

# Contoh Tampilan CLI
```text
=== DATA INPUT ===
X                : 'b'
Y                : 'c'
Biner X          : 01100010
Biner Y          : 01100011
Perbedaan input  : 1 bit

=== HASH SHA-256 ===
... (Tampilan biner 256 bit) ...

=== HASIL PERBANDINGAN ===
Jumlah bit beda (jBeda) : 133 bit dari 256 bit
Persentase beda         : 51.95%

=== KESIMPULAN ===
Pada percobaan ini, perubahan 1 bit pada input menghasilkan
133 bit berbeda (51.95%) pada output hash SHA-256.
Hasil tersebut menunjukkan bahwa algoritma SHA-256 memiliki
Avalanche Effect yang sangat baik, karena perubahan kecil pada
input menghasilkan perubahan besar dan acak pada output hash.
```
