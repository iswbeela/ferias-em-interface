from tkinter import *

# Função para verificar o pedido de férias
def ferias():
    try:
        tempo = int(tempo_entry.get())
        mes = int(mes_entry.get())
        if tempo > 3:
            resultado_label.config(text="Pedido de férias aprovado")
        elif mes not in [6, 7, 12, 1]:
            resultado_label.config(text="Férias fora da temporada")
        else:
            resultado_label.config(text="Pedido de férias negado")
    except ValueError:
        resultado_label.config(text="Por favor, insira valores válidos")

# Criando a interface gráfica
app = Tk()
app.title("Sistema de Férias")
app.geometry("400x300+100+100")

# Campo para tempo de serviço
Label(app, text="Tempo de serviço (em anos):").pack()
tempo_entry = Entry(app)
tempo_entry.pack()

# Campo para o mês desejado de férias
Label(app, text="Mês desejado para as férias (1-12):").pack()
mes_entry = Entry(app)
mes_entry.pack()

# Criando o botão para verificar o pedido de férias
Button(app, text="Verificar Pedido de Férias", command=ferias).pack()

# Label para exibir o resultado
resultado_label = Label(app, text="", fg="blue")
resultado_label.pack()

app.mainloop()
