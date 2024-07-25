from tkinter import Tk, StringVar, W, E, N, S
from tkinter import ttk
import math

def TemaOscuro(*args):
    estilos.configure("mainframe.TFrame", background="#010924")
    estilos_label1.configure("label1.TLabel", background="#010924", foreground="white")
    estilos_label2.configure("label2.TLabel", background="#010924", foreground="white")
    estilos_botones_numeros.configure("botones_numeros.TButton", background="#00044A", foreground="white")
    estilos_botones_numeros.map("botones_numeros.TButton", background=[("active", "#020A90")])
    estilos_botones_borrar.configure("botones_borrar.TButton", background="#010924", foreground="white")
    estilos_botones_borrar.map("botones_borrar.TButton", background=[("active", "#000AB1")])
    estilos_botones_restantes.configure("botones_restantes.TButton", background="#010924", foreground="white")
    estilos_botones_restantes.map("botones_restantes.TButton", background=[("active", "#000AB1")])

def TemaClaro(*args):
    estilos.configure("mainframe.TFrame", background="#DBDBDB")
    estilos_label1.configure("label1.TLabel", background="#DBDBDB", foreground="black")
    estilos_label2.configure("label2.TLabel", background="#DBDBDB", foreground="black")
    estilos_botones_numeros.configure("botones_numeros.TButton", background="#FFFFFF", foreground="black")
    estilos_botones_numeros.map("botones_numeros.TButton", background=[("active", "#B9B9B9")])
    estilos_botones_borrar.configure("botones_borrar.TButton", background="#CECECE", foreground="black")
    estilos_botones_borrar.map("botones_borrar.TButton", background=[("active", "#B9B9B9")])
    estilos_botones_restantes.configure("botones_restantes.TButton", background="#CECECE", foreground="black")
    estilos_botones_restantes.map("botones_restantes.TButton", background=[("active", "#B9B9B9")])

def ingresarValores(tecla):
    if tecla.isdigit() or tecla in "() .":
        entrada2.set(entrada2.get() + tecla)
    elif tecla in "*/+-":
        entrada1.set(entrada1.get() + entrada2.get() + tecla)
        entrada2.set("")
    elif tecla == "=":
        try:
            expresion = entrada1.get() + entrada2.get()
            resultado = eval(expresion)
            entrada1.set(expresion)  # Mostrar la expresión ingresada en entrada1
            entrada2.set(str(resultado))
        except Exception as e:
            entrada2.set("Error")
            print(f"Error evaluando la expresión: {e}")

def raizCuadrada():
    try:
        resultado = math.sqrt(float(entrada2.get()))
        entrada1.set("")
        entrada2.set(str(resultado))
    except ValueError as e:
        entrada2.set("Error")
        print(f"Error calculando la raíz cuadrada: {e}")

def borrar():
    entrada2.set(entrada2.get()[:-1])

def borrarTodo():
    entrada1.set("")
    entrada2.set("")

def ingresarValoresTeclado(event):
    tecla = event.keysym
    if tecla.isdigit():
        entrada2.set(entrada2.get() + event.char)
    elif tecla == "parenleft":
        ingresarValores("(")
    elif tecla == "parenright":
        ingresarValores(")")
    elif tecla == "period":
        ingresarValores(".")
    elif tecla == "asterisk":
        ingresarValores("*")
    elif tecla == "plus":
        ingresarValores("+")
    elif tecla == "minus":
        ingresarValores("-")
    elif tecla == "slash":
        ingresarValores("/")
    elif tecla == "Return":  # Para la tecla "Enter"
        ingresarValores("=")
    elif tecla == "BackSpace":
        borrar()
    elif tecla == "b":
        borrarTodo()
    elif tecla == "r":
        raizCuadrada()
    elif tecla == "o":
        TemaOscuro()
    elif tecla == "c":
        TemaClaro()

root = Tk()
root.title("Calculadora")
root.geometry("+500+80")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Estilo para el frame principal
estilos = ttk.Style()
estilos.configure("mainframe.TFrame", background="#DBDBDB")
estilos.theme_use("clam")

mainframe = ttk.Frame(root, style="mainframe.TFrame")
mainframe.grid(column=0, row=0, sticky=(N, S, E, W), padx=1, pady=1)

for i in range(4):
    mainframe.columnconfigure(i, weight=1)
    mainframe.rowconfigure(i, weight=1)

# Estilos para las etiquetas
estilos_label1 = ttk.Style()
estilos_label1.configure("label1.TLabel", font="Arial 15", anchor="e")

estilos_label2 = ttk.Style()
estilos_label2.configure("label2.TLabel", font="Arial 40", anchor="e")

# Estilos para los botones
estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure("botones_numeros.TButton", font="Arial 22", width=5, background="#FFFFFF", relief="flat")
estilos_botones_numeros.map("botones_numeros.TButton", background=[("active", "#B9B9B9")])

estilos_botones_borrar = ttk.Style()
estilos_botones_borrar.configure("botones_borrar.TButton", font="Arial 22", width=5, relief="flat", background="#CECECE")
estilos_botones_borrar.map("botones_borrar.TButton", foreground=[("active", "#FF0000")], background=[("active", "#858585")])

estilos_botones_restantes = ttk.Style()
estilos_botones_restantes.configure("botones_restantes.TButton", font="Arial 22", width=5, relief="flat", background="#CECECE")
estilos_botones_restantes.map("botones_restantes.TButton", background=[("active", "#858585")])

