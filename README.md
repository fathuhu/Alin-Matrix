# Matriks Calc 

Kalkulator matriks ini adalah sebuah aplikasi web yang bisa mengeksekusi berbagai operasi matriks seperti penjumlahan, pengurangan, perkalian, transpose, determinan, dan menyelesaikan sistem persamaan linear (SPL) menggunakan metode eliminasi Gauss.

![Matrix Calculator](assets\images\UI-ChooseMatrix.png)

## Fitur
- **Operasi Matriks Dasar:**
  - Penjumlahan Matriks
  - Pengurangan Matriks
  - Perkalian Matriks
  - Pembagian Matriks
  - Transpose Matriks
  - Determinan Matriks
  - OBE (Operasi Baris Elementer) Matriks
  
- **Sistem Persamaan Linear (SPL):**
  - Penyelesaian SPL menggunakan Metode Eliminasi Gauss
  - Penyelesaian SPL menggunakan Metode Gauss-Jordan
  - Deteksi penyelesaian tidak ada jika determinan = 0
  
- **Tampilan Hasil:**
  - Hasil operasi matriks ditampilkan dalam format yang rapi
  - Tampilan `steps` (langkah-langkah) menggunakan scroll untuk mempermudah pembacaan
  - Penanganan pesan kesalahan atau hasil khusus seperti "Tidak ada penyelesaian" jika matriks tidak memenuhi syarat

## Prasyarat
Sebelum menjalankan aplikasi, pastikan Anda telah menginstall:
- **Python 3.6+**
- **Virtual Environment (venv)**

## Installation
Ikuti langkah-langkah berikut untuk menginstall dan menjalankan aplikasi:

```bash
# Clone repository ini
git clone https://github.com/username/matriks-calc.git

# Masuk ke direktori project
cd matriks-calc

# Buat environment virtual
python -m venv venv

# Aktivasi environment virtual
source venv/bin/activate   # Untuk Linux/Mac
venv\Scripts\activate      # Untuk Windows

# Install dependencies
pip install -r requirements.txt
```

## Deployment

To deploy this project run

```bash
  #Jalankan pada server lokal
  python app.py

  #Atau jika menggunakan node.js:
  npm install -g http-server
  http-server

```


## Tech Stack

**HTML5**: Struktur markup untuk halaman aplikasi.

**CSS3**: Styling antarmuka pengguna.

**JavaScript**: Logika utama aplikasi dan perhitungan matriks.

**Python (Flask)**: Backend untuk memproses data matriks dan mengelola routing.

**Node.js**: (Opsional) untuk menjalankan server lokal.

## Contoh Matriks untuk Pengujian
Berikut adalah beberapa contoh matriks yang bisa digunakan untuk menguji berbagai fitur operasi matriks dan SPL di aplikasi ini:

Penjumlahan Matriks 2x2

Matriks A: [[1, 2], [3, 4]]
Matriks B: [[5, 6], [7, 8]]

Pengurangan Matriks 3x3

Matriks A: [[3, 2, 1], [1, 0, -1], [4, 5, 6]]
Matriks B: [[1, -2, 3], [2, 3, 4], [-1, -1, 1]]

SPL Metode Gauss untuk Matriks 3x4:

Matriks: [[2, 1, -1, 8], [-3, -1, 2, -11], [-2, 1, 2, -3]]
Hasil: [x, y, z] = [2, 3, -1]


## Authors

- [@adriannprtm (Adrian Pratama Sasmita - 231524033) ](https://github.com/adriannprtm)
- [@peitann (Ahmad Fatan Haidar - 231524034) ](https://github.com/Peitann)
- [@Fathuhu (Fathan Khairun Normawijaya - 231524044) ](https://github.com/Fathuhu) 
- [@krsXishere  (Krisna Purnama - 231524048) ](https://github.com/krsXishere )