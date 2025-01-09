import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from data_loader import download_currency_data
from train_model import train_model
from predict import predict_future
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Veri indirme fonksiyonu
def download_data():
    try:
        messagebox.showinfo("Başarılı", "Veriler indirilmeye başlandı...")

        # Veriyi indir
        data = download_currency_data()

        # Son 10 günü al
        last_10_days = data.tail(10)

        # Ekranda son 10 günü göstermek için Text widget'ını kullanabiliriz
        display_text = "Son 10 Gün:\n"
        for index, row in last_10_days.iterrows():
            display_text += f"Tarih: {row['Date'].strftime('%Y-%m-%d')}, Kapanış: {row['Exchange_Rate']:.4f}\n"

        # Text widget'ında göster
        result_text.delete(1.0, tk.END)  # Önceki verileri temizle
        result_text.insert(tk.END, display_text)  # Son 10 günün verilerini ekle

        # Grafik gösterimi
        plot_data(data)  # Son 2 yıl verisini çiz

    except Exception as e:
        messagebox.showerror("Hata", f"Veri indirilirken bir hata oluştu: {str(e)}")

# Model eğitme fonksiyonu
def train_model_function():
    try:
        messagebox.showinfo("Başarılı", "Model eğitilmeye başlandı...")
        train_model()
    except Exception as e:
        messagebox.showerror("Hata", f"Model eğitilirken bir hata oluştu: {str(e)}")

# Tahmin fonksiyonu
def make_prediction():
    try:
        messagebox.showinfo("Başarılı", "Tahmin yapılmaya başlandı...")
        prediction = predict_future()
        result_label.config(text=f"Tahmin edilen döviz kuru: {prediction:.4f} TRY")
    except Exception as e:
        messagebox.showerror("Hata", f"Tahmin yapılırken bir hata oluştu: {str(e)}")

# Grafik oluşturma fonksiyonu
def plot_data(data):
    # Veriyi çiz
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(data['Date'], data['Exchange_Rate'], marker='o', color='#4CAF50', label="Kapanış Fiyatı")

    ax.set_title("Son 2 Yıl Döviz Kuru", fontsize=14, color="#333333")
    ax.set_xlabel("Tarih", fontsize=12)
    ax.set_ylabel("Döviz Kuru (TRY)", fontsize=12)
    ax.legend()
    ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

    # Tkinter widget'ına ekle
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=20)

# Tkinter GUI tasarımı
root = tk.Tk()
root.title("Döviz Kuru Tahmin Uygulaması")
root.geometry("700x700")
root.configure(bg="#f9f9f9")

# Başlık
title_label = tk.Label(root, text="Döviz Kuru Tahmin Uygulaması", font=("Arial", 16, "bold"), bg="#f9f9f9", fg="#333333")
title_label.pack(pady=20)

# Veri İndir Butonu
download_button = tk.Button(root, text="Veri İndir", command=download_data, font=("Arial", 12), bg="#5bc0de", fg="white", relief="flat", padx=10, pady=5)
download_button.pack(pady=10)

# Model Eğit Butonu
train_button = tk.Button(root, text="Modeli Eğit", command=train_model_function, font=("Arial", 12), bg="#5cb85c", fg="white", relief="flat", padx=10, pady=5)
train_button.pack(pady=10)

# Tahmin Yap Butonu
predict_button = tk.Button(root, text="Tahmin Yap", command=make_prediction, font=("Arial", 12), bg="#f0ad4e", fg="white", relief="flat", padx=10, pady=5)
predict_button.pack(pady=10)

# Tahmin Sonuçları
result_label = tk.Label(root, text="Tahmin sonucu burada görünecek.", font=("Arial", 12), bg="#f9f9f9", fg="#555555")
result_label.pack(pady=20)

# Son 10 Gün Verilerini Gösterme
result_text = tk.Text(root, height=10, width=60, font=("Arial", 10), bg="#ffffff", fg="#333333", relief="solid", borderwidth=1)
result_text.pack(pady=10)

# Uygulamayı çalıştır
root.mainloop()
