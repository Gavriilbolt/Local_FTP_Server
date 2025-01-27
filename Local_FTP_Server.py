import tkinter as tk
from tkinter import filedialog, messagebox
import socket
import subprocess
import threading
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "Не удалось определить IP"
    finally:
        s.close()
    return ip


def configure_firewall():
    try:
        subprocess.run(["netsh", "advfirewall", "firewall", "add", "rule", "name=FTP Server", "dir=in", "action=allow",
                        "protocol=TCP", "localport=21"], check=True)
        messagebox.showinfo("Успех", "Брандмауэр настроен для порта 21")
    except subprocess.CalledProcessError:
        messagebox.showerror("Ошибка", "Не удалось настроить брандмауэр")


def start_stop_server():
    global server, server_thread
    if server is None:
        server_thread = threading.Thread(target=start_ftp_server, daemon=True)
        server_thread.start()
        root.after(1000, update_status)
        start_stop_btn.config(text="Остановить FTP сервер")
    else:
        stop_ftp_server()
        start_stop_btn.config(text="Запустить FTP сервер")


def start_ftp_server():
    global server
    auth_type = auth_var.get()
    folder = directory.get()
    if not folder:
        messagebox.showwarning("Предупреждение", "Выберите директорию для расшаривания")
        return

    authorizer = DummyAuthorizer()
    if auth_type == "anonymous":
        authorizer.add_anonymous(folder)
    else:
        authorizer.add_user(username.get(), password.get(), folder, perm="elradfmw")

    handler = FTPHandler
    handler.authorizer = authorizer
    server = FTPServer((get_local_ip(), 21), handler)
    server.serve_forever()


def stop_ftp_server():
    global server
    if server:
        server.close_all()
        server = None
        server_status.set("Сервер остановлен")


def update_status():
    if server:
        server_status.set(f"Сервер запущен: ftp://{get_local_ip()}")
    else:
        server_status.set("Сервер остановлен")


def browse_folder():
    folder_selected = filedialog.askdirectory()
    directory.set(folder_selected)


# Интерфейс приложения
root = tk.Tk()
root.title("FTP Server Setup")
root.geometry("400x400")

directory = tk.StringVar()
auth_var = tk.StringVar(value="anonymous")
username = tk.StringVar()
password = tk.StringVar()
server_status = tk.StringVar(value="Сервер не запущен")
server = None
server_thread = None

tk.Label(root, text="Выберите директорию для расшаривания:").pack(pady=5)
tk.Entry(root, textvariable=directory, width=40).pack()
tk.Button(root, text="Обзор").pack(pady=5)

tk.Label(root, text=f"Ваш локальный IP: {get_local_ip()}").pack(pady=5)

tk.Label(root, text="Тип авторизации:").pack()
tk.Radiobutton(root, text="Анонимный доступ", variable=auth_var, value="anonymous").pack()
tk.Radiobutton(root, text="Логин/пароль", variable=auth_var, value="user").pack()

tk.Label(root, text="Логин:").pack()
tk.Entry(root, textvariable=username).pack()
tk.Label(root, text="Пароль:").pack()
tk.Entry(root, textvariable=password, show="*").pack()

tk.Button(root, text="Настроить брандмауэр", command=configure_firewall).pack(pady=5)
start_stop_btn = tk.Button(root, text="Запустить FTP сервер", command=start_stop_server)
start_stop_btn.pack(pady=5)

tk.Label(root, textvariable=server_status, fg="blue").pack(pady=5)

tk.Button(root, text="Выход", command=root.quit).pack(pady=5)

root.mainloop()