# Variables para las etiquetas de entrada
entrada1 = StringVar()
Label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style="label1.TLabel")
Label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W, E))

entrada2 = StringVar()
Label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, style="label2.TLabel")
Label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W, E))

# Botones de la calculadora
Button0 = ttk.Button(mainframe, text="0", style="botones_numeros.TButton", command=lambda: ingresarValores("0"))
Button1 = ttk.Button(mainframe, text="1", style="botones_numeros.TButton", command=lambda: ingresarValores("1"))
Button2 = ttk.Button(mainframe, text="2", style="botones_numeros.TButton", command=lambda: ingresarValores("2"))
Button3 = ttk.Button(mainframe, text="3", style="botones_numeros.TButton", command=lambda: ingresarValores("3"))
Button4 = ttk.Button(mainframe, text="4", style="botones_numeros.TButton", command=lambda: ingresarValores("4"))
Button5 = ttk.Button(mainframe, text="5", style="botones_numeros.TButton", command=lambda: ingresarValores("5"))
Button6 = ttk.Button(mainframe, text="6", style="botones_numeros.TButton", command=lambda: ingresarValores("6"))
Button7 = ttk.Button(mainframe, text="7", style="botones_numeros.TButton", command=lambda: ingresarValores("7"))
Button8 = ttk.Button(mainframe, text="8", style="botones_numeros.TButton", command=lambda: ingresarValores("8"))
Button9 = ttk.Button(mainframe, text="9", style="botones_numeros.TButton", command=lambda: ingresarValores("9"))

Button_borrar = ttk.Button(mainframe, text=chr(9003), style="botones_borrar.TButton", command=borrar)
Button_borrar_todo = ttk.Button(mainframe, text="C", style="botones_borrar.TButton", command=borrarTodo)
Button_parentesis1 = ttk.Button(mainframe, text="(", style="botones_restantes.TButton", command=lambda: ingresarValores("("))
Button_parentesis2 = ttk.Button(mainframe, text=")", style="botones_restantes.TButton", command=lambda: ingresarValores(")"))
Button_punto = ttk.Button(mainframe, text=".", style="botones_restantes.TButton", command=lambda: ingresarValores("."))

Button_division = ttk.Button(mainframe, text="÷", style="botones_restantes.TButton", command=lambda: ingresarValores("/"))
Button_multiplicacion = ttk.Button(mainframe, text="*", style="botones_restantes.TButton", command=lambda: ingresarValores("*"))
Button_resta = ttk.Button(mainframe, text="-", style="botones_restantes.TButton", command=lambda: ingresarValores("-"))
Button_suma = ttk.Button(mainframe, text="+", style="botones_restantes.TButton", command=lambda: ingresarValores("+"))

Button_igual = ttk.Button(mainframe, text="=", style="botones_restantes.TButton", command=lambda: ingresarValores("="))
Button_raiz_cuadrada = ttk.Button(mainframe, text="√", style="botones_restantes.TButton", command=raizCuadrada)

# Posicionamiento de los botones en la cuadrícula
Button_parentesis1.grid(column=0, row=2, padx=1, pady=1, sticky=(W, N, E, S))
Button_parentesis2.grid(column=1, row=2, padx=1, pady=1, sticky=(W, N, E, S))
Button_borrar_todo.grid(column=2, row=2, padx=1, pady=1, sticky=(W, N, E, S))
Button_borrar.grid(column=3, row=2, padx=1, pady=1, sticky=(W, N, E, S))

Button7.grid(column=0, row=3, padx=1, pady=1, sticky=(W, N, E, S))
Button8.grid(column=1, row=3, padx=1, pady=1, sticky=(W, N, E, S))
Button9.grid(column=2, row=3, padx=1, pady=1, sticky=(W, N, E, S))
Button_division.grid(column=3, row=3, padx=1, pady=1, sticky=(W, N, E, S))

Button4.grid(column=0, row=4, padx=1, pady=1, sticky=(W, N, E, S))
Button5.grid(column=1, row=4, padx=1, pady=1, sticky=(W, N, E, S))
Button6.grid(column=2, row=4, padx=1, pady=1, sticky=(W, N, E, S))
Button_multiplicacion.grid(column=3, row=4, padx=1, pady=1, sticky=(W, N, E, S))

Button1.grid(column=0, row=5, padx=1, pady=1, sticky=(W, N, E, S))
Button2.grid(column=1, row=5, padx=1, pady=1, sticky=(W, N, E, S))
Button3.grid(column=2, row=5, padx=1, pady=1, sticky=(W, N, E, S))
Button_suma.grid(column=3, row=5, padx=1, pady=1, sticky=(W, N, E, S))

Button0.grid(column=0, row=6, columnspan=2, sticky=(W, N, E, S), padx=1, pady=1)
Button_punto.grid(column=2, row=6, padx=1, pady=1, sticky=(W, N, E, S))
Button_resta.grid(column=3, row=6, padx=1, pady=1, sticky=(W, N, E, S))

Button_igual.grid(column=0, row=7, columnspan=3, sticky=(W, N, E, S), padx=1, pady=1)
Button_raiz_cuadrada.grid(column=3, row=7, padx=1, pady=1, sticky=(W, N, E, S))

# Ajustar el relleno de todos los widgets dentro del mainframe
for child in mainframe.winfo_children():
    child.grid_configure(ipady=1)

root.bind("<KeyPress>", ingresarValoresTeclado)

root.mainloop()