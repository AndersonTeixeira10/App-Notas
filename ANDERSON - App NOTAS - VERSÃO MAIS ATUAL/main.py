import tkinter as tk
from tkinter import messagebox, font
from notas import open_notas_window
from historico import open_historico_window

# Função para verificar o login
def login(root):
    username = entry_username.get()
    password = entry_password.get()

    # Lógica de autenticação
    if (username == "anderson" and password == "windows13") or (username == "admin@10" and password == "costelaria@10"):
        messagebox.showinfo("Login", "Login bem-sucedido!")
        # Após o login, abrir a janela de cadastro de notas
        root.destroy()
        open_notas_window()
    else:
        messagebox.showerror("Login", "Credenciais inválidas")

# Criar a janela de login
root = tk.Tk()
root.title("App Controle de Estoque")
root.configure(bg='#0d0d0d')  # Fundo preto
root.state('zoomed')  # Abrir em tela cheia

# Estilos
title_font = ('Comic Sans MS', 24, 'bold')
label_font = ('Comic Sans MS', 12)
entry_font = ('Comic Sans MS', 12)
button_font = ('Comic Sans MS', 12, 'bold')
button_bg = '#00ffcc'  # Cor neon
button_fg = '#0d0d0d'  # Preto
entry_bg = '#1a1a1a'  # Fundo cinza escuro
entry_fg = '#00ffcc'  # Texto neon

# Título
title_label = tk.Label(root, text="App Controle de Estoque", font=title_font, bg='#0d0d0d', fg='#00ffcc')
title_label.pack(pady=(20, 10))

# Frame para centralizar o conteúdo
login_frame = tk.Frame(root, bg='#1a1a1a', padx=20, pady=20, bd=2, relief='solid', highlightbackground='#00ffcc', highlightthickness=2, highlightcolor='#00ffcc')
login_frame.pack(pady=(0, 20))

# Labels e Entradas para usuário e senha
label_username = tk.Label(login_frame, text="Usuário:", font=label_font, bg='#1a1a1a', fg='#00ffcc')
label_username.pack(pady=(10, 0))
entry_username = tk.Entry(login_frame, font=entry_font, bg=entry_bg, fg=entry_fg, bd=2, relief='solid', highlightbackground='#00ffcc', highlightthickness=2, insertbackground='#00ffcc')
entry_username.pack(pady=(0, 10), ipadx=10, ipady=5)

label_password = tk.Label(login_frame, text="Senha:", font=label_font, bg='#1a1a1a', fg='#00ffcc')
label_password.pack(pady=(10, 0))
entry_password = tk.Entry(login_frame, show="*", font=entry_font, bg=entry_bg, fg=entry_fg, bd=2, relief='solid', highlightbackground='#00ffcc', highlightthickness=2, insertbackground='#00ffcc')
entry_password.pack(pady=(0, 10), ipadx=10, ipady=5)

# Botão de Login
button_login = tk.Button(login_frame, text="Login", font=button_font, bg=button_bg, fg=button_fg, command=lambda: login(root), bd=2, relief='solid', highlightbackground='#00ffcc', highlightthickness=2, activebackground='#00b38f', activeforeground='#0d0d0d')
button_login.pack(pady=(10, 20), ipadx=10, ipady=5)

# Marcação com texto e formatação especial
watermark_frame = tk.Frame(root, bg='#0d0d0d')
watermark_frame.pack(side=tk.BOTTOM, fill=tk.X)

label_watermark = tk.Label(watermark_frame, text="Desenvolvido por Anderson Teixeira", font=label_font, bg='#0d0d0d', fg='#00ffcc')
label_watermark.pack()

# Rodar a aplicação
root.mainloop()
