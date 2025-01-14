import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menentukan zodiak
def get_zodiac(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries", "Memiliki Sifat Pemimpin, Berani, Penuh Semangat"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus", "Memiliki Sifat Setia, Stabil, Praktis"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini", "Memiliki Sifat Sosial, Komunikatif, Adaptif"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer", "Memiliki Sifat Sensitif, Perhatian, Penyayang"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo", "Memiliki Sifat Percaya diri, Ramah, Kreatif"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo", "Memiliki Sifat Teliti, Perfeksionis, Analitis"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra", "Memiliki Sifat Harmonis, Adil, Sosial"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio", "Memiliki Sifat Intens, Penuh gairah, Setia"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius", "Memiliki Sifat Petualang, Optimis, Suka kebebasan"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn", "Memiliki Sifat Ambisius, Bertanggung jawab, Disiplin"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius", "Memiliki Sifat Inovatif, Idealis, Suka kebebasan"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces", "Memiliki Sifat Empatik, Artistik, Sensitif"
    else:
        return None, "Tanggal atau bulan tidak valid."

# Fungsi untuk menangani aksi klik tombol
def check_zodiac():
    try:
        day = int(entry_day.get())  # Mengambil input dari user untuk tanggal
        month = int(entry_month.get())  # Mengambil input dari user untuk bulan
        
        # Validasi input tanggal dan bulan
        if not (1 <= month <= 12) or not (1 <= day <= 31):
            messagebox.showerror("Input Error", "Tanggal atau Bulan Tidak Valid! Coba Lagi Oke.")
            return
        
        zodiac = get_zodiac(day, month)
        
        if zodiac:
            messagebox.showinfo("Hasil Zodiak", f"Zodiak Kamu adalah: {zodiac[0]}\nKarakteristik: {zodiac[1]}")
        else:
            messagebox.showerror("Input Error", "Tanggal lahir tidak valid!")
        
        # Reset input setelah cek
        entry_day.delete(0, tk.END)
        entry_month.delete(0, tk.END)
    
    except ValueError:
        messagebox.showerror("Input Error", "Harap masukkan angka yang valid!")

# Fungsi untuk mereset aplikasi ke tampilan awal
def reset():
    entry_day.delete(0, tk.END)  # Menghapus input tanggal
    entry_month.delete(0, tk.END)  # Menghapus input bulan

# Membuat jendela aplikasi
window = tk.Tk()
window.title("Game Menebak Zodiak Berdasarkan Tanggal Lahir")

# Label untuk Tanggal dan Bulan
label_day = tk.Label(window, text="Masukkan Tanggal Lahir (1-31):", font=("Comic Sans MS", 12))
label_day.grid(row=0, column=0, padx=10, pady=10)

label_month = tk.Label(window, text="Masukkan Bulan Lahir (1-12):", font=("Comic Sans MS", 12))
label_month.grid(row=1, column=0, padx=10, pady=10)

# Entry untuk Tanggal dan Bulan
entry_day = tk.Entry(window, font=("Comic Sans MS", 12), width=10)
entry_day.grid(row=0, column=1, padx=10, pady=10)

entry_month = tk.Entry(window, font=("Comic Sans MS", 12), width=10)
entry_month.grid(row=1, column=1, padx=10, pady=10)

# Tombol untuk Mengecek Zodiak
button_check = tk.Button(window, text="Cek Zodiak", font=("Comic Sans MS", 12), command=check_zodiac)
button_check.grid(row=2, column=0, columnspan=2, pady=10)

# Tombol untuk Reset aplikasi
button_reset = tk.Button(window, text="Reset", font=("Comic Sans MS", 12), command=reset)
button_reset.grid(row=3, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
window.mainloop()
