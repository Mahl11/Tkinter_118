import tkinter as tk
from tkinter import messagebox

# Inisialisasi jendela utama aplikasi
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("450x620")
root.configure(bg="#253b74")
root.resizable(False, False)

# Label Judul Aplikasi
label_judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Helvetica", 16, "bold"),
    fg="white",
    bg="#253b74"
)
label_judul.pack(pady=(25, 15))

# Frame untuk form input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#253b74")
frame_input.pack(pady=5)

# List untuk menampung widget Entry nilai mata pelajaran
entries = []

for i in range(1, 11):
    label = tk.Label(
        frame_input,
        text=f"Nilai Mata Pelajaran {i}:",
        font=("Helvetica", 10),
        fg="white",
        bg="#253b74",
        anchor="w"
    )
    label.grid(row=i-1, column=0, padx=15, pady=3, sticky="w")
    
    entry = tk.Entry(frame_input, width=20, font=("Helvetica", 10))
    entry.grid(row=i-1, column=1, padx=15, pady=3)
    entries.append(entry)

# Label teks pilihan jurusan
label_jurusan_info = tk.Label(
    root,
    text="Pilihan Jurusan Anda:",
    font=("Helvetica", 11, "bold"),
    fg="white",
    bg="#253b74"
)
label_jurusan_info.pack(pady=(15, 3))

# Label luaran hasil prediksi prodi
label_hasil = tk.Label(
    root,
    text="",
    font=("Helvetica", 12, "bold"),
    fg="white",
    bg="#253b74"
)
label_hasil.pack(pady=2)

# Fungsi prediksi prodi pilihan dengan validasi nilai
def prediksi_prodi():
    for i, entry in enumerate(entries, start=1):
        nilai = entry.get().strip()
        if not nilai:
            messagebox.showwarning("Peringatan", f"Nilai Mata Pelajaran {i} belum diisi!")
            return
        try:
            val = float(nilai)
            if val < 0 or val > 100:
                messagebox.showwarning("Peringatan", f"Nilai Mata Pelajaran {i} harus berada di antara 0 - 100!")
                return
        except ValueError:
            messagebox.showwarning("Peringatan", f"Nilai Mata Pelajaran {i} harus berupa angka!")
            return
            
    # Menampilkan hasil prodi pilihan sesuai ketentuan praktikum
    label_hasil.config(text="Teknologi Informasi")

# Tombol hasil prediksi
btn_prediksi = tk.Button(
    root,
    text="Hasil Prediksi",
    font=("Helvetica", 10, "bold"),
    bg="white",
    fg="#253b74",
    padx=15,
    pady=5,
    relief="raised",
    command=prediksi_prodi
)
btn_prediksi.pack(pady=(10, 20))

# Menjalankan event loop utama aplikasi
root.mainloop()
