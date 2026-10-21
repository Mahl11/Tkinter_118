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

# Frame untuk form input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#253b74")
frame_input.pack(pady=5)

# Input Nilai Mata Pelajaran 1 dan 2
label_mp1 = tk.Label(frame_input, text="Nilai Mata Pelajaran 1:", font=("Helvetica", 10), fg="white", bg="#253b74")
label_mp1.grid(row=0, column=0, padx=10, pady=4, sticky="w")
entry_mp1 = tk.Entry(frame_input, width=20)
entry_mp1.grid(row=0, column=1, padx=10, pady=4)

label_mp2 = tk.Label(frame_input, text="Nilai Mata Pelajaran 2:", font=("Helvetica", 10), fg="white", bg="#253b74")
label_mp2.grid(row=1, column=0, padx=10, pady=4, sticky="w")
entry_mp2 = tk.Entry(frame_input, width=20)
entry_mp2.grid(row=1, column=1, padx=10, pady=4)

# Menjalankan aplikasi
root.mainloop()
