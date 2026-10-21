import tkinter as tk

# Inisialisasi jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("450x620")
root.configure(bg="#253b74")

# Label Judul Aplikasi
label_judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Helvetica", 16, "bold"),
    fg="white",
    bg="#253b74"
)
label_judul.pack(pady=(25, 20))

# Menjalankan aplikasi
root.mainloop()
