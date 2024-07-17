import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import tkinter.font as tkFont
from PIL import Image, ImageTk
from upload_estilos import criar_estilo


class Interface:

    cor = "#13191C"
    cor_botoes = "#00ABD1"
    fonte = "Segoe UI"

    # Configurações da janela principal
    def __init__(self):
        super().__init__()
        
        janela = tk.Tk()
        janela.title("CRIADOR DE ESTILOS GEOSERVER")
        janela.geometry("600x450")
        janela.configure(bg=self.cor)

        # Estilos
        fonte_titulos = tkFont.Font(family="Segoe UI", size=22, weight="bold")
        fonte_padrao = tkFont.Font(family="Segoe UI", size=14, weight="bold")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", font=fonte_padrao, background=self.cor_botoes, foreground="white", padding=3)
        style.map("TButton", background=[("active", "#008CAB")])

        # Frame principal com cor de fundo
        frame = ttk.Frame(janela, padding="20", style="Custom.TFrame")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Configurando a cor de fundo do frame
        style.configure("Custom.TFrame", background=self.cor)

        # Variáveis para armazenar os caminhos das pastas
        self.pasta = tk.StringVar()
        self.pasta.trace("w", self.desabilitador_botao)  # Monitora alterações no StringVar
        self.usuario = tk.StringVar()
        self.usuario.trace("w", self.desabilitador_botao)
        self.senha = tk.StringVar()
        self.senha.trace("w", self.desabilitador_botao)


        ttk.Label(frame, text="CRIADOR DE ESTILOS GEOSERVER", font=fonte_titulos, background=self.cor, foreground="white").grid(column=0, row=1, padx=10, pady=5, columnspan=2)

        # Usuário
        ttk.Label(frame, text="Usuário do Geoserver:", font=(self.fonte, 16), background=self.cor, foreground="white").grid(column=0, row=2, padx=10, pady=10, sticky="e")
        tk.Entry(frame, textvariable=self.usuario, font=(self.fonte, 12), background="white", width=23).grid(column=1, row=2, padx=20, pady=10, columnspan=2, sticky="w")

        # Senha
        ttk.Label(frame, text="Senha:", font=(self.fonte, 16), background=self.cor, foreground="white").grid(column=0, row=3, padx=10, pady=10, sticky="e")
        tk.Entry(frame, textvariable=self.senha, font=(self.fonte, 12), background="white", width=23).grid(column=1, row=3, padx=20, pady=10, columnspan=2, sticky="w")
        
        # Selecionar caminho do estilo
        ttk.Label(frame, text="Caminho do estilo:", font=(self.fonte, 16), background=self.cor, foreground="white").grid(column=0, row=4, padx=10, pady=10, sticky="e")
        ttk.Button(frame, text="Selecionar Pasta", command=self.abrir_pasta).grid(column=1, row=4, padx=20, pady=10, sticky="w")

        # Carregar a imagem do check
        self.checkmark_image = Image.open(r".\venv\check.png").resize((30, 30))
        self.checkmark_photo = ImageTk.PhotoImage(self.checkmark_image)
        self.checkmark_label = ttk.Label(frame, background=self.cor)
        self.checkmark_label.grid(column=1, row=4, padx=20, pady=10, sticky="e")

        # Botão Criar
        self.botao_criar = ttk.Button(frame, text="Criar", command=self.exibir_estilos, padding=10)
        self.botao_criar.grid(column=0, row=5, sticky="ew", columnspan=2, padx=20, pady=10)
        self.botao_criar.config(state=tk.DISABLED)


        self.exibir = ttk.Label(frame, text="TESTE", font=(self.fonte, 16), background="white", foreground="black")
        self.exibir.grid(column=0, row=6, padx=10, pady=10, columnspan=2)
        
        # Créditos ao Desenvolvedor
        ttk.Label(frame, text="2024 © Desenvolvido por Eric Cabral", font=('Segoe UI', 10), background=self.cor, foreground="white").grid(column=0, row=7, padx=5, pady=10, sticky='w')


        janela.mainloop()
      
        
    # Função para abrir os seletores de pasta
    def abrir_pasta(self):
        caminho = filedialog.askdirectory()
        if caminho:
            self.pasta.set(caminho)


    # Função para desabilitar botão até selecionar pastas
    def desabilitador_botao(self, *args):
        if self.pasta.get().strip():
            self.botao_criar.config(state=tk.NORMAL)
            self.checkmark_label.config(image=self.checkmark_photo)
        else:
            self.botao_criar.config(state=tk.DISABLED)


    def exibir_estilos(self):
        resultado = criar_estilo(self.usuario.get(), self.senha.get())
        self.exibir.config(text=resultado)
