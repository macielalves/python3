from googletrans import Translator  # pip install googletrans==4.0.0-rc1
from tkinter import *  # Tk, Frame, Button, Label, Entry, Place
from tkinter import ttk


class Tela(Tk):
    def __init__(self):
        # root
        super().__init__()
        self.title("Tradutor")
        self.geometry("500x400")
        self.minsize(width=500, height=400)
        self.resizable(width=True, height=True)
        # tela
        self.frame_1 = None
        self.frame_2 = None
        self.lb_entrada = None
        self.ld_qtd = None
        self.text_entry = None
        self.btn_get_text = None
        self.btn_detect = None
        self.circulo = None
        self.idioma_detectado = None
        self.idioma_destino = None
        self.text_out = None
        self.frames()
        self.container()
        # start tela

    def frames(self):
        self.frame_1 = Frame(self, bg="#aae3e1")
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.48)
        self.frame_2 = Frame(self, bg="#aae3e1")
        self.frame_2.place(relx=0.02, rely=0.499, relwidth=0.96, relheight=0.48)

    def container(self):
        self.lb_entrada = Label(self.frame_1, text="Insira o texto a ser traduzido:")
        self.lb_entrada.place(relx=0.02, rely=0.02, relwidth=0.4, relheight=0.1)

        # self.text_entry = Entry(self.frame_1)
        self.text_entry = Text(self.frame_1, maxundo=15000)
        self.text_entry.place(relx=0.02, rely=0.15, relwidth=0.96, relheight=0.7)

        self.text_out = Text(self.frame_2, maxundo=15000)
        self.text_out.place(relx=0.02, rely=0.05, relwidth=0.96, relheight=0.7)

        self.idioma_destino = ttk.Combobox(self.frame_1, state="readonly", values=("pt", "en"))
        self.idioma_destino.set("pt")
        self.idioma_destino.place(relx=0.54, rely=0.9, relwidth=0.1, relheight=0.1)

        self.btn_get_text = Button(self.frame_1, text="Traduzir", command=self.traduzir)
        self.btn_get_text.place(relx=0.88, rely=0.9, relwidth=0.1, relheight=0.1)

        self.btn_detect = Button(self.frame_1, text="Detectar idioma", command=self.detectar_idioma)
        self.btn_detect.place(relx=0.66, rely=0.9, relwidth=0.2, relheight=0.1)

        # self.circulo = Canvas(self.frame_1)
        # self.circulo.grid()
        # self.circulo.create_oval(100, 100, 5, 5, fill="red")
        ...

    def traduzir(self):
        entrada = self.text_entry.get("1.0", "end-1c")
        dest = self.idioma_destino.get()
        tradutor = Translator()
        try:
            traducao = tradutor.translate(entrada, dest=dest)
            texto_traduzido = traducao.text
        except TypeError:
            texto_traduzido = ""
            print("Erro ao traduzir")
        self.text_out.delete("1.0", "2.0")
        self.text_out.insert("end", texto_traduzido)

    def detectar_idioma(self):
        detectado = Translator()
        entrada = self.text_entry.get("1.0", "end-1c")
        try:
            detectado = detectado.detect(entrada).lang
        except TypeError:
            detectado = "Idioma não identificado"
        finally:
            self.idioma_detectado = detectado

        print(self.idioma_detectado)

    def event_time(self):
        entrada = self.text_entry.get("1.0", "end-1c")
        self.ld_qtd = Label(self.frame_1, text=f"{len(entrada)} caracteres")
        self.ld_qtd.place(relx=0.78, rely=0.02, relwidth=0.2, relheight=0.1)
        ...


tela = Tela()
tela.mainloop()
