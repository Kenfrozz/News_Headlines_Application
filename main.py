import requests
import tkinter as tk
from tkinter import Scrollbar, Listbox


def get_news():
    api_key = 'e5a74c6675444585bea37eca44b62156'
    url = f'https://newsapi.org/v2/top-headlines?country=tr&apiKey={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        articles = response.json()['articles']
        news_listbox.delete(0, tk.END)
        for i, article in enumerate(articles, 1):
            news_listbox.insert(tk.END, f"{i}. Haber: {article['title']}")
    else:
        news_listbox.delete(0, tk.END)
        news_listbox.insert(tk.END, 'Haberler yüklenirken bir hata oluştu.')


# Tkinter penceresini oluştur
window = tk.Tk()
window.title("Haber Başlıkları")

# Haberleri göstermek için bir liste kutusu ve kaydırma çubuğu oluştur
frame = tk.Frame(window)
frame.pack(pady=10)

scrollbar = Scrollbar(frame, orient=tk.VERTICAL)
news_listbox = Listbox(frame, width=150, height=20, yscrollcommand=scrollbar.set)
scrollbar.config(command=news_listbox.yview)

news_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# "Haberleri Getir" düğmesi
get_news_button = tk.Button(window, text="Haberleri Getir", command=get_news)
get_news_button.pack()

# Pencere boyutunu otomatik olarak ayarla
window.update_idletasks()
window_width = window.winfo_reqwidth()
window_height = window.winfo_reqheight()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

window.geometry(f"+{int(x)}+{int(y)}")

# Pencereyi başlat
window.mainloop()
