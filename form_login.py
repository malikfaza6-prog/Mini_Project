import tkinter as tk
from tkinter import messagebox

data_login = [
    {"username": "admin", "password": "123"},
    {"username": "user", "password": "abc"},
    {"username": "guest", "password": "xyz"}
]


def login():
    nama = entry_nama.get()
    sandi = entry_sandi.get()
    
    ditemukan = False  # flag apakah user ditemukan
    
    # Nested loop: cek setiap dictionary di dalam list data_login
    for akun in data_login:
        for kunci, nilai in akun.items():
            # Loop pertama cek key, tapi kita pakai if untuk username
            if akun["username"] == nama and akun["password"] == sandi:
                ditemukan = True
                break
        if ditemukan:
            break

    # === IF-ELSE ===
    if ditemukan:
        messagebox.showinfo("Login", "Login Berhasil!")
    else:
        messagebox.showerror("Login", "Username atau Password Salah!")
        
# Buat jendela utama
screen = tk.Tk()
screen.title("Form Login")
screen.geometry("450x350")
screen.resizable(False,False)



# 🏷️ Label judul
label_judul = tk.Label(screen, text="Login Here", fg="#5C6BF7", bg="#80A1BA", font=("Arial Black", 20, "bold"))
label_judul.pack(pady=10)
subtitle = tk.Label(screen, text="Members Login Area",bg="#80A1BA" ,fg="#A3485A", font=("Arial", 10,"bold"))
subtitle.pack(pady=(0, 15))

# 🧍 Input Nama
label_nama = tk.Label(screen, text="Username", bg="#80A1BA",fg="#A3485A")
label_nama.pack()
entry_nama = tk.Entry(screen, font=("Arial", 11), width=23, bd=0, highlightthickness=1, highlightcolor="#5C6BF7", relief="solid" )
entry_nama.pack()

# 🔐 Input Sandi
label_sandi = tk.Label(screen, text="Password",bg="#80A1BA",fg="#A3485A")
label_sandi.pack()
entry_sandi = tk.Entry(screen, text="Password", font=("Arial", 11), width=23, bd=0, highlightthickness=1, highlightcolor="#5C6BF7", relief="solid")
entry_sandi.pack(pady=5)


# 🔘 Tombol untuk memproses input
tombol_submit = tk.Button(screen, text="Kirim",fg="white",bg="#9B5DE0", command=login, width = 20, height= 0)
tombol_submit.pack(pady=20)
screen.config(bg="#80A1BA")

screen.mainloop()

