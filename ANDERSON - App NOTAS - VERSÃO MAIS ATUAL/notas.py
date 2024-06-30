import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from historico import open_historico_window
from estoque import open_estoque_window
import json
import os

notas = []

def carregar_notas():
    global notas
    if os.path.exists("notas.json"):
        with open("notas.json", "r") as file:
            notas = json.load(file)

def salvar_notas():
    with open("notas.json", "w") as file:
        json.dump(notas, file)

def open_notas_window():
    carregar_notas()

    def add_mercadoria():
        nome = entry_nome_mercadoria.get()
        grupo = combo_grupo_mercadoria.get()
        quantidade = entry_quantidade_mercadoria.get()
        if nome and grupo and quantidade:
            mercadorias_listbox.insert(tk.END, f"{nome} - {grupo} - {quantidade} unidades")
            entry_nome_mercadoria.delete(0, tk.END)
            combo_grupo_mercadoria.set('')
            entry_quantidade_mercadoria.delete(0, tk.END)

    def remover_mercadoria():
        selected_items = mercadorias_listbox.curselection()
        if not selected_items:
            messagebox.showerror("Erro", "Selecione uma mercadoria para remover.")
            return
        for index in selected_items[::-1]:  # Remover do final para o início
            mercadorias_listbox.delete(index)

    def cadastrar():
        data = entry_data.get()
        fornecedor = entry_fornecedor.get()
        valor = entry_valor.get()
        parcelas = combo_parcelas.get()
        vencimento = entry_vencimento.get()
        centro_custo = combo_centro_custo.get()
        mercadorias = mercadorias_listbox.get(0, tk.END)
        
        # Verificar se todos os campos foram preenchidos
        if not (data and fornecedor and valor and parcelas and vencimento and centro_custo and mercadorias):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos e adicione pelo menos uma mercadoria.")
            return

        nota = {
            "data": data,
            "fornecedor": fornecedor,
            "valor": valor,
            "parcelas": parcelas,
            "vencimento": vencimento,
            "centro_custo": centro_custo,
            "mercadorias": list(mercadorias)
        }
        notas.append(nota)
        salvar_notas()
        messagebox.showinfo("Cadastro", "Nota cadastrada com sucesso!")

        # Limpar as entradas específicas
        entry_fornecedor.delete(0, tk.END)
        entry_valor.delete(0, tk.END)
        entry_vencimento.delete(0, tk.END)
        mercadorias_listbox.delete(0, tk.END)

    # Criar a janela de cadastro de notas
    notas_window = tk.Tk()
    notas_window.title("Cadastro de Notas")
    notas_window.configure(bg='#0d0d0d')  # Fundo preto
    notas_window.state('zoomed')  # Abrir em tela cheia

    # Estilos
    title_font = ('Comic Sans MS', 24, 'bold')
    label_font = ('Comic Sans MS', 12)
    entry_font = ('Comic Sans MS', 12)
    button_font = ('Comic Sans MS', 12, 'bold')
    button_bg = '#00ffcc'  # Cor neon
    button_fg = '#0d0d0d'  # Preto
    entry_bg = '#1a1a1a'  # Fundo cinza escuro
    entry_fg = '#00ffcc'  # Texto neon
    combo_style = {
        "font": entry_font,
        "background": '#1a1a1a',
        "foreground": '#00ffcc'
    }

    # Frame para centralizar o conteúdo
    container_frame = tk.Frame(notas_window, bg='#0d0d0d')
    container_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

    left_frame = tk.Frame(container_frame, bg='#1a1a1a', padx=20, pady=20, bd=2, relief='solid', highlightbackground='#00ffcc', highlightthickness=2)
    left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    right_frame = tk.Frame(container_frame, bg='#1a1a1a', padx=20, pady=20, bd=2, relief='solid', highlightbackground='#00ffcc', highlightthickness=2)
    right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    container_frame.columnconfigure(0, weight=1)
    container_frame.columnconfigure(1, weight=1)
    container_frame.rowconfigure(0, weight=1)

    # Labels e Entradas para o cadastro de notas no left_frame
    label_data = tk.Label(left_frame, text="Data de Entrada:", font=label_font, bg='#1a1a1a', fg='#00ffcc')
    label_data.grid(row=0, column=0, pady=(10, 0), padx=5, sticky='w')
    entry_data = DateEntry(left_frame, font=entry_font, bd=2, relief='solid', highlightbackground='#00ffcc', highlightthickness=2, date_pattern='dd/mm/yyyy', locale='pt_BR')
    entry_data.grid(row=0, column=1, pady=(10, 0), padx=5, ipadx=10, ipady=5)

    label_fornecedor = tk.Label(left_frame, text="Fornecedor:", font=label_font, bg='#1a1a1a', fg='#00ffcc')
    label_fornecedor.grid(row=1, column=0, pady=(10, 0), padx=5, sticky='w')
    entry_fornecedor = tk.Entry(left_frame, font=entry_font, bd=2, relief='solid', bg=entry_bg, fg=entry_fg, highlightbackground='#00ffcc', highlightthickness=2, insertbackground='#00ffcc')
    entry_fornecedor.grid(row=1, column=1, pady=(10, 0), padx=5, ipadx=10, ipady=5)

    label_valor = tk.Label(left_frame, text="Valor em R$:", font=label_font, bg='#1a1a1a', fg='#00ffcc')
    label_valor.grid(row=2, column=0, pady=(10, 0), padx=5, sticky='w')
    entry_valor = tk.Entry(left_frame, font=entry_font, bd=2, relief='solid', bg=entry_bg, fg=entry_fg, highlightbackground='#00ffcc', highlightthickness=2, insertbackground='#00ffcc')
    entry_valor.grid(row=2, column=1, pady=(10, 0), padx=5, ipadx=10, ipady=5)

    label_parcelas = tk.Label(left_frame, text="Quantidade de Parcelas:", font=label_font, bg='#1a1a1a', fg='#00ffcc')
    label_parcelas.grid(row=3, column=0, pady=(10, 0), padx=5, sticky='w')
    parcelas_options = ["à vista"] + [f"{i}x" for i in range(2, 13)]
    combo_parcelas = ttk.Combobox(left_frame, values=parcelas_options, font=entry_font, state="readonly")
    combo_parcelas.grid(row=3, column=1, pady=(10, 0), padx=5, ipadx=10, ipady=5)
    combo_parcelas.configure(**combo_style)

    label_vencimento = tk.Label(left_frame, text="Data de Vencimento:", font=label_font, bg='#1a1a1a', fg='#00ffcc')
    label_vencimento.grid(row=4, column=0, pady=(10, 0), padx=5, sticky='w')
    entry_vencimento = tk.Entry(left_frame, font=entry_font, bd=2, relief='solid', bg=entry_bg, fg=entry_fg, highlightbackground='#00ffcc', highlightthickness=2, insertbackground='#00ffcc')
    entry_vencimento.grid(row=4, column=1, pady=(10, 0), padx=5, ipadx=10, ipady=5)

    label_centro_custo = tk.Label(left_frame, text="Centro de Custo:", font=label_font, bg='#1a1a1a', fg='#00ffcc')
    label_centro_custo.grid(row=5, column=0, pady=(10, 0), padx=5, sticky='w')
    centro_custo_options = ["Cozinha", "Bar", "Salão", "Manutenção", "Limpeza", "Serviços Gerais", "Outros"]
    combo_centro_custo = ttk.Combobox(left_frame, values=centro_custo_options, font=entry_font, state="readonly")
    combo_centro_custo.grid(row=5, column=1, pady=(10, 0), padx=5, ipadx=10, ipady=5)
    combo_centro_custo.configure(**combo_style)

    # Mercadorias no right_frame
    label_mercadorias = tk.Label(right_frame, text="Mercadorias:", font=label_font, bg='#1a1a1a', fg='#00ffcc')
    label_mercadorias.grid(row=0, column=0, columnspan=2, pady=(10, 0), padx=5, sticky='w')

    label_nome_mercadoria = tk.Label(right_frame, text="Nome:", font=label_font, bg='#1a1a1a', fg='#00ffcc')
    label_nome_mercadoria.grid(row=1, column=0, pady=(10, 0), padx=5, sticky='w')
    entry_nome_mercadoria = tk.Entry(right_frame, font=entry_font, bd=2, relief='solid', bg=entry_bg, fg=entry_fg, highlightbackground='#00ffcc', highlightthickness=2, insertbackground='#00ffcc')
    entry_nome_mercadoria.grid(row=1, column=1, pady=(10, 0), padx=5, ipadx=10, ipady=5)

    label_grupo_mercadoria = tk.Label(right_frame, text="Grupo:", font=label_font, bg='#1a1a1a', fg='#00ffcc')
    label_grupo_mercadoria.grid(row=2, column=0, pady=(10, 0), padx=5, sticky='w')
    grupo_options = ["Alimentos", "Bebidas", "Limpeza", "Utensílios", "Outros"]
    combo_grupo_mercadoria = ttk.Combobox(right_frame, values=grupo_options, font=entry_font, state="readonly")
    combo_grupo_mercadoria.grid(row=2, column=1, pady=(10, 0), padx=5, ipadx=10, ipady=5)
    combo_grupo_mercadoria.configure(**combo_style)

    label_quantidade_mercadoria = tk.Label(right_frame, text="Quantidade:", font=label_font, bg='#1a1a1a', fg='#00ffcc')
    label_quantidade_mercadoria.grid(row=3, column=0, pady=(10, 0), padx=5, sticky='w')
    entry_quantidade_mercadoria = tk.Entry(right_frame, font=entry_font, bd=2, relief='solid', bg=entry_bg, fg=entry_fg, highlightbackground='#00ffcc', highlightthickness=2, insertbackground='#00ffcc')
    entry_quantidade_mercadoria.grid(row=3, column=1, pady=(10, 0), padx=5, ipadx=10, ipady=5)

    button_add_mercadoria = tk.Button(right_frame, text="Adicionar Mercadoria", font=button_font, bg=button_bg, fg=button_fg, command=add_mercadoria, bd=2, relief='solid', highlightbackground='#00ffcc', highlightthickness=2, activebackground='#00b38f', activeforeground='#0d0d0d')
    button_add_mercadoria.grid(row=4, column=0, columnspan=2, pady=(10, 0), padx=5, ipadx=10, ipady=5)

    button_remove_mercadoria = tk.Button(right_frame, text="Remover Mercadoria", font=button_font, bg='red', fg='white', command=remover_mercadoria, bd=2, relief='solid', highlightbackground='#00ffcc', highlightthickness=2, activebackground='#ff6666', activeforeground='#0d0d0d')
    button_remove_mercadoria.grid(row=5, column=0, columnspan=2, pady=(10, 0), padx=5, ipadx=10, ipady=5)

    mercadorias_listbox = tk.Listbox(right_frame, font=entry_font, bd=2, relief='solid', bg=entry_bg, fg=entry_fg, highlightbackground='#00ffcc', highlightthickness=2)
    mercadorias_listbox.grid(row=6, column=0, columnspan=2, pady=(10, 0), padx=5, ipadx=10, ipady=5, sticky='nsew')

    right_frame.rowconfigure(6, weight=1)

    # Botões de Cadastro, Histórico e Estoque
    button_frame = tk.Frame(container_frame, bg='#0d0d0d')
    button_frame.grid(row=1, column=0, columnspan=2, pady=(10, 20), padx=5)

    button_cadastrar = tk.Button(button_frame, text="Cadastrar", font=button_font, bg=button_bg, fg=button_fg, command=cadastrar, bd=2, relief='solid', highlightbackground='#00ffcc', highlightthickness=2, activebackground='#00b38f', activeforeground='#0d0d0d')
    button_cadastrar.grid(row=0, column=0, pady=(10, 20), padx=10, ipadx=10, ipady=5)

    button_historico = tk.Button(button_frame, text="Histórico", font=button_font, bg=button_bg, fg=button_fg, bd=2, relief='solid', highlightbackground='#00ffcc', highlightthickness=2, command=lambda: open_historico_window(notas), activebackground='#00b38f', activeforeground='#0d0d0d')
    button_historico.grid(row=0, column=1, pady=(10, 20), padx=10, ipadx=10, ipady=5)

    button_estoque = tk.Button(button_frame, text="Estoque", font=button_font, bg=button_bg, fg=button_fg, bd=2, relief='solid', highlightbackground='#00ffcc', highlightthickness=2, command=open_estoque_window, activebackground='#00b38f', activeforeground='#0d0d0d')
    button_estoque.grid(row=0, column=2, pady=(10, 20), padx=10, ipadx=10, ipady=5)

    # Rodar a aplicação de cadastro de notas
    notas_window.mainloop()


