from tkinter import *

# Cria a janela
janela = Tk()
janela.title("Tela de Login")
janela.geometry("400x300")
janela.configure(bg="#E0FFFF")

# Define as cores
cor1 = "#00CED1"
cor2 = "#F5FFFA"

# Função para o botão de login
def login():
    username = entrada_username.get()
    password = entrada_password.get()
    if username == "admin" and password == "1234":
        texto_aviso.configure(text="Login Feito com sucesso!", fg="green")
    else:
        texto_aviso.configure(text="Usuário ou senha inválido!", fg="red")

# Função para o botão de cadastro
def cadastrar():
    novo_usuario = entrada_username.get()
    nova_senha = entrada_password.get()
    arquivo = open("usuarios.txt", "a")
    arquivo.write(f"{novo_usuario}:{nova_senha}\n")
    arquivo.close()
    texto_aviso.configure(text="Usuário cadastrado com sucesso!", fg="green")

# Label de boas-vindas
texto_boas_vindas = Label(janela, text="Bem-vindo(a)!", font=("Arial", 18), bg=cor1, fg="white")
texto_boas_vindas.pack(fill=X)

# Label e campo de entrada de usuário
label_username = Label(janela, text="Usuário:", font=("Arial", 14), bg=cor2, fg="black")
label_username.place(x=50, y=100)
entrada_username = Entry(janela, font=("Arial", 14))
entrada_username.place(x=150, y=100)

# Label e campo de entrada de senha
label_password = Label(janela, text="Senha:", font=("Arial", 14), bg=cor2, fg="black")
label_password.place(x=50, y=150)
entrada_password = Entry(janela, font=("Arial", 14), show="*")
entrada_password.place(x=150, y=150)

# Botão de login
botao_login = Button(janela, text="Login", font=("Arial", 14), bg=cor1, fg="white", command=login)
botao_login.place(x=100, y=200)

# Botão de cadastro
botao_cadastrar = Button(janela, text="Cadastrar", font=("Arial", 14), bg=cor1, fg="white", command=cadastrar)
botao_cadastrar.place(x=200, y=200)

# Label para mensagens de aviso
texto_aviso = Label(janela, font=("Arial", 14), bg="#E0FFFF")
texto_aviso.place(x=50, y=250)

# Executa a janela
janela.mainloop()
