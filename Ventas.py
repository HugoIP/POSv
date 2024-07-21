from tkinter import *

class Ventana(Tk):
	def ventana_login(self):
		self.frame_login=Frame(self)
		self.frame_login.pack()

		self.lblframe_login=LabelFrame(self.frame_login,text="Acceso")
		self.lblframe_login.pack(padx=10,pady=10)

		lbltitulo=Label(self.lblframe_login,text="Inicio de sesion")
		lbltitulo.pack()

		txt_usuario=Entry(self.lblframe_login)
		txt_usuario.pack(padx=10,pady=10)
		txt_clave=Entry(self.lblframe_login)
		txt_clave.pack(padx=10,pady=10)
		txt_acceso=Button(self.lblframe_login,text="Ingresar")
		txt_acceso.pack(padx=10,pady=10)

	def __init__(self):
		super().__init__()
		self.ventana_login()

	

def main():
	app=Ventana()
	app.title("vNova Internet")
	app.state("zoomed")
	app.mainloop()

if __name__=='__main__':
	main()
