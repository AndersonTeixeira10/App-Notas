import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import pandas as pd
from datetime import datetime

def carregar_notas():
    if os.path.exists("notas.json"):
        with open("notas.json", "r") as file:
            return json.load(file)
    return []

def salvar_notas(notas):
    with open("notas.json", "w") as file:
        json.dump(notas, file)

def open_historico_window(notas):
    def filtrar_notas():
        filtro_data = entry_filtro_data.get()
        filtro_fornecedor = entry_filtro_fornecedor.get()
        filtro_valor = entry_filtro_valor.get()
        filtro_parcelas = combo_filtro_parcelas.get()
        filtro_vencimento = entry_filtro_vencimento.get()
        filtro_centro_custo = combo_filtro_centro_custo.get()

        # Limpar a Treeview
        for item in tree.get_children():
            tree.delete(item)

        # Adicionar as notas filtradas à Treeview
        for nota in reversed(notas):
            if (filtro_data in nota["data"] and
                filtro_fornecedor.lower() in nota["fornecedor"].lower() and
                filtro_valor in nota["valor"] and
                (filtro_parcelas == "Todos" or filtro_parcelas == nota["parcelas"]) and
                filtro_vencimento in nota["vencimento"] and
                (filtro_centro_custo == "Todos" or filtro_centro_custo.lower() in nota["centro_custo"].lower())):
                tree.insert("", tk.END, values=(
                    nota["data"], 
                    nota["fornecedor"], 
                    nota["valor"], 
                    nota["parcelas"], 
                    nota["vencimento"], 
                    nota["centro_custo"]
                ))

        # Limpar os campos de filtro após a filtragem
        entry_filtro_fornecedor.delete(0, tk.END)
        entry_filtro_valor.delete(0, tk.END)
        combo_filtro_parcelas.set("Todos")
        entry_filtro_vencimento.delete(0, tk.END)
        combo_filtro_centro_custo.set("Todos")

    def exportar_para_excel():
        # Obter dados da Treeview
        dados = []
        for row in tree.get_children():
            dados.append(tree.item(row)["values"])

        # Converter para DataFrame do pandas
        df = pd.DataFrame(dados, columns=["Data", "Fornecedor", "Valor", "Parcelas", "Vencimento", "Centro de Custo"])

        # Gerar o arquivo Excel com nome único
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        arquivo = f"historico_notas_{timestamp}.xlsx"
        df.to_excel(arquivo, index=False)

        messagebox.showinfo("Exportação", f"Histórico exportado com sucesso para {arquivo}")

    def remover_nota():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Erro", "Selecione uma nota para remover.")
            return

        nota_selecionada = tree.item(selected_item, 'values')
        data, fornecedor, valor, parcelas, vencimento, centro_custo = nota_selecionada[:6]

        for nota in notas:
            if (nota["data"] == data and
                nota["fornecedor"] == fornecedor and
                nota["valor"] == valor and
                nota["parcelas"] == parcelas and
                nota["vencimento"] == vencimento and
                nota["centro_custo"] == centro_custo):
                notas.remove(nota)
                break

        salvar_notas(notas)
        filtrar_notas()
        messagebox.showinfo("Remoção", "Nota removida com sucesso.")

    # Criar a janela de histórico de notas
    historico_window = tk.Tk()
    historico_window.title("Histórico de Notas")
    historico_window.configure(bg='#0d0d0d')  # Fundo preto
    historico_window.state('zoomed')  # Abrir em tela cheia

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
    container_frame = tk.Frame(historico_window, bg='#0d0d0d', padx=20, pady=20, bd=2, relief='solid', highlightbackground='#00ffcc', highlightthickness=2)
    container_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

    # Título
    title_label = tk.Label(container_frame, text="Histórico de Notas", font=title_font, bg='#0d0d0d', fg='#00ffcc')
    title_label.pack(pady=(10, 20))

    # Frame de filtros
    filtros_frame = tk.Frame(container_frame, bg='#0d0d0d')
    filtros_frame.pack(pady=10, padx=10, fill=tk.X)

    # Botão de Filtrar acima das caixas de filtro
    button_filtrar = tk.Button(filtros_frame, text="Filtrar", font=button_font, bg=button_bg, fg=button_fg, command=filtrar_notas, bd=2, relief='solid', highlightbackground='#00ffcc', highlightthickness=2, activebackground='#00b38f', activeforeground='#0d0d0d')
    button_filtrar.grid(row=0, column=0, columnspan=12, pady=(0, 10))

    tk.Label(filtros_frame, text="Data", font=label_font, bg='#0d0d0d', fg='#00ffcc').grid(row=1, column=0, padx=5, pady=5)
    entry_filtro_data = tk.Entry(filtros_frame, font=entry_font, bg=entry_bg, fg=entry_fg, bd=2, relief='solid', highlightbackground='#00ffcc', highlightthickness=2, insertbackground='#00ffcc', width=10)
    entry_filtro_data.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(filtros_frame, text="Fornecedor", font=label_font, bg='#0d0d0d', fg='#00ffcc').grid(row=1, column=2, padx=5, pady=5)
    entry_filtro_fornecedor = tk.Entry(filtros_frame, font=entry_font, bg=entry_bg, fg=entry_fg, bd=2, relief='solid', highlightbackground='#00ffcc', highlightthickness=2, insertbackground='#00ffcc', width=15)
    entry_filtro_fornecedor.grid(row=1, column=3, padx=5, pady=5)

    tk.Label(filtros_frame, text="Valor", font=label_font, bg='#0d0d0d', fg='#00ffcc').grid(row=1, column=4, padx=5, pady=5)
    entry_filtro_valor = tk.Entry(filtros_frame, font=entry_font, bg=entry_bg, fg=entry_fg, bd=2, relief='solid', highlightbackground='#00ffcc', highlightthickness=2, insertbackground='#00ffcc', width=10)
    entry_filtro_valor.grid(row=1, column=5, padx=5, pady=5)

    parcelas_options = ["Todos", "à vista"] + [f"{i}x" for i in range(2, 13)]
    tk.Label(filtros_frame, text="Parcelas", font=label_font, bg='#0d0d0d', fg='#00ffcc').grid(row=1, column=6, padx=5, pady=5)
    combo_filtro_parcelas = ttk.Combobox(filtros_frame, values=parcelas_options, font=entry_font, state="readonly", width=8)
    combo_filtro_parcelas.grid(row=1, column=7, padx=5, pady=5)
    combo_filtro_parcelas.set("Todos")  # Definir a opção padrão como "Todos"
    combo_filtro_parcelas.configure(**combo_style)

    tk.Label(filtros_frame, text="Vencimento", font=label_font, bg='#0d0d0d', fg='#00ffcc').grid(row=1, column=8, padx=5, pady=5)
    entry_filtro_vencimento = tk.Entry(filtros_frame, font=entry_font, bg=entry_bg, fg=entry_fg, bd=2, relief='solid', highlightbackground='#00ffcc', highlightthickness=2, insertbackground='#00ffcc', width=10)
    entry_filtro_vencimento.grid(row=1, column=9, padx=5, pady=5)

    centro_custo_options = ["Todos", "Cozinha", "Bar", "Salão", "Manutenção", "Limpeza", "Serviços Gerais", "Outros"]
    tk.Label(filtros_frame, text="Centro de Custo", font=label_font, bg='#0d0d0d', fg='#00ffcc').grid(row=1, column=10, padx=5, pady=5)
    combo_filtro_centro_custo = ttk.Combobox(filtros_frame, values=centro_custo_options, font=entry_font, state="readonly", width=8)
    combo_filtro_centro_custo.grid(row=1, column=11, padx=5, pady=5)
    combo_filtro_centro_custo.set("Todos")  # Definir a opção padrão como "Todos"
    combo_filtro_centro_custo.configure(**combo_style)

    # Treeview para exibir o histórico de notas em forma de tabela
    columns = ("data", "fornecedor", "valor", "parcelas", "vencimento", "centro_custo")
    tree = ttk.Treeview(container_frame, columns=columns, show='headings', selectmode='browse')
    
    tree.heading("data", text="Data")
    tree.heading("fornecedor", text="Fornecedor")
    tree.heading("valor", text="Valor (R$)")
    tree.heading("parcelas", text="Parcelas")
    tree.heading("vencimento", text="Vencimento")
    tree.heading("centro_custo", text="Centro de Custo")

    tree.column("data", anchor=tk.CENTER, width=100)
    tree.column("fornecedor", anchor=tk.W, width=120)
    tree.column("valor", anchor=tk.E, width=80)
    tree.column("parcelas", anchor=tk.CENTER, width=80)
    tree.column("vencimento", anchor=tk.CENTER, width=100)
    tree.column("centro_custo", anchor=tk.W, width=120)

    tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Estilizar a Treeview
    style = ttk.Style()
    style.configure("Treeview", 
                    background="white",
                    foreground="#00ffcc",
                    rowheight=25,
                    fieldbackground="white")
    style.map('Treeview', background=[('selected', '#00ffcc')], foreground=[('selected', 'black')])

    # Adicionar os dados ao Treeview na ordem inversa para mostrar a última nota primeiro
    for nota in reversed(notas):
        tree.insert("", tk.END, values=(
            nota["data"], 
            nota["fornecedor"], 
            nota["valor"], 
            nota["parcelas"], 
            nota["vencimento"], 
            nota["centro_custo"]
        ))

    # Frame para botões na parte inferior
    buttons_frame = tk.Frame(container_frame, bg='#0d0d0d')
    buttons_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=(10, 0))

    # Botão para exportar para Excel
    button_exportar = tk.Button(buttons_frame, text="Exportar para Excel", font=button_font, bg=button_bg, fg=button_fg, command=exportar_para_excel, bd=2, relief='solid', highlightbackground='#00ffcc', highlightthickness=2, activebackground='#00b38f', activeforeground='#0d0d0d')
    button_exportar.pack(side=tk.LEFT, padx=10, ipadx=10, ipady=5)

    # Botão para fechar o histórico
    button_fechar = tk.Button(buttons_frame, text="Fechar", font=button_font, bg=button_bg, fg=button_fg, bd=2, relief='solid', highlightbackground='#00ffcc', highlightthickness=2, command=historico_window.destroy, activebackground='#00b38f', activeforeground='#0d0d0d')
    button_fechar.pack(side=tk.LEFT, padx=10, ipadx=10, ipady=5)

    # Botão de Exclusão
    button_manutencao = tk.Button(buttons_frame, text="Excluir Nota", font=button_font, bg='red', fg='white', command=remover_nota, bd=2, relief='solid', highlightbackground='#00ffcc', highlightthickness=2, activebackground='#ff6666', activeforeground='#0d0d0d')
    button_manutencao.pack(side=tk.RIGHT, padx=10, ipadx=10, ipady=5)

    label_manutencao = tk.Label(buttons_frame, text="Usar em último caso", font=label_font, bg='#0d0d0d', fg='red')
    label_manutencao.pack(side=tk.RIGHT, padx=10)

    # Rodar a aplicação de histórico de notas
    historico_window.mainloop()

if __name__ == "__main__":
    notas = carregar_notas()
    open_historico_window(notas)
