from tkinter import *
from tkinter import ttk
import ttkbootstrap as tb

class Ventana(tb.Window):
	def ventana_login(self):
		self.frame_login=Frame(self)
		self.frame_login.pack()

		self.lblframe_login=LabelFrame(self.frame_login,text="Acceso")
		self.lblframe_login.pack(padx=10,pady=10)

		lbltitulo=ttk.Label(self.lblframe_login,text="Inicio de sesion", font=('Arial',18))
		lbltitulo.pack(padx=10,pady=35)

		txt_usuario=ttk.Entry(self.lblframe_login,width=40,justify=CENTER)
		txt_usuario.pack(padx=10,pady=10)
		txt_clave=ttk.Entry(self.lblframe_login,width=40,justify=CENTER)
		txt_clave.pack(padx=10,pady=10)
		txt_clave.configure(show='*')
		txt_acceso=ttk.Button(self.lblframe_login,text="Ingresar",width=34)
		txt_acceso.pack(padx=10,pady=10)

	def __init__(self):
		super().__init__()
		self.ventana_login()

	

def main():
	app=Ventana()
	app.title("vNova Internet")
	app.state("zoomed")
	tb.Style("superhero")
	app.mainloop()

if __name__=='__main__':
	main()
