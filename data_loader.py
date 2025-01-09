import yfinance as yf
import pandas as pd
import datetime
import os


def download_currency_data(symbol="USDTRY=X"):
    # Bugünün tarihini alıyoruz
    today = datetime.date.today()

    # Bugünden iki yıl öncesine kadar olan tarih
    two_years_ago = today - datetime.timedelta(days=2 * 365)  # 2 yıl = 730 gün

    # Veriyi yfinance ile indiriyoruz
    data = yf.download(symbol, start=two_years_ago, end=today)

    # Veriyi düzenliyoruz
    data.reset_index(inplace=True)
    data = data[['Date', 'Close']]  # Tarih ve kapanış fiyatı
    data.columns = ['Date', 'Exchange_Rate']

    # Proje dizinini al
    project_dir = os.path.dirname(os.path.abspath(__file__))

    # Data klasörünün tam yolunu oluştur
    data_dir = os.path.join(project_dir, 'data')

    # Eğer 'data' klasörü yoksa, oluştur
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Veriyi 'data' klasörüne kaydet
    data.to_csv(os.path.join(data_dir, 'raw_data.csv'), index=False)

    print("Veri başarıyla indirildi ve kaydedildi.")
    return data


if __name__ == "__main__":
    download_currency_data()  # Fonksiyonu çalıştırıyoruz
