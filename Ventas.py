from tkinter import *
from tkinter import ttk
import ttkbootstrap as tb

class Ventana(tb.Window):
	def __init__(self):
		super().__init__()
		self.ventana_login()
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
		txt_acceso=ttk.Button(self.lblframe_login,text="Ingresar",width=38,command=self.logueo)#"call function logueo"
		txt_acceso.pack(padx=10,pady=10)

	def ventana_menu(self):
		self.frame_left=Frame(self,width=200)
		self.frame_left.grid(row=0,column=0,sticky=NSEW)
		self.frame_center=Frame(self)
		self.frame_center.grid(row=0,column=1,sticky=NSEW)
		self.frame_rigth=Frame(self,width=400)
		self.frame_rigth.grid(row=0,column=2,sticky=NSEW)

		btn_productos=ttk.Button(self.frame_left,text="Productos",width=15)
		btn_productos.grid(row=0,column=0,padx=10,pady=10)
		btn_ventas=ttk.Button(self.frame_left,text="Ventas",width=15)
		btn_ventas.grid(row=1,column=0,padx=10,pady=10)
		bnt_clientes=ttk.Button(self.frame_left,text="Clientes",width=15)
		bnt_clientes.grid(row=2,column=0,padx=10,pady=10)
		bnt_compras=ttk.Button(self.frame_left,text="Compras",width=15)
		bnt_compras.grid(row=3,column=0,padx=10,pady=10)
		bnt_usuarios=ttk.Button(self.frame_left,text="Usuarios",width=15,command=self.ventana_lista_usuarios)
		bnt_usuarios.grid(row=4,column=0,padx=10,pady=10)
		bnt_reportes=ttk.Button(self.frame_left,text="Reportes",width=15)
		bnt_reportes.grid(row=5,column=0,padx=10,pady=10)
		bnt_backup=ttk.Button(self.frame_left,text="Backup",width=15)
		bnt_backup.grid(row=6,column=0,padx=10,pady=10)
		bnt_restaurarbd=ttk.Button(self.frame_left,text="Restauras BD",width=15)
		bnt_restaurarbd.grid(row=7,column=0,padx=10,pady=10)

		lbl2=Label(self.frame_center,text="Aqui pondremos las ventanas que creemos")
		lbl2.grid(row=0,column=0,padx=10,pady=10)
		lbl3=Label(self.frame_rigth,text="Aqui pondremos las busquedas para la venta")
		lbl3.grid(row=0,column=0,padx=10,pady=10)

	def logueo(self):
		self.frame_login.pack_forget()
		self.ventana_menu()

	def ventana_lista_usuarios(self):
		self.frame_lista_usuarios=Frame(self.frame_center)
		self.frame_lista_usuarios.grid(row=0,column=0,columnspan=2,sticky=NSEW)

		self.lblframe_botones_listausu=LabelFrame(self.frame_lista_usuarios)
		self.lblframe_botones_listausu.grid(row=0,column=0,sticky=NSEW)

		btn_nuevo_usuario=ttk.Button(self.lblframe_botones_listausu,text="Nuevo",width=15)
		btn_nuevo_usuario.grid(row=0,column=0,padx=5,pady=5)
		btn_modificar_usuario=ttk.Button(self.lblframe_botones_listausu,text="Modificar",width=15)
		btn_modificar_usuario.grid(row=0,column=1,padx=5,pady=5)
		btn_eliminar_usuario=ttk.Button(self.lblframe_botones_listausu,text="Eliminar",width=15)
		btn_eliminar_usuario.grid(row=0,column=2,padx=5,pady=5)

		self.lblframe_busqueda_listausu=LabelFrame(self.frame_lista_usuarios)
		self.lblframe_busqueda_listausu.grid(row=1,column=0,sticky=NSEW)
		txt_busqueda_usuarios=ttk.Entry(self.lblframe_busqueda_listausu,width=50)
		txt_busqueda_usuarios.grid(row=0,column=0,padx=5,pady=5)


		self.lblframe_tree_listausu=LabelFrame(self.frame_lista_usuarios)
		self.lblframe_tree_listausu.grid(row=2,column=0,sticky=NSEW)

		columnas=("codigo","nombre","clave","rol")

		tree_lista_usuarios=ttk.Treeview(self.lblframe_tree_listausu,columns=columnas,height=17,show="headings")
		tree_lista_usuarios.grid(row=0,column=0)
		tree_lista_usuarios.heading("codigo",text="Codigo",anchor=W)
		tree_lista_usuarios.heading("nombre",text="Nombre",anchor=W)
		tree_lista_usuarios.heading("clave",text="Clave",anchor=W)
		tree_lista_usuarios.heading("rol",text="Rol",anchor=W)
		tree_lista_usuarios["displaycolumns"]=("codigo","nombre","rol")#para ocultar la clave

		#Scrollbar
		tree_scroll_listausu=Scrollbar(self.frame_lista_usuarios)
		tree_scroll_listausu.grid(row=2,column=1)
		#Config Scrollbar
		tree_scroll_listausu.config(command=tree_lista_usuarios.yview)





	

def main():
	app=Ventana()
	app.title("vNova Internet")
	app.state("zoomed")
	tb.Style("superhero")
	app.mainloop()

if __name__=='__main__':
	main()
