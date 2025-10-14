import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import timedelta
import io, base64

def regresi_emas(csv_path, days_ahead=7):
    # 1. Load dataset dengan delimiter ';'
    df = pd.read_csv(csv_path, delimiter=';')

    # 2. Bersihkan nama kolom (hilangkan spasi dan ubah jadi lowercase)
    df.columns = [col.strip().lower().replace(' ', '') for col in df.columns]

    # 3. Ubah kolom harga jadi numerik
    # contoh "1.129.000,00" → "1129000.00"
    df['harga'] = df['harga'].astype(str)
    df['harga'] = df['harga'].str.replace('.', '', regex=False)   # hapus titik pemisah ribuan
    df['harga'] = df['harga'].str.replace(',', '.', regex=False)  # ubah koma jadi titik
    df['harga'] = df['harga'].astype(float)

    # 4. Ubah tanggal jadi datetime dan hitung hari ke-n
    df['tanggal'] = pd.to_datetime(df['tanggal'], format='%d/%m/%Y')
    df['hari_ke'] = (df['tanggal'] - df['tanggal'].min()).dt.days

    # 5. Siapkan X dan y
    X = df[['hari_ke']].values.reshape(-1, 1)
    y = df['harga'].values

    # 6. Buat model regresi linear
    model = LinearRegression()
    model.fit(X, y)

    # 7. Prediksi ke depan
    last_day = df['hari_ke'].max()
    future_days = np.arange(last_day + 1, last_day + days_ahead + 1).reshape(-1, 1)
    y_pred_future = model.predict(future_days)

    # 8. Buat dataframe hasil prediksi
    future_dates = [df['tanggal'].max() + timedelta(days=i) for i in range(1, days_ahead + 1)]
    df_future = pd.DataFrame({'tanggal': future_dates, 'harga_prediksi': y_pred_future})

    # 8b. Ambil 5 harga tertinggi dari data asli periode 2024-205
    df['tahun'] = df['tanggal'].dt.year
    df_top5 = df[df['tahun'].isin([2024, 2025])].nlargest(5,'harga')[['tanggal','harga']]
    df_top5['tanggal'] = pd.to_datetime(df_top5['tanggal'], errors='coerce')

    # 9. Visualisasi hasilnya
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(df['tanggal'].values, df['harga'].values, label='Data Aktual')
    ax.plot(df_future['tanggal'].values, df_future['harga_prediksi'].values, '--', label='Prediksi 7 Hari')
    ax.set_title('Prediksi Harga Emas')
    ax.set_xlabel('Tanggal')
    ax.set_ylabel('Harga (Rupiah)')
    ax.legend()

    # Simpan gambar ke base64 agar bisa ditampilkan di Flask nanti
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    encoded = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)

    # Visualisasi Top 5 Harga Tertinggi
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    ax2.plot(df['tanggal'].values, df['harga'].values, label='Data Aktual')
    ax2.scatter(df_top5['tanggal'].values, df_top5['harga'].values, color='red', s=60,  label='Top 5 Harga Tertinggi')
    ax2.set_title('Top 5 Harga Tertinggi Emas 2024-2025')
    ax2.set_xlabel('Tanggal')
    ax2.set_ylabel('Harga (Rupiah)')
    ax2.legend()

    # Simpan Grafik Kedua
    buf2 = io.BytesIO()
    plt.savefig(buf2, format='png')
    buf2.seek(0)
    encode_top5 = base64.b64encode(buf2.read()).decode('utf-8')
    plt.close(fig2)

    # Hitung rata-rata harga prediksi 
    avg_prediksi = df_future['harga_prediksi'].mean()

    # 10. Return hasil
    return {
        "koefisien": model.coef_[0],
        "intercept": model.intercept_,
        "prediksi": df_future.to_dict(orient='records'),
        "top5": df_top5.to_dict(orient='records'),
        "plot": encoded,
        "plot_top5": encode_top5,
        "avg_prediksi": avg_prediksi
    }
