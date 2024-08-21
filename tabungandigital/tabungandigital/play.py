import tkinter as tk
from tkinter import ttk,messagebox
import csv
import pandas as pd

class TabunganDigital:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabungan")

        self.tabungan = []

        # Fungsi dibawah ini untuk membuat tabel untuk menampilkan Tabungan
        columns = ("Tanggal","Hari","Uang")
        self.tree = ttk.Treeview(root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(padx=10, pady=10)

        # untuk tempat menginputkan data
        tanggal_label = tk.Label(root, text="Tanggal/Bulan/Tahun:")
        tanggal_label.pack()
        self.tanggal_entry = tk.Entry(root)
        self.tanggal_entry.pack()

        hari_label = tk.Label(root, text="Hari:")
        hari_label.pack()
        self.hari_entry = tk.Entry(root)
        self.hari_entry.pack()

        uang_label = tk.Label(root, text="Uang:")
        uang_label.pack()
        self.uang_entry = tk.Entry(root)
        self.uang_entry.pack()

       
        # Button untuk menambah seluruh data yang telah diinputkan
        add_button = tk.Button(root, text="Submit", command=self.add_tabungan)
        add_button.pack(pady=10)

        save_button = tk.Button(root, text="Simpan ke CSV", command=self.save_to_csv)
        save_button.pack(pady=10)

        calculate_button = tk.Button(root, text="Jumlah Tabungan", command=self.jumlah_tabungan)
        calculate_button.pack(pady=10)

        # Load data dari CSV
        self.load_tabungan()

    def load_tabungan(self):
        try:
            with open("tabungan.csv", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.tree.insert("", "end", values=(row["Tanggal"], row["Hari"], row["Uang"]))
                    self.tabungan.append(row)
        except FileNotFoundError:
            # untuk mengantisipasi jika file tidak ditemukan
            pass
   

    def add_tabungan(self):
        # untuk Mendapatkan nilai dari data yang sudah diinputkan
        tanggal = self.tanggal_entry.get()
        hari = self.hari_entry.get()
        uang = self.uang_entry.get()
        
        # untuk menyimpan data diCSV
        self.tabungan.append({"Tanggal": tanggal, "Hari": hari, "Uang": uang })

        # Menambahkan data pengeluaran ke Treeview
        self.tree.insert("", "end", values=(tanggal, hari, uang))

        # untuk mengosongkan input data setelah ditambahkan
        self.tanggal_entry.delete(0, tk.END)
        self.uang_entry.delete(0, tk.END)
        self.hari_entry.delete(0, tk.END)

    def save_to_csv(self):
    # Membuat DataFrame dari data tabungan
        df = pd.DataFrame(self.tabungan)

    # Menyimpan DataFrame ke dalam file CSV tanpa menyertakan indeks
        df.to_csv("tabungan.csv", index=False)
        print("Data berhasil disimpan ke tabungan.csv")

    def jumlah_tabungan(self):
            try:
                # Membaca data dari file CSV menggunakan pandas
                df = pd.read_csv("tabungan.csv")

                # Menghitung total data pada kolom "Uang"
                total = df["Uang"].sum()

                # Menampilkan hasil penjumlahan
                messagebox.showinfo("Total Uang",f"Total Uang: {total}")

            except FileNotFoundError:
                print("File tabungan.csv tidak ditemukan.")
            except KeyError:
                print("Kolom Uang tidak ditemukan dalam file CSV.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TabunganDigital(root)
    root.mainloop()

