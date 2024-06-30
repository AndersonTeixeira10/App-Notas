import tkinter as tk

def open_estoque_window():
    # Criar a janela de estoque
    estoque_window = tk.Tk()
    estoque_window.title("Estoque")
    estoque_window.configure(bg='#0d0d0d')  # Fundo preto

    # Estilos
    title_font = ('Comic Sans MS', 24, 'bold')
    label_font = ('Comic Sans MS', 12)
    entry_font = ('Comic Sans MS', 12)
    button_font = ('Comic Sans MS', 12, 'bold')
    button_bg = '#00ffcc'  # Cor neon
    button_fg = '#0d0d0d'  # Preto

    # Frame para centralizar o conteúdo
    container_frame = tk.Frame(estoque_window, bg='#0d0d0d', padx=20, pady=20, bd=2, relief='solid', highlightbackground='#00ffcc', highlightthickness=2)
    container_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

    # Título
    title_label = tk.Label(container_frame, text="Estoque", font=title_font, bg='#0d0d0d', fg='#00ffcc')
    title_label.pack(pady=(10, 20))

    # Listbox para exibir o estoque
    estoque_listbox = tk.Listbox(container_frame, font=entry_font, bd=2, relief='solid', bg='#1a1a1a', fg='#00ffcc', highlightbackground='#00ffcc', highlightthickness=2)
    estoque_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Botão para fechar o estoque
    button_fechar = tk.Button(container_frame, text="Fechar", font=button_font, bg=button_bg, fg=button_fg, bd=2, relief='solid', highlightbackground='#00ffcc', highlightthickness=2, command=estoque_window.destroy)
    button_fechar.pack(pady=10, ipadx=10, ipady=5)

    # Rodar a aplicação de estoque
    estoque_window.mainloop()
