import hashlib
def text_to_bytes(text):
    return text.encode("utf-8")

def bytes_to_binary(data):
    return ''.join(f'{byte:08b}' for byte in data)

def format_binary_groups(binary_string, group_size=8):
    return ' '.join(
        binary_string[i:i + group_size]
        for i in range(0, len(binary_string), group_size)
    )

def sha256_hex(text):
    return hashlib.sha256(text_to_bytes(text)).hexdigest()

def sha256_binary(text):
    digest = hashlib.sha256(text_to_bytes(text)).digest()
    return ''.join(f'{byte:08b}' for byte in digest)

def count_input_bit_difference(x, y):
    x_bytes = text_to_bytes(x)
    y_bytes = text_to_bytes(y)

    if len(x_bytes) != len(y_bytes):
        raise ValueError(
            "X dan Y harus memiliki panjang karakter/byte yang sama untuk pengujian ini.")

    total_diff = 0
    for bx, by in zip(x_bytes, y_bytes):
        total_diff += (bx ^ by).bit_count()
    return total_diff

def count_hash_bit_difference(bin_a, bin_b):
    if len(bin_a) != len(bin_b):
        raise ValueError("Panjang biner hash harus sama.")

    jBeda = 0
    for i in range(len(bin_a)):
        if bin_a[i] != bin_b[i]:
            jBeda += 1
    return jBeda

def tampilkan_header():
    print(" ")
    print("=" * 45)
    print("        Avalanche Effect SHA-256 (NKYC)")
    print("=" * 45)
    print("Pilih salah 1:")
    print("1. Mulai Eksperimen")
    print("2. Selesai")
    print("     Made by Havidz Andrian-231111899")
    print("=" * 45)

def tampilkan_menu_ulang():
    print("\nPilih salah 1:")
    print("1. Hitung lagi")
    print("2. Selesai")

def jalankan_eksperimen():
    print("\n=== Mulai Eksperimen Avalanche Effect SHA-256 ===")

    x = input("Masukkan X: ")
    y = input("Masukkan Y: ")

    try:
        beda_input = count_input_bit_difference(x, y)
    except ValueError as e:
        print(f"\nError: {e}")
        return

    # Validasi agar minimal ada perbedaan input
    if beda_input == 0:
        print("\nInput X dan Y sama persis. Masukkan teks yang ada perbedaannya.")
        return

    hash_x_hex = sha256_hex(x)
    hash_y_hex = sha256_hex(y)
    hash_x_bin = sha256_binary(x)
    hash_y_bin = sha256_binary(y)

    jBeda = count_hash_bit_difference(hash_x_bin, hash_y_bin)
    persentase = (jBeda / 256) * 100

    print("\n=== DATA INPUT ===")
    print(f"X                : {repr(x)}")
    print(f"Y                : {repr(y)}")
    print(f"Biner X          : {format_binary_groups(bytes_to_binary(text_to_bytes(x)))}")
    print(f"Biner Y          : {format_binary_groups(bytes_to_binary(text_to_bytes(y)))}")
    print(f"Perbedaan input  : {beda_input} bit")

    print("\n=== HASH SHA-256 ===")
    print(f"h(X) hex         : {hash_x_hex}")
    print(f"h(Y) hex         : {hash_y_hex}")
    print(f"h(X) biner 256   : {format_binary_groups(hash_x_bin)}")
    print(f"h(Y) biner 256   : {format_binary_groups(hash_y_bin)}")

    print("\n=== HASIL PERBANDINGAN ===")
    print(f"Jumlah bit beda (jBeda) : {jBeda} bit dari 256 bit")
    print(f"Persentase beda         : {persentase:.2f}%")

    # KESIMPULAN HASIL (Dibuat dinamis untuk NKYC)
    print("\n=== KESIMPULAN ===")
    print(f"Pada percobaan ini, perubahan {beda_input} bit pada input menghasilkan")
    print(f"{jBeda} bit berbeda ({persentase:.2f}%) pada output hash SHA-256.")
    
    if beda_input == 1:
        print(f"Hasil ini menunjukkan adanya avalanche effect, karena perubahan")
        print(f"kecil pada input (1 bit) menghasilkan perubahan besar pada output.")
    else:
        print(f"Hasil ini membuktikan sifat acak SHA-256. Walaupun input diubah")
        print(f"secara ekstrem ({beda_input} bit), tingkat kekacauan output tetap konsisten.")
        
    print(f"Secara teori, nilai ideal avalanche effect pada SHA-256 adalah")
    print(f"sekitar 128 dari 256 bit (50%). Hasil percobaan ini sebesar")
    print(f"{jBeda} bit ({persentase:.2f}%) masih berada dalam kisaran yang wajar,")
    print(f"mengingat sifat probabilistik dari fungsi hash.")

def main():
    while True:
        tampilkan_header()
        pilihan_awal = input("Masukkan pilihan (1/2): ")

        if pilihan_awal == "1":
            while True:
                jalankan_eksperimen()
                tampilkan_menu_ulang()
                pilihan_lagi = input("Masukkan pilihan (1/2): ")

                if pilihan_lagi == "1":
                    continue
                elif pilihan_lagi == "2":
                    print("\nTerimakasih telah menggunakan program ini :)")
                    return
                else:
                    print("\nPilihan tidak valid. Silakan pilih 1 atau 2.")

        elif pilihan_awal == "2":
            print("\nTerimakasih telah menggunakan program ini :)")
            break
        else:
            print("\nPilihan tidak valid. Silakan pilih 1 atau 2.\n")

if __name__ == "__main__":
    main()
