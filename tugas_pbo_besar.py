import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from ttkthemes import ThemedTk
from PIL import Image, ImageTk

class PemesananTiketApp:
    def __init__(self):
        # Membuat koneksi dan tabel jika belum ada
        self.create_table()
        self.create_ticket_table()

        # Membuat GUI
        self.app = ThemedTk(theme="equilux")
        self.app.title("Aplikasi Pemesanan Tiket Penerbangan")

        # Frame untuk registrasi
        self.register_frame = ttk.Frame(self.app)

        self.reg_username_var = tk.StringVar()
        self.reg_password_var = tk.StringVar()

        ttk.Label(self.register_frame, text="Registrasi", font=('Helvetica', 16)).grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(self.register_frame, text="Username:").grid(row=1, column=0, padx=10, pady=5)
        ttk.Entry(self.register_frame, textvariable=self.reg_username_var).grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self.register_frame, text="Password:").grid(row=2, column=0, padx=10, pady=5)
        ttk.Entry(self.register_frame, textvariable=self.reg_password_var, show="*").grid(row=2, column=1, padx=10, pady=5)

        ttk.Button(self.register_frame, text="Register", command=self.register_user).grid(row=3, column=0, columnspan=2, pady=10)

        # Frame untuk login
        self.login_frame = ttk.Frame(self.app)

        self.login_username_var = tk.StringVar()
        self.login_password_var = tk.StringVar()

        ttk.Label(self.login_frame, text="Login", font=('Helvetica', 16)).grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(self.login_frame, text="Username:").grid(row=1, column=0, padx=10, pady=5)
        ttk.Entry(self.login_frame, textvariable=self.login_username_var).grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self.login_frame, text="Password:").grid(row=2, column=0, padx=10, pady=5)
        ttk.Entry(self.login_frame, textvariable=self.login_password_var, show="*").grid(row=2, column=1, padx=10, pady=5)

        ttk.Button(self.login_frame, text="Login", command=self.login_user).grid(row=3, column=0, columnspan=2, pady=10)

        # Frame utama
        self.main_frame = CustomFrame(self.app)

        # Variabel untuk menyimpan input dari user
        self.maskapai_var = tk.StringVar()
        self.jumlah_penumpang_var = tk.StringVar()
        self.tanggal_var = tk.StringVar()
        self.tujuan_var = tk.StringVar()
        self.nama_var = tk.StringVar()

        # Label dan Entry untuk input
        ttk.Label(self.main_frame, text="Pemesanan Tiket", font=('Helvetica', 16)).grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(self.main_frame, text="Maskapai:").grid(row=1, column=0, padx=10, pady=5)
        ttk.Entry(self.main_frame, textvariable=self.maskapai_var).grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self.main_frame, text="Jumlah Penumpang:").grid(row=2, column=0, padx=10, pady=5)
        ttk.Entry(self.main_frame, textvariable=self.jumlah_penumpang_var).grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self.main_frame, text="Tanggal Keberangkatan:").grid(row=3, column=0, padx=10, pady=5)
        ttk.Entry(self.main_frame, textvariable=self.tanggal_var).grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(self.main_frame, text="Tujuan:").grid(row=4, column=0, padx=10, pady=5)
        ttk.Entry(self.main_frame, textvariable=self.tujuan_var).grid(row=4, column=1, padx=10, pady=5)

        ttk.Label(self.main_frame, text="Nama Pemesan:").grid(row=5, column=0, padx=10, pady=5)
        ttk.Entry(self.main_frame, textvariable=self.nama_var).grid(row=5, column=1, padx=10, pady=5)

        # Button Submit
        ttk.Button(self.main_frame, text="Submit", command=self.submit_pesanan).grid(row=6, column=0, columnspan=2, pady=10)

        # Button Tampilkan Pesanan
        ttk.Button(self.main_frame, text="Tampilkan Pesanan", command=self.tampilkan_pesanan).grid(row=7, column=0, columnspan=2, pady=10)

        # Logout
        ttk.Button(self.main_frame, text="Logout", command=self.logout).grid(row=8, column=0, columnspan=2, pady=10)

        # Button untuk kembali ke frame utama dari frame registrasi atau login
        ttk.Button(self.register_frame, text="sudah punya akun?", command=self.show_login_frame).grid(row=4, column=0, columnspan=2, pady=10)
        ttk.Button(self.login_frame, text="belum punya akun?", command=self.show_register_frame).grid(row=4, column=0, columnspan=2, pady=10)

        # Menampilkan frame registrasi saat aplikasi dimulai
        self.register_frame.pack()

        # Variabel untuk menyimpan informasi pengguna yang saat ini login
        self.current_user = None

        # Menjalankan GUI
        self.app.mainloop()

    def create_connection(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pemesanan_tiket"
        )

    def create_table(self):
        connection = self.create_connection()
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) UNIQUE,
                password VARCHAR(255)
            )
        """)
        connection.commit()
        connection.close()

    def register(self, username, password):
        connection = self.create_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        connection.commit()
        connection.close()

    def login(self, username, password):
        connection = self.create_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        connection.close()
        return user

    def logout(self):
        self.current_user = None
        self.main_frame.pack_forget()
        self.show_login_frame()

    def create_ticket_table(self):
        connection = self.create_connection()
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pesanan (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                maskapai VARCHAR(255),
                jumlah_penumpang INT,
                tanggal_keberangkatan DATE,
                tujuan VARCHAR(255),
                nama_pemesan VARCHAR(255),
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        connection.commit()
        connection.close()

    def tambah_pesanan(self):
        if not self.current_user:
            messagebox.showerror("Error", "Silakan login terlebih dahulu.")
            return

        maskapai = self.maskapai_var.get()
        jumlah_penumpang = self.jumlah_penumpang_var.get()
        tanggal_keberangkatan = self.tanggal_var.get()
        tujuan = self.tujuan_var.get()
        nama_pemesan = self.nama_var.get()

        connection = self.create_connection()  # Menggunakan koneksi yang telah dibuat
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO pesanan (user_id, maskapai, jumlah_penumpang, tanggal_keberangkatan, tujuan, nama_pemesan)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (self.current_user[0], maskapai, jumlah_penumpang, tanggal_keberangkatan, tujuan, nama_pemesan))
        connection.commit()
        connection.close()

        messagebox.showinfo("Sukses", "Pesanan berhasil dimasukkan ke database.")

    def tampilkan_pesanan(self):
        if not self.current_user:
            messagebox.showerror("Error", "Silakan login terlebih dahulu.")
            return

        connection = self.create_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM pesanan WHERE user_id = %s", (self.current_user[0],))
        pesanan = cursor.fetchall()
        connection.close()

        if not pesanan:
            messagebox.showinfo("Tidak Ada Pesanan", "Belum ada pesanan yang dimasukkan.")
        else:
            detail_pesanan = "\n".join([f"ID: {row[0]}, Maskapai: {row[2]}, Jumlah Penumpang: {row[3]}, Tanggal Keberangkatan: {row[4]}, Tujuan: {row[5]}, Nama Pemesan: {row[6]}" for row in pesanan])
            messagebox.showinfo("Detail Pesanan", detail_pesanan)

    def register_user(self):
        username = self.reg_username_var.get()
        password = self.reg_password_var.get()

        if not username or not password:
            messagebox.showerror("Error", "Username dan password harus diisi.")
            return

        self.create_table()  # Pastikan tabel users sudah ada
        self.register(username, password)
        messagebox.showinfo("Registrasi Berhasil", "Registrasi berhasil. Silakan login.")

    def login_user(self):
        username = self.login_username_var.get()
        password = self.login_password_var.get()

        if not username or not password:
            messagebox.showerror("Error", "Username dan password harus diisi.")
            return

        user = self.login(username, password)

        if user:
            self.current_user = user
            messagebox.showinfo("Login Berhasil", "Login berhasil.")
            self.login_frame.pack_forget()
            self.main_frame.pack()
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah.")

    def submit_pesanan(self):
        self.tambah_pesanan()

    def show_login_frame(self):
        self.main_frame.pack_forget()
        self.register_frame.pack_forget()
        self.login_frame.pack()

    def show_register_frame(self):
        self.main_frame.pack_forget()
        self.login_frame.pack_forget()
        self.register_frame.pack()


class CustomFrame(ttk.Frame):
    def pack_forget(self):
        print("Custom Frame's pack_forget method")
        super().pack_forget()


# Menjalankan aplikasi
app = PemesananTiketApp()
