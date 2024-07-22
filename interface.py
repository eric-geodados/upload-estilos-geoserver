import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import tkinter.font as tkFont
from PIL import Image, ImageTk
from estilos_geoserver import criar_estilo, listar_workspaces, validar_login
from tkinter import messagebox


class Interface:

    cor = "#13191C"
    cor_botoes = "#00ABD1"
    fonte = "Segoe UI"

    # Configurações da self.janela principal
    def __init__(self):        
        self.janela = tk.Tk()
        self.janela.title("CRIADOR DE ESTILOS GEOSERVER")
        self.janela.geometry("550x350")
        self.janela.configure(bg=self.cor)
        
        # Configurar a grade da janela principal para centralizar o frame
        self.janela.grid_rowconfigure(0, weight=1)
        self.janela.grid_rowconfigure(1, weight=1)
        self.janela.grid_columnconfigure(0, weight=1)
        self.janela.grid_columnconfigure(1, weight=1)

        # Estilos
        self.fonte_titulos = tkFont.Font(family="Segoe UI", size=22, weight="bold")
        self.fonte_padrao = tkFont.Font(family="Segoe UI", size=14, weight="bold")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", font=self.fonte_padrao, background=self.cor_botoes, foreground="white", padding=3)
        style.map("TButton", background=[("active", "#008CAB")])

        # Frame principal com cor de fundo
        self.login_frame = ttk.Frame(self.janela, padding="20", style="Custom.TFrame")
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        self.upload_frame = ttk.Frame(self.janela, padding="20", style="Custom.TFrame")
        self.upload_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Configurando a cor de fundo do frame
        style.configure("Custom.TFrame", background=self.cor)
        
        
        self.login()


    def login(self):
        # Variáveis para armazenar os caminhos das pastas
        self.usuario = tk.StringVar()
        self.usuario.trace("w", self.desabilitador_botao_logar)
        self.senha = tk.StringVar()
        self.senha.trace("w", self.desabilitador_botao_logar)
        
        
        ttk.Label(self.login_frame, text="CRIADOR DE ESTILOS GEOSERVER", font=self.fonte_titulos, background=self.cor, foreground="white").grid(column=0, row=0, padx=10, pady=5, columnspan=2)
        ttk.Label(self.login_frame, text="――――――――――――――――――――――――――――――――――――――――――", font=(self.fonte, 8), background=self.cor, foreground="white").grid(column=0, row=1, padx=10, pady=5, columnspan=2)

        # Usuário
        ttk.Label(self.login_frame, text="Usuário do GeoServer:", font=(self.fonte, 16), background=self.cor, foreground="white").grid(column=0, row=2, padx=10, pady=5, sticky="e")
        self.usuario_entrada = tk.Entry(self.login_frame, textvariable=self.usuario, font=(self.fonte, 12), background="white", width=23)
        self.usuario_entrada.grid(column=1, row=2, padx=20, pady=5, columnspan=2, sticky="w")

        # Senha
        ttk.Label(self.login_frame, text="Senha:", font=(self.fonte, 16), background=self.cor, foreground="white").grid(column=0, row=3, padx=10, pady=5, sticky="e")
        self.senha_entrada = tk.Entry(self.login_frame, textvariable=self.senha, show="*",font=(self.fonte, 12), background="white", width=23)
        self.senha_entrada.grid(column=1, row=3, padx=20, pady=5, columnspan=2, sticky="w")

        # Botão de login
        self.botao_logar = ttk.Button(self.login_frame, text="Logar", command=self.ao_clicar_botao_logar, padding=10)
        self.botao_logar.grid(column=0, row=4, sticky="ew", columnspan=2, padx=20, pady=10)
        self.botao_logar.config(state=tk.DISABLED)
        self.janela.bind('<Return>', self.ao_clicar_botao_logar)
        
        # Créditos ao Desenvolvedor
        ttk.Label(self.login_frame, text="2024 © Desenvolvido por Eric Cabral", font=('Segoe UI', 10), background=self.cor, foreground="white").grid(column=0, row=5, padx=5, pady=10, sticky='w')

        # Mostrar o frame de login centralizado
        self.login_frame.grid(row=1, column=1, sticky="nsew")

    def upload(self):
        self.login_frame.grid_forget()
        
        # Variáveis para armazenar os caminhos das pastas
        self.pasta = tk.StringVar()
        self.pasta.trace("w", self.desabilitador_botao_criar)  # Monitora alterações no StringVar
        
        
        ttk.Label(self.upload_frame, text="CRIADOR DE ESTILOS GEOSERVER", font=self.fonte_titulos, background=self.cor, foreground="white").grid(column=0, row=0, padx=10, pady=5, columnspan=2)
        ttk.Label(self.upload_frame, text="――――――――――――――――――――――――――――――――――――――――――", font=(self.fonte, 8), background=self.cor, foreground="white").grid(column=0, row=1, padx=10, pady=5, columnspan=2)
        
        # Selecionar caminho do estilo
        ttk.Label(self.upload_frame, text="Caminho do Estilo:", font=(self.fonte, 16), background=self.cor, foreground="white").grid(column=0, row=2, padx=10, pady=5, sticky="e")
        ttk.Button(self.upload_frame, text="Selecionar (.ZIP)", command=self.abrir_pasta).grid(column=1, row=2, padx=20, pady=5, sticky="w")

        # Carregar a imagem do check
        self.checkmark_image = Image.open(r".\venv\check.png").resize((30, 30))
        self.checkmark_photo = ImageTk.PhotoImage(self.checkmark_image)
        self.checkmark_label = ttk.Label(self.upload_frame, background=self.cor)
        self.checkmark_label.grid(column=1, row=2, padx=15, pady=5, sticky="e")

        # Município
        ttk.Label(self.upload_frame, text="Município:", font=(self.fonte, 16), background=self.cor, foreground="white").grid(column=0, row=3, padx=10, pady=5, sticky="e")
        self.combobox = ttk.Combobox(self.upload_frame, font=(self.fonte, 10), values=listar_workspaces(self.usuario.get(), self.senha.get()), width=25)
        self.combobox.grid(column=1, row=3, sticky="w", columnspan=2, padx=20, pady=5)

        # Botão criar
        self.botao_criar = ttk.Button(self.upload_frame, text="Enviar", command=self.ao_clicar_botao_criar, padding=10)
        self.botao_criar.grid(column=0, row=4, sticky="ew", columnspan=3, padx=20, pady=10)
        self.botao_criar.config(state=tk.DISABLED)
        self.janela.bind('<Return>', self.ao_clicar_botao_criar)

        # Créditos ao Desenvolvedor
        ttk.Label(self.upload_frame, text="2024 © Desenvolvido por Eric Cabral", font=('Segoe UI', 10), background=self.cor, foreground="white").grid(column=0, row=5, padx=5, pady=10, sticky='w')

        # Mostrar o frame de login centralizado
        self.upload_frame.grid(row=1, column=1, sticky="nsew")


    # Função para abrir os seletores de pasta
    def abrir_pasta(self):
        caminho = filedialog.askopenfilename(filetypes=[("Arquivos ZIP", "*.zip")])
        if caminho:
            self.pasta.set(caminho)


    # Função para desabilitar botão até selecionar pastas
    def desabilitador_botao_logar(self, *args):
        if self.usuario.get().strip() and self.senha.get().strip():
            self.botao_logar.config(state=tk.NORMAL)
        else:
            self.botao_logar.config(state=tk.DISABLED)
    
    # Função para desabilitar botão até selecionar pastas
    def desabilitador_botao_criar(self, *args):
        if self.pasta.get().strip():
            self.botao_criar.config(state=tk.NORMAL)
            self.checkmark_label.config(image=self.checkmark_photo)
        else:
            self.botao_criar.config(state=tk.DISABLED)


    def ao_clicar_botao_logar(self, event=None):
        self.logar_para_upload()


    def ao_clicar_botao_criar(self, event=None):
        self.enviar_estilo()


    def logar_para_upload(self):
        if not validar_login(self.usuario.get(), self.senha.get()):
            messagebox.showwarning('FALHA NO LOGIN', 'Usuário ou senha inválidos!')
            self.usuario_entrada.delete(0, tk.END)
            self.senha_entrada.delete(0, tk.END)
        else:
            self.upload()


    def enviar_estilo(self):
        if criar_estilo(self.usuario.get(), self.senha.get(), self.combobox.get(), self.pasta.get()):
            messagebox.showinfo('STATUS DE PROCESSAMENTO', '✓ Estilo criado e carregado com sucesso ao GeoServer!')
            self.continuar_envio_estilo()
        else:
            messagebox.showerror('STATUS DE PROCESSAMENTO', 'Erro ao criar estilo!\nVerifique se o arquivo carregado está zipado com um arquivo .SLD dentro!')        
            self.upload()

    def continuar_envio_estilo(self):
        self.mensagem_continuar_envio = messagebox.askyesno("CONFIRMAÇÃO", "Você deseja enviar outro estilo?")
        if self.mensagem_continuar_envio:
            self.upload()
        else:
            self.janela.destroy()
