# utilities/csv_loader.py
"""
CSV loader utilities for Matriks project.

Fitur:
- membaca CSV dengan delimiter ';' (fallback autodetect jika diperlukan)
- membersihkan kolom harga berformat lokal (contoh: "1.129.000,00")
- mengubah kolom tanggal ke datetime
- helper untuk menyiapkan X (fitur) dan y (target) untuk regresi linear

Fungsi utama:
- load_csv(path_or_file, sep=';')
- clean_price_series(series)
- prepare_regression(df, date_col='tanggal', price_col='harga')

path_or_file bisa berupa path string atau file-like object (mis. werkzeug FileStorage dari Flask).
"""

from typing import Tuple, Union
import pandas as pd
import numpy as np
from io import StringIO

def load_csv(path_or_file: Union[str, 'file'], sep: str = ';', encoding: str = 'utf-8') -> pd.DataFrame:
    """
    Load CSV into pandas DataFrame.
    - default separator ';' (sesuai dataset kamu).
    - menerima path string atau file-like (mis. upload Flask).

    Returns DataFrame dengan kolom sudah strip() dan lowercase.
    """
    # read_csv dapat menerima path atau file-like
    try:
        df = pd.read_csv(path_or_file, sep=sep, encoding=encoding)
    except Exception as e:
        # fallback: coba read dengan pandas autodetect separator (commonly , or ;)
        try:
            df = pd.read_csv(path_or_file, encoding=encoding)
        except Exception as e2:
            raise RuntimeError(f"gagal membaca csv: {e}; fallback error: {e2}")

    # bersihkan nama kolom
    df.columns = [c.strip().lower() for c in df.columns]
    return df

def clean_price_series(series: pd.Series) -> pd.Series:
    """
    Convert price-like strings (e.g. "1.129.000,00" or "1129000,00") to float.
    - Menghapus titik sebagai pemisah ribuan
    - Mengganti koma decimal menjadi titik
    - Mengembalikan pd.Series dtype float
    """
    s = series.astype(str).str.strip()
    # Hapus tanda non-digit kecuali ',' atau '.'
    # Karena format lokal biasanya '.' ribuan dan ',' desimal, kita lakukan:
    # 1) hapus titik (ribuan)
    # 2) ganti koma -> titik (desimal)
    s = s.str.replace('.', '', regex=False)   # hapus titik ribuan
    s = s.str.replace(',', '.', regex=False)  # ubah desimal
    # Hapus karakter non-digit/decimal (safety)
    s = s.str.replace(r'[^0-9\.]', '', regex=True)
    # Convert ke float
    return pd.to_numeric(s, errors='coerce')

def prepare_regression(df: pd.DataFrame,
                       date_col: str = 'tanggal',
                       price_col: str = 'harga') -> Tuple[pd.DataFrame, np.ndarray, np.ndarray]:
    """
    Siapkan data untuk regresi:
    - Pastikan kolom tanggal jadi datetime
    - Harga dibersihkan jadi numeric
    - Tambahkan kolom 'hari_ke' (0..N-1) sebagai fitur numerik
    Returns: (df_clean, X, y)
      - df_clean: dataframe yang sudah terproses (tanggal, harga, hari_ke)
      - X: numpy array shape (n_samples, 1) berisi hari_ke
      - y: numpy array shape (n_samples,) berisi harga (float)
    """
    if date_col not in df.columns:
        raise KeyError(f"kolom tanggal tidak ditemukan: {date_col}")

    if price_col not in df.columns:
        raise KeyError(f"kolom harga tidak ditemukan: {price_col}")

    # Parse tanggal
    # Coba format umum dd/mm/YYYY dulu; jika gagal, fallback parse otomatis
    try:
        df[date_col] = pd.to_datetime(df[date_col], format='%d/%m/%Y')
    except Exception:
        df[date_col] = pd.to_datetime(df[date_col], dayfirst=True, errors='coerce')

    # Bersihkan harga
    df[price_col] = clean_price_series(df[price_col])

    # Hilangkan baris yang gagal parsing
    df = df.dropna(subset=[date_col, price_col]).copy()

    # Urutkan berdasarkan tanggal (penting)
    df = df.sort_values(by=date_col).reset_index(drop=True)

    # hitung hari_ke (0 = tanggal pertama)
    df['hari_ke'] = (df[date_col] - df[date_col].min()).dt.days.astype(int)

    X = df[['hari_ke']].values
    y = df[price_col].values

    return df, X, y

# Convenience function: load + prepare
def load_and_prepare(path_or_file: Union[str, 'file'],
                     sep: str = ';',
                     date_col: str = 'tanggal',
                     price_col: str = 'harga') -> Tuple[pd.DataFrame, np.ndarray, np.ndarray]:
    """
    Kombinasi load_csv + prepare_regression.
    Gunakan untuk langsung mendapat (df_clean, X, y).
    """
    df = load_csv(path_or_file, sep=sep)
    return prepare_regression(df, date_col=date_col, price_col=price_col)


# Jika ingin testing cepat pada modul ini
if __name__ == '__main__':
    # tes lokal file bernama datasetemas.csv di folder yang sama
    import sys
    sample_path = sys.argv[1] if len(sys.argv) > 1 else 'datasetemas.csv'
    print("Mencoba load:", sample_path)
    df, X, y = load_and_prepare(sample_path)
    print("Baris dataset:", len(df))
    print(df.head())
