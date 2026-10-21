import tkinter as tk

# Inisialisasi jendela utama
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

# List untuk menampung widget input nilai mata pelajaran
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

# Label luaran hasil prediksi
label_hasil = tk.Label(
    root,
    text="",
    font=("Helvetica", 12, "bold"),
    fg="white",
    bg="#253b74"
)
label_hasil.pack(pady=2)

# Tombol hasil prediksi
btn_prediksi = tk.Button(
    root,
    text="Hasil Prediksi",
    font=("Helvetica", 10, "bold"),
    bg="white",
    fg="#253b74",
    padx=15,
    pady=5,
    relief="raised"
)
btn_prediksi.pack(pady=(10, 20))

# Menjalankan aplikasi
root.mainloop()
