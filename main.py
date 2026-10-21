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

# Input Nilai Mata Pelajaran 1 sampai 10
label_mp1 = tk.Label(frame_input, text="Nilai Mata Pelajaran 1:", font=("Helvetica", 10), fg="white", bg="#253b74")
label_mp1.grid(row=0, column=0, padx=10, pady=4, sticky="w")
entry_mp1 = tk.Entry(frame_input, width=20)
entry_mp1.grid(row=0, column=1, padx=10, pady=4)

label_mp2 = tk.Label(frame_input, text="Nilai Mata Pelajaran 2:", font=("Helvetica", 10), fg="white", bg="#253b74")
label_mp2.grid(row=1, column=0, padx=10, pady=4, sticky="w")
entry_mp2 = tk.Entry(frame_input, width=20)
entry_mp2.grid(row=1, column=1, padx=10, pady=4)

label_mp3 = tk.Label(frame_input, text="Nilai Mata Pelajaran 3:", font=("Helvetica", 10), fg="white", bg="#253b74")
label_mp3.grid(row=2, column=0, padx=10, pady=4, sticky="w")
entry_mp3 = tk.Entry(frame_input, width=20)
entry_mp3.grid(row=2, column=1, padx=10, pady=4)

label_mp4 = tk.Label(frame_input, text="Nilai Mata Pelajaran 4:", font=("Helvetica", 10), fg="white", bg="#253b74")
label_mp4.grid(row=3, column=0, padx=10, pady=4, sticky="w")
entry_mp4 = tk.Entry(frame_input, width=20)
entry_mp4.grid(row=3, column=1, padx=10, pady=4)

label_mp5 = tk.Label(frame_input, text="Nilai Mata Pelajaran 5:", font=("Helvetica", 10), fg="white", bg="#253b74")
label_mp5.grid(row=4, column=0, padx=10, pady=4, sticky="w")
entry_mp5 = tk.Entry(frame_input, width=20)
entry_mp5.grid(row=4, column=1, padx=10, pady=4)

label_mp6 = tk.Label(frame_input, text="Nilai Mata Pelajaran 6:", font=("Helvetica", 10), fg="white", bg="#253b74")
label_mp6.grid(row=5, column=0, padx=10, pady=4, sticky="w")
entry_mp6 = tk.Entry(frame_input, width=20)
entry_mp6.grid(row=5, column=1, padx=10, pady=4)

label_mp7 = tk.Label(frame_input, text="Nilai Mata Pelajaran 7:", font=("Helvetica", 10), fg="white", bg="#253b74")
label_mp7.grid(row=6, column=0, padx=10, pady=4, sticky="w")
entry_mp7 = tk.Entry(frame_input, width=20)
entry_mp7.grid(row=6, column=1, padx=10, pady=4)

label_mp8 = tk.Label(frame_input, text="Nilai Mata Pelajaran 8:", font=("Helvetica", 10), fg="white", bg="#253b74")
label_mp8.grid(row=7, column=0, padx=10, pady=4, sticky="w")
entry_mp8 = tk.Entry(frame_input, width=20)
entry_mp8.grid(row=7, column=1, padx=10, pady=4)

label_mp9 = tk.Label(frame_input, text="Nilai Mata Pelajaran 9:", font=("Helvetica", 10), fg="white", bg="#253b74")
label_mp9.grid(row=8, column=0, padx=10, pady=4, sticky="w")
entry_mp9 = tk.Entry(frame_input, width=20)
entry_mp9.grid(row=8, column=1, padx=10, pady=4)

label_mp10 = tk.Label(frame_input, text="Nilai Mata Pelajaran 10:", font=("Helvetica", 10), fg="white", bg="#253b74")
label_mp10.grid(row=9, column=0, padx=10, pady=4, sticky="w")
entry_mp10 = tk.Entry(frame_input, width=20)
entry_mp10.grid(row=9, column=1, padx=10, pady=4)

# Menjalankan aplikasi
root.mainloop()
