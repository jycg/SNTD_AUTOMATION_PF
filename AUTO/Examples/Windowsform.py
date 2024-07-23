import tkinter as tk
from tkinter import messagebox

def run_app():
    messagebox.showinfo("info", "Automation completed")

def on_button_click():
    try:
        run_app()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Configuración de la ventana principal de tkinter
root = tk.Tk()
root.title("Automation desktop")
window_width = 1200
window_height = 650

# Obtén las dimensiones de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcula la posición del centro
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# Establece la geometría de la ventana
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Crear un botón que ejecute el script de automatización
button = tk.Button(root, text="Example", command=on_button_click)
button.pack(pady=50)

# Ejecutar el bucle principal de tkinter
root.mainloop()
