from tkinter import  Tk, Button, Entry, Label, ttk, PhotoImage
from tkinter import  StringVar, Scrollbar,Frame, messagebox
from conexion import *
import time
from datetime import datetime 
class Ventana(Frame):
    def __init__(self, master, *args):
        super().__init__( master,*args)
        self.menu = True
        self.color = True
                
        self.codpro = StringVar()
        self.tipmov = StringVar()
        self.nummov = StringVar()
        self.fecmov = datetime.now().strftime('%d-%m-%Y')
        self.descripcion = StringVar()
        self.detalle = StringVar()
        self.unidad = StringVar()
        self.cantidad = StringVar()
        self.fecpro = StringVar()
        self.lote = StringVar()
        self.fecven = StringVar()
        self.costouni = StringVar()
        self.amount = StringVar()
        self.buscar = StringVar()
        self.buscar_actualiza =  StringVar()
        self.id = StringVar()
        
        self.base_datos = Registro_datos()
        
        self.frame_inicio = Frame(self.master, bg='black', width=50, height=45)
        self.frame_inicio.grid_propagate(0)
        self.frame_inicio.grid(column=0, row = 0, sticky='nsew')
        self.frame_menu = Frame(self.master, bg='black', width = 50)
        self.frame_menu.grid_propagate(0)
        self.frame_menu.grid(column=0, row = 1, sticky='nsew')
        self.frame_top = Frame(self.master, bg='black', height = 50)
        self.frame_top.grid(column = 1, row = 0, sticky='nsew')
        self.frame_principal = Frame(self.master, bg='black')
        self.frame_principal.grid(column=1, row=1, sticky='nsew')
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.frame_principal.columnconfigure(0, weight=1)
        self.frame_principal.rowconfigure(0, weight=1)
        
        self.widgets()
		

    def pantalla_inicio(self):
        self.paginas.select([self.frame_uno])

	
    def pantalla_maestro(self):
        self.paginas.select([self.frame_dos])
        self.frame_dos.columnconfigure(0, weight=1)
        self.frame_dos.columnconfigure(1, weight=1)
        self.frame_dos.rowconfigure(2, weight=1)
        self.frame_tabla_uno.columnconfigure(0, weight=1)
        self.frame_tabla_uno.rowconfigure(0, weight=1)

    def pantalla_entrada(self):
        self.paginas.select([self.frame_tres])
        self.frame_tres.columnconfigure(0, weight=1)
        self.frame_tres.columnconfigure(1, weight=1)

    def pantalla_editar(self):
        self.paginas.select([self.frame_cuatro])	
        self.frame_cuatro.columnconfigure(0, weight=1)
        self.frame_cuatro.columnconfigure(1, weight=1)

    def pantalla_salida(self):
        self.paginas.select([self.frame_cinco])
        self.frame_cinco.columnconfigure(0, weight=1)
        self.frame_cinco.columnconfigure(1, weight=1)

    def pantalla_movimientos(self):
        self.paginas.select([self.frame_siete])
        self.frame_siete.columnconfigure(0, weight=1)
        self.frame_siete.columnconfigure(1, weight=1)
        self.frame_siete.rowconfigure(2, weight=1)
        self.frame_tabla_dos.columnconfigure(0, weight=1)
        self.frame_tabla_dos.rowconfigure(0, weight=1)
    
    def pantalla_creditos(self):
        self.paginas.select([self.frame_seis])


    def menu_lateral(self):
        if self.menu is True:
            for i in range(50,200,10):				
                self.frame_menu.config(width= i)
                self.frame_inicio.config(width= i)
                self.frame_menu.update()
                clik_inicio = self.bt_cerrar.grid_forget()
                if clik_inicio is None:		
                    self.bt_inicio.grid(column=0, row=0, padx =10, pady=10)
                    self.bt_inicio.grid_propagate(0)
                    self.bt_inicio.config(width=i)
                    self.pantalla_inicio()
                self.menu = False
        else:
            for i in range(170,50,-10):
                self.frame_menu.config(width=  i)
                self.frame_inicio.config(width= i)
                self.frame_menu.update()
                clik_inicio = self.bt_inicio.grid_forget()
                if clik_inicio is   None:
                    self.frame_menu.grid_propagate(0)		
                    self.bt_cerrar.grid(column=0, row=0, padx =10, pady=10)
                    self.bt_cerrar.grid_propagate(0)
                    self.bt_cerrar.config(width=i)
                    self.pantalla_inicio()
                self.menu = True

    def cambiar_color(self):
        if self.color == True:
            self.bt_color['image'] = self.dia
            self.titulo.config(fg='deep sky blue')
            self.frame_seis.config(bg= 'black')
            self.text_ajustes.config(bg='black')
            self.texto.config(bg='black')
            self.bt_color.config(bg='black',activebackground='black')	
            self.color = False	
        else:
            self.bt_color['image'] = self.noche
            self.titulo.config(fg='white')
            self.frame_seis.config(bg= 'white')
            self.text_ajustes.config(bg='white')
            self.texto.config(bg='white')
            self.bt_color.config(bg='white',activebackground='white')	
            self.color = True

    def widgets(self):
        self.imagen_inicio = PhotoImage(file ='inicio.png')
        self.imagen_menu = PhotoImage(file ='menu.png')
        self.imagen_maestro = PhotoImage(file ='maestro.png')
        self.imagen_entrada = PhotoImage(file ='entrada.png')
        self.imagen_editar = PhotoImage(file ='editar.png')
        self.imagen_salida = PhotoImage(file ='salida.png')
        self.imagen_movimiento = PhotoImage(file ='movimiento.png')
        self.imagen_creditos = PhotoImage(file ='creditos.png')
        
        
        self.logo = PhotoImage(file ='logo.png')
        self.imagen_uno = PhotoImage(file ='imagen_uno.png')
        self.imagen_dos= PhotoImage(file ='imagen_dos.png')
        self.imagen_tres= PhotoImage(file ='imagen_tres.png')
        self.dia = PhotoImage(file ='dia.png')
        self.noche= PhotoImage(file ='noche.png')
        
        self.bt_inicio = Button(self.frame_inicio, image= self.imagen_inicio, bg='black',activebackground='black', bd=0, command = self.menu_lateral)
        self.bt_inicio.grid(column=0, row=0, padx=5, pady=10)
        self.bt_cerrar = Button(self.frame_inicio, image= self.imagen_menu, bg='black',activebackground='black', bd=0, command = self.menu_lateral)
        self.bt_cerrar.grid(column=0, row=0, padx=5, pady=10)	

		#BOTONES Y ETIQUETAS DEL MENU LATERAL 
        Button(self.frame_menu, image= self.imagen_maestro, bg='black', activebackground='black', bd=0, command = self.pantalla_maestro).grid(column=0, row=1, pady=20,padx=10)
        Button(self.frame_menu, image= self.imagen_entrada, bg='black',activebackground='black', bd=0, command =self.pantalla_entrada).grid(column=0, row=2, pady=20,padx=10)
        Button(self.frame_menu, image= self.imagen_editar, bg= 'black',activebackground='black', bd=0, command = self.pantalla_editar).grid(column=0, row=3, pady=20,padx=10)
        Button(self.frame_menu, image= self.imagen_salida, bg= 'black',activebackground='black', bd=0, command = self.pantalla_salida).grid(column=0, row=4, pady=20,padx=10)		
        Button(self.frame_menu, image= self.imagen_movimiento, bg= 'black',activebackground='black', bd=0, command = self.pantalla_movimientos).grid(column=0, row=5, pady=20,padx=10)
        Button(self.frame_menu, image= self.imagen_creditos, bg= 'black',activebackground='black', bd=0, command = self.pantalla_creditos).grid(column=0, row=6, pady=20,padx=10)
         
		# se cambio base->Maestro, Registrar -> entrada, actualizar ->salida, eliminar -> Modificar, ajustes ->creditos
        Label(self.frame_menu, text= 'Maestro', bg= 'black', fg= '#B0E0E6', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=1, pady=20, padx=2)
        Label(self.frame_menu, text= 'Entrada', bg= 'black', fg= '#B0E0E6', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=2, pady=20, padx=2)
        Label(self.frame_menu, text= 'Editar', bg= 'black', fg= '#B0E0E6', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=3, pady=20, padx=2)
        Label(self.frame_menu, text= 'Salida', bg= 'black', fg= '#B0E0E6', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=4, pady=20, padx=2)	 
        Label(self.frame_menu, text= 'Movimientos', bg= 'black', fg= '#B0E0E6', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=5, pady=20, padx=2)
        Label(self.frame_menu, text= 'Creditos', bg= 'black', fg= '#B0E0E6', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=6, pady=20, padx=2)
        
		#############################  CREAR  PAGINAS  ##############################
        estilo_paginas = ttk.Style()
        estilo_paginas.configure("TNotebook", background='black', foreground='black', padding=0, borderwidth=0)
        estilo_paginas.theme_use('default')
        estilo_paginas.configure("TNotebook", background='black', borderwidth=0)
        estilo_paginas.configure("TNotebook.Tab", background="black", borderwidth=0)
        estilo_paginas.map("TNotebook", background=[("selected", 'black')])
        estilo_paginas.map("TNotebook.Tab", background=[("selected", 'black')], foreground=[("selected", 'black')]);

		#CREACCION DE LAS PAGINAS 
        self.paginas = ttk.Notebook(self.frame_principal , style= 'TNotebook') #, style = 'TNotebook'
        self.paginas.grid(column=0,row=0, sticky='nsew')
        self.frame_uno = Frame(self.paginas, bg='#FFEFD5')
        self.frame_dos = Frame(self.paginas, bg='white')
        self.frame_tres = Frame(self.paginas, bg='white')
        self.frame_cuatro = Frame(self.paginas, bg='white')
        self.frame_cinco = Frame(self.paginas, bg='white')
        self.frame_seis = Frame(self.paginas, bg='white')
        self.frame_siete = Frame(self.paginas, bg='white')
        self.paginas.add(self.frame_uno)
        self.paginas.add(self.frame_dos)
        self.paginas.add(self.frame_tres)
        self.paginas.add(self.frame_cuatro)
        self.paginas.add(self.frame_cinco)
        self.paginas.add(self.frame_seis)
        self.paginas.add(self.frame_siete)

		##############################         PAGINAS       #############################################

		######################## FRAME TITULO #################
        self.titulo = Label(self.frame_top,text= 'BIENVENID@ A HUACARIZ S.A.C.', bg='black', fg= 'white', font= ('Imprint MT Shadow', 15, 'bold'))
        self.titulo.pack(expand=1)

		######################## VENTANA PRINCIPAL #################

        Label(self.frame_uno, text= 'GRUPO 1', bg='#FFEFD5', fg= 'black', font= ('Freehand521 BT', 20, 'bold')).pack(expand=0)
        Label(self.frame_uno ,image= self.logo, bg='#FFEFD5').pack(expand=0.5)


		######################## MOSTRAR TODOS LOS PRODUCTOS DE LA BASE DE DATOS #################
        Label(self.frame_dos, text= 'Maestro de Productos', bg='white', fg= '#191970', font= ('Comic Sans MS', 12, 'bold')).grid(column =0, row=0)
        Button(self.frame_dos, text='ACTUALIZAR',fg='black' ,font = ('Arial', 11,'bold'), command= self.datos_totales, bg = '#F0E68C', bd = 2, borderwidth=2).grid(column=1, row=0, pady=5)
        
		#ESTILO DE LAS TABLAS DE DATOS TREEVIEW
        estilo_tabla = ttk.Style()
        estilo_tabla.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black',  background='white')  #, fieldbackground='yellow'
        estilo_tabla.map('Treeview',background=[('selected', '#B0E0E6')], foreground=[('selected','black')] )		
        estilo_tabla.configure('Heading',background = 'white', foreground='navy',padding=3, font= ('Arial', 10, 'bold'))
        estilo_tabla.configure('Item',foreground = 'white', focuscolor ='#B0E0E6')
        estilo_tabla.configure('TScrollbar', arrowcolor = '#B0E0E6',bordercolor  ='black', troughcolor= '#B0E0E6',background ='white')
        

		#TABLA UNO 
        self.frame_tabla_uno = Frame(self.frame_dos, bg= 'gray90')
        self.frame_tabla_uno.grid(columnspan=3, row=2, sticky='nsew')		
        self.tabla_uno = ttk.Treeview(self.frame_tabla_uno) 
        self.tabla_uno.grid(column=0, row=0, sticky='nsew')
        ladox = ttk.Scrollbar(self.frame_tabla_uno, orient = 'horizontal', command= self.tabla_uno.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = ttk.Scrollbar(self.frame_tabla_uno, orient ='vertical', command = self.tabla_uno.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla_uno.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
        self.tabla_uno['columns'] = ('Descripcion', 'Detalle', 'Unidad', 'Cantidad', 'FecPro', 'Lote', 'FecVen', 'Costouni')
        self.tabla_uno.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla_uno.column('Descripcion', minwidth=100, width=180 , anchor='center')
        self.tabla_uno.column('Detalle', minwidth=100, width=120, anchor='center' )
        self.tabla_uno.column('Unidad', minwidth=100, width=120 , anchor='center')
        self.tabla_uno.column('Cantidad', minwidth=100, width=80, anchor='center')
        self.tabla_uno.column('FecPro', minwidth=100, width=80, anchor='center')
        self.tabla_uno.column('Lote', minwidth=100, width=80, anchor='center')
        self.tabla_uno.column('FecVen', minwidth=100, width=80, anchor='center')
        self.tabla_uno.column('Costouni', minwidth=100, width=80, anchor='center')

        self.tabla_uno.heading('#0', text='Codpro', anchor ='center')
        self.tabla_uno.heading('Descripcion', text='Descripcion', anchor ='center')
        self.tabla_uno.heading('Detalle', text='Detalle', anchor ='center')
        self.tabla_uno.heading('Unidad', text='Unidad', anchor ='center')
        self.tabla_uno.heading('Cantidad', text='Cantidad', anchor ='center')
        self.tabla_uno.heading('FecPro', text='FecPro', anchor ='center')
        self.tabla_uno.heading('Lote', text='Lote', anchor ='center')
        self.tabla_uno.heading('FecVen', text='FecVen', anchor ='center')
        self.tabla_uno.heading('Costouni', text='Costouni', anchor ='center')
        self.tabla_uno.bind("<<TreeviewSelect>>", self.obtener_fila) 

		######################## REGISTRAR  NUEVOS PRODUCTOS #################
        Label(self.frame_tres, text = 'Agregar Nuevo Producto',fg='navy', bg ='white', font=('Kaufmann BT',24,'bold')).grid(columnspan=2, column=0,row=0, pady=5)
        Label(self.frame_tres, text = 'Codpro',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=1, pady=15, padx=5)
        Label(self.frame_tres, text = 'Descripcion',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=10)
        Label(self.frame_tres, text = 'Detalle',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=10)
        Label(self.frame_tres, text = 'Unidad', fg='navy',bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=10)
        Label(self.frame_tres, text = 'Cantidad',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=10)  ##E65561
        Label(self.frame_tres, text = 'FecPro',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=6, pady=10)
        Label(self.frame_tres, text = 'Lote',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=7, pady=10)
        Label(self.frame_tres, text = 'FecVen',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=8, pady=10)
        Label(self.frame_tres, text = 'Costouni',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=9, pady=10)
        Label(self.frame_tres, text = 'NumMov',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=10, pady=10)
        
        Entry(self.frame_tres, textvariable=self.codpro , font=('Comic Sans MS', 12),highlightbackground = "#0000CD", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=1)
        Entry(self.frame_tres, textvariable=self.descripcion , font=('Comic Sans MS', 12),highlightbackground = "#0000CD", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=2)
        Entry(self.frame_tres, textvariable=self.detalle , font=('Comic Sans MS', 12),highlightbackground = "#0000CD", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=3)
        Entry(self.frame_tres, textvariable=self.unidad , font=('Comic Sans MS', 12),highlightbackground = "#0000CD", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=4)
        Entry(self.frame_tres, textvariable=self.cantidad , font=('Comic Sans MS', 12),highlightbackground = "#0000CD", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=5)
        Entry(self.frame_tres, textvariable=self.fecpro , font=('Comic Sans MS', 12),highlightbackground = "#0000CD", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=6)
        Entry(self.frame_tres, textvariable=self.lote , font=('Comic Sans MS', 12),highlightbackground = "#0000CD", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=7)
        Entry(self.frame_tres, textvariable=self.fecven , font=('Comic Sans MS', 12),highlightbackground = "#0000CD", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=8)
        Entry(self.frame_tres, textvariable=self.costouni , font=('Comic Sans MS', 12),highlightbackground = "#0000CD", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=9)
        Entry(self.frame_tres, textvariable=self.nummov , font=('Comic Sans MS', 12),highlightbackground = "#0000CD", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=10)
        
        Button(self.frame_tres, command= self.agregar_datos , text='AGREGAR', font=('Arial',16,'bold'), bg='#F0E68C').grid(column=3,row=6, pady=10, padx=4)
        Label(self.frame_tres, image= self.imagen_uno, bg= 'white').grid(column= 3, rowspan= 5, row = 0, padx= 50)
        self.aviso_guardado = Label(self.frame_tres, bg= 'white', font=('Comic Sans MS', 12), fg='black')
        self.aviso_guardado.grid(columnspan= 2 , column =0, row = 11, padx= 5)
        
        		########################   MODIFICACION DE PRODUCTOS   #################
        Label(self.frame_cuatro, text = 'Modifica datos del Producto',fg='navy', bg ='white', font=('Kaufmann BT',24,'bold')).grid(columnspan=4, row=0)		
        Label(self.frame_cuatro, text = 'Ingrese el código del producto a editar',fg='black', bg ='white', font=('Rockwell',12)).grid(columnspan=2,row=1)
        Entry(self.frame_cuatro, textvariable= self.buscar_actualiza , font=('Comic Sans MS', 12), highlightbackground = "#66CDAA", width=12, highlightthickness=5).grid(column=2,row=1, padx=5)
        Button(self.frame_cuatro, command= self.actualizar_datos, text='BUSCAR', font=('Arial',12,'bold'), bg='#F0E68C').grid(column=3,row=1, pady=5, padx=15)
        self.aviso_actualizado = Label(self.frame_cuatro, fg='black', bg ='white', font=('Arial',12,'bold'))
        self.aviso_actualizado.grid(columnspan= 2, row=11, pady=10, padx=5)
        
        Label(self.frame_cuatro, text = 'Codpro',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=10, padx=10)
        Label(self.frame_cuatro, text = 'Descripcion',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=10)
        Label(self.frame_cuatro, text = 'Detalle',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=10)
        Label(self.frame_cuatro, text = 'Unidad', fg='navy',bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=10)
        Label(self.frame_cuatro, text = 'Cantidad',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=6, pady=10)  ##E65561
        Label(self.frame_cuatro, text = 'FecPro',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=7, pady=10)
        Label(self.frame_cuatro, text = 'Lote',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=8, pady=10)
        Label(self.frame_cuatro, text = 'FecVen',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=9, pady=10)
        Label(self.frame_cuatro, text = 'Costouni',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=10, pady=10)
        
        Entry(self.frame_cuatro, textvariable=self.codpro , font=('Comic Sans MS', 12), highlightbackground = "#0000CD", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=2)
        Entry(self.frame_cuatro, textvariable=self.descripcion , font=('Comic Sans MS', 12), highlightbackground = "#0000CD", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=3)
        Entry(self.frame_cuatro, textvariable=self.detalle , font=('Comic Sans MS', 12), highlightbackground = "#0000CD", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=4)
        Entry(self.frame_cuatro, textvariable=self.unidad , font=('Comic Sans MS', 12), highlightbackground = "#0000CD", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=5)
        Entry(self.frame_cuatro, textvariable=self.cantidad , font=('Comic Sans MS', 12), highlightbackground = "#0000CD", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=6)
        Entry(self.frame_cuatro, textvariable=self.fecpro , font=('Comic Sans MS', 12), highlightbackground = "#0000CD", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=7)
        Entry(self.frame_cuatro, textvariable=self.lote , font=('Comic Sans MS', 12), highlightbackground = "#0000CD", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=8)
        Entry(self.frame_cuatro, textvariable=self.fecven , font=('Comic Sans MS', 12), highlightbackground = "#0000CD", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=9)
        Entry(self.frame_cuatro, textvariable=self.costouni , font=('Comic Sans MS', 12), highlightbackground = "#0000CD", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=10)
        
        Button(self.frame_cuatro,command= self.actualizar_tabla, text='Modificar', font=('Arial',16,'bold'), bg='#F0E68C').grid(column=2, columnspan= 2 ,row=7, pady=2)
        Label(self.frame_cuatro, image= self.imagen_dos, bg='white').grid(column= 2,columnspan= 2, rowspan= 5, row = 2, padx=2)
        
        		######################## SALIDA DE PRODUCTOS #################
        Label(self.frame_cinco, text = 'Busca y Despacha',fg='navy', bg ='white', font=('Kaufmann BT',24,'bold')).grid(columnspan= 4,  row=0,sticky='nsew',padx=2)
        Entry(self.frame_cinco, textvariable= self.buscar , font=('Comic Sans MS', 12),highlightbackground = "#0000CD", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=0,row=1,sticky='nsew', padx=2)
        Button(self.frame_cinco,command = self.buscar_codpro, text='BUSCAR POR CÓDIGO', font=('Arial',8,'bold'), bg='#F0E68C').grid(column = 1, row=1, sticky='nsew', padx=2)		
        self.indica_busqueda = Label(self.frame_cinco, width= 15,text = '',fg='purple', bg ='white', font=('Arial',12,'bold'))
        self.indica_busqueda.grid(column = 3,  row=1,padx=2)
        
        Label(self.frame_cinco, text = 'Codpro',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=10, padx=10)
        Label(self.frame_cinco, text = 'Descripcion',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=10)
        Label(self.frame_cinco, text = 'Detalle',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=10)
        Label(self.frame_cinco, text = 'Unidad', fg='navy',bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=10)
        Label(self.frame_cinco, text = 'Cantidad',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=6, pady=10)  ##E65561
        Label(self.frame_cinco, text = 'FecVen',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=7, pady=10)
        Label(self.frame_cinco, text = 'Costouni',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=8, pady=10)
        Label(self.frame_cinco, text = 'NumMov',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=9, pady=10)
        
        Entry(self.frame_cinco, textvariable=self.codpro , font=('Comic Sans MS', 12), highlightbackground = "#778899", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=2)
        Entry(self.frame_cinco, textvariable=self.descripcion , font=('Comic Sans MS', 12), highlightbackground = "#778899", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=3)
        Entry(self.frame_cinco, textvariable=self.detalle , font=('Comic Sans MS', 12), highlightbackground = "#778899", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=4)
        Entry(self.frame_cinco, textvariable=self.unidad , font=('Comic Sans MS', 12), highlightbackground = "#778899", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=5)
        Entry(self.frame_cinco, textvariable=self.cantidad , font=('Comic Sans MS', 12), highlightbackground = "#778899", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=6)
        Entry(self.frame_cinco, textvariable=self.fecven , font=('Comic Sans MS', 12), highlightbackground = "#778899", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=7)
        Entry(self.frame_cinco, textvariable=self.costouni , font=('Comic Sans MS', 12), highlightbackground = "#778899", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=8)
        Entry(self.frame_cinco, textvariable=self.nummov , font=('Comic Sans MS', 12), highlightbackground = "#778899", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=1,row=9)
        
        Entry(self.frame_cinco, textvariable = self.amount , font=('Comic Sans MS', 12), highlightbackground = "#FFD700", highlightcolor= "#66CDAA", highlightthickness=5).grid(column=2,row=7, pady = 10)
        Label(self.frame_cinco, text = 'Ingrese La cantidad a despachar' ,fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=2,row=8, pady=10)
        
        Button(self.frame_cinco, command= self.actualizar_cantidad, text='Despachar', font=('Arial',16,'bold'), bg='#F0E68C').grid(column=2 ,row=9, pady=10)
        Label(self.frame_cinco, image= self.imagen_tres, bg='white').grid(column= 2,columnspan= 1, rowspan= 5, row = 2, padx=2)
        self.aviso_actualizado = Label(self.frame_cinco, fg='black', bg ='white', font=('Arial',12,'bold'))
        self.aviso_actualizado.grid(column = 2, row=10, pady=10, padx=2)
       
        
                                    ######################## MOSTRAR TODOS LOS PRODUCTOS DE LA BASE DE DATOS MOVIMIENTOS #################
        Label(self.frame_siete, text= 'Movimiento de Productos', bg='white', fg= '#191970', font= ('Comic Sans MS', 12, 'bold')).grid(column =0, row=0)
        Button(self.frame_siete, text='ACTUALIZAR',fg='black' ,font = ('Arial', 11,'bold'), command= self.datos_movidos, bg = '#F0E68C', bd = 2, borderwidth=2).grid(column=1, row=0, pady=5)


		#ESTILO DE LAS TABLAS DE DATOS TREEVIEW
        estilo_tabla = ttk.Style()
        estilo_tabla.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black',  background='white')  #, fieldbackground='yellow'
        estilo_tabla.map('Treeview',background=[('selected', '#B0E0E6')], foreground=[('selected','black')] )		
        estilo_tabla.configure('Heading',background = 'white', foreground='navy',padding=3, font= ('Arial', 10, 'bold'))
        estilo_tabla.configure('Item',foreground = 'white', focuscolor ='#B0E0E6')
        estilo_tabla.configure('TScrollbar', arrowcolor = '#B0E0E6',bordercolor  ='black', troughcolor= '#B0E0E6',background ='white')
        

		#TABLA DOS 
        self.frame_tabla_dos = Frame(self.frame_siete, bg= 'gray90')
        self.frame_tabla_dos.grid(columnspan=3, row=2, sticky='nsew')		
        self.tabla_dos = ttk.Treeview(self.frame_tabla_dos) 
        self.tabla_dos.grid(column=0, row=0, sticky='nsew')
        ladox = ttk.Scrollbar(self.frame_tabla_dos, orient = 'horizontal', command= self.tabla_dos.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = ttk.Scrollbar(self.frame_tabla_dos, orient ='vertical', command = self.tabla_dos.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla_dos.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
        self.tabla_dos['columns'] = ('TipMov', 'NumMov', 'FecMov', 'Descripcion', 'Detalle', 'Unidad', 'Cantidad', 'FecPro', 'Lote', 'FecVen', 'Costouni')
        self.tabla_dos.column('#0', minwidth=100, width=80, anchor='center')
        self.tabla_dos.column('TipMov', minwidth=100, width=80 , anchor='center')
        self.tabla_dos.column('NumMov', minwidth=100, width=80 , anchor='center') 
        self.tabla_dos.column('FecMov', minwidth=100, width=80 , anchor='center')
        self.tabla_dos.column('Descripcion', minwidth=100, width=180 , anchor='center')
        self.tabla_dos.column('Detalle', minwidth=100, width=120, anchor='center' )
        self.tabla_dos.column('Unidad', minwidth=100, width=120 , anchor='center')
        self.tabla_dos.column('Cantidad', minwidth=100, width=80, anchor='center')
        self.tabla_dos.column('FecPro', minwidth=100, width=80, anchor='center')
        self.tabla_dos.column('Lote', minwidth=100, width=80, anchor='center')
        self.tabla_dos.column('FecVen', minwidth=100, width=80, anchor='center')
        self.tabla_dos.column('Costouni', minwidth=100, width=80, anchor='center')

        self.tabla_dos.heading('#0', text='Codpro', anchor ='center')
        self.tabla_dos.heading('TipMov', text='TipMov', anchor ='center')
        self.tabla_dos.heading('NumMov', text='NumMov', anchor ='center')
        self.tabla_dos.heading('FecMov', text='FecMov', anchor ='center')
        self.tabla_dos.heading('Descripcion', text='Descripcion', anchor ='center')
        self.tabla_dos.heading('Detalle', text='Detalle', anchor ='center')
        self.tabla_dos.heading('Unidad', text='Unidad', anchor ='center')
        self.tabla_dos.heading('Cantidad', text='Cantidad', anchor ='center')
        self.tabla_dos.heading('FecPro', text='FecPro', anchor ='center')
        self.tabla_dos.heading('Lote', text='Lote', anchor ='center')
        self.tabla_dos.heading('FecVen', text='FecVen', anchor ='center')
        self.tabla_dos.heading('Costouni', text='Costouni', anchor ='center')
        self.tabla_dos.bind("<<TreeviewSelect>>", self.obtener_fila)
        
        
        
        		######################## CREDITOS #################
        self.text_ajustes = Label(self.frame_seis, text = 'Créditos para este equipaso conformado por:',fg='gold', bg ='white', font=('Kaufmann BT',28,'bold'))
        self.text_ajustes.pack(expand=1)
        self.bt_color = Button(self.frame_seis, image = self.noche , command= self.cambiar_color, bg = 'white', bd=0, activebackground='white')
        self.bt_color.pack(expand=1)
        self.texto = Label(self.frame_seis, text = 'Anthony Jaimes Cardenas \n Brigitte Saldias \n Isis Vera \n Valeria Castañeda \n Maricielo Delgado',fg='white', bg ='white', font=('Kaufmann BT',24))
        self.texto.pack(expand=1)
        


    def datos_totales(self):
        datos = self.base_datos.mostrar_productos()
        self.tabla_uno.delete(*self.tabla_uno.get_children())
        i = -1
        for dato in datos:
            i= i+1
            self.tabla_uno.insert('',i, text = datos[i][1:2], values=datos[i][2:10])

    def datos_movidos(self):
        datas = self.base_datos.mostrar_movimientos()
        self.tabla_dos.delete(*self.tabla_dos.get_children())
        i = -1
        for dato in datas:
            i= i+1
            self.tabla_dos.insert('',i, text = datas[i][1:2], values=datas[i][2:13])
 

    def agregar_datos(self):
        codpro = self.codpro.get()
        tipmov = "EntradaProd"
        nummov = self.nummov.get()
        fecmov = self.fecmov
        descripcion = self.descripcion.get()
        detalle = self.detalle.get()
        unidad = self.unidad.get()
        cantidad = self.cantidad.get()
        fecpro = self.fecpro.get()
        lote = self.lote.get()
        fecven = self.fecven.get()
        costouni = self.costouni.get()
        datas = (tipmov, nummov, fecmov, descripcion, detalle, unidad, cantidad, fecpro, lote, fecven, costouni)
        datos = (descripcion, detalle, unidad, cantidad, fecpro, lote, fecven, costouni)
        
        if codpro and nummov and descripcion and detalle and unidad and cantidad and fecpro and lote and fecven and costouni !='':
            self.tabla_uno.insert('',0, text = codpro, values=datos) 
            self.base_datos.inserta_producto(codpro, descripcion, detalle, unidad, cantidad, fecpro, lote, fecven, costouni)
            self.tabla_dos.insert('',0, text = codpro, values=datas)
            self.base_datos.inserta_movimiento(codpro,tipmov, nummov, fecmov, descripcion, detalle, unidad, cantidad, fecpro, lote, fecven, costouni)
            
            self.aviso_guardado['text'] = 'Registro Exitoso'
            self.limpiar_datos()
            self.aviso_guardado.update()						
            time.sleep(1) 
            self.aviso_guardado['text'] = ''						
        else:
            self.aviso_guardado['text'] = 'Ingrese todos los datos'
            self.aviso_guardado.update()
            time.sleep(1) 
            self.aviso_guardado['text'] = ''
             
            
             
            #############EDITAR PRODUCTOS#################
    
    
    def actualizar_datos(self):
        dato = self.buscar_actualiza.get()
        dato = str("'" + dato + "'")
        codpro_buscado = self.base_datos.busca_producto(dato)

        if codpro_buscado == []:
            self.aviso_actualizado['text'] = 'No existe'			
            self.indica_busqueda.update()						
            time.sleep(1) 
            self.limpiar_datos()
            self.aviso_actualizado['text'] = ''
        else:
            i = -1
            for dato in codpro_buscado:
                i= i+1
                self.id.set(codpro_buscado[i][0])
                self.codpro.set(codpro_buscado[i][1])
                self.descripcion.set(codpro_buscado[i][2])
                self.detalle.set(codpro_buscado[i][3])
                self.unidad.set(codpro_buscado[i][4])
                self.cantidad.set(codpro_buscado[i][5])
                self.fecpro.set(codpro_buscado[i][6])
                self.lote.set(codpro_buscado[i][7])
                self.fecven.set(codpro_buscado[i][8])
                self.costouni.set(codpro_buscado[i][9])
    

    def actualizar_tabla(self):	
        Id = self.id.get() 	
        codpro = self.codpro.get()
        descripcion = self.descripcion.get()
        detalle = self.detalle.get()
        unidad = self.unidad.get()
        cantidad = self.cantidad.get()
        fecpro = self.fecpro.get()
        lote = self.lote.get()
        fecven = self.fecven.get()
        costouni = self.costouni.get()
        self.base_datos.actualiza_productos(Id, codpro, descripcion, detalle, unidad, cantidad, fecpro, lote, fecven, costouni)	
        self.aviso_actualizado['text'] = 'Datos Actualizados'			
        self.indica_busqueda.update()						
        time.sleep(1) 
        self.aviso_actualizado['text'] = ''
        self.limpiar_datos()
        self.buscar_actualiza.set('')
				
    def limpiar_datos(self):
        self.codpro.set('')
        self.nummov.set('')
        self.descripcion.set('')
        self.detalle.set('')
        self.unidad.set('')
        self.cantidad.set('')
        self.fecpro.set('')
        self.lote.set('')
        self.fecven.set('')
        self.costouni.set('')
        self.amount.set('')

    def buscar_codpro(self):
        codpro_producto = self.buscar.get()
        codpro_producto = str("'" + codpro_producto + "'")
        codpro_buscado = self.base_datos.busca_producto(codpro_producto)
        
        if codpro_buscado == []:
            self.indica_busqueda['text'] = 'No existe'
            self.indica_busqueda.update()						
            time.sleep(1) 
            self.indica_busqueda['text'] =''

        else:
            i = -1
            for dato in codpro_buscado:
                i= i+1
                self.id.set(codpro_buscado[i][0])
                self.codpro.set(codpro_buscado[i][1])
                self.descripcion.set(codpro_buscado[i][2])
                self.detalle.set(codpro_buscado[i][3])
                self.unidad.set(codpro_buscado[i][4])
                self.cantidad.set(codpro_buscado[i][5])
                self.fecpro.set(codpro_buscado[i][6])
                self.lote.set(codpro_buscado[i][7])
                self.fecven.set(codpro_buscado[i][8])
                self.costouni.set(codpro_buscado[i][9])

    def actualizar_cantidad(self):	
        Id = self.id.get() 	
        codpro = self.codpro.get()
        tipmov = "SalidaVen"
        nummov = self.nummov.get()
        fecmov = self.fecmov
        descripcion = self.descripcion.get()
        detalle = self.detalle.get()
        unidad = self.unidad.get()
        cantidad = str(int(self.cantidad.get())-int(self.amount.get()))
        amount = self.amount.get()
        fecpro = self.fecpro.get()
        lote = self.lote.get()
        fecven = self.fecven.get()
        costouni = self.costouni.get()
        if int(cantidad) < 0 :
            
            self.aviso_actualizado['text'] = 'NOOOOOOOOOO Despachado'		
        else:
        
            datas = (tipmov, nummov, fecmov, descripcion, detalle, unidad, cantidad,amount, fecpro, lote, fecven, costouni)
            
            self.base_datos.actualiza_productos(Id, codpro, descripcion, detalle, unidad, cantidad, fecpro, lote, fecven, costouni)	
            
            self.tabla_dos.insert('',0, text = codpro, values=datas)
            self.base_datos.inserta_movimiento(codpro,tipmov, nummov, fecmov, descripcion, detalle, unidad, amount, fecpro, lote, fecven, costouni)
                
            self.aviso_actualizado['text'] = 'Producto Despachado'			
            self.indica_busqueda.update()						
            time.sleep(1) 
            self.aviso_actualizado['text'] = ''
            self.limpiar_datos()
            self.buscar.set('')
        
        
    def obtener_fila(self, event):
        current_item = self.tabla_uno.focus()

if __name__ == "__main__":
	ventana = Tk()
	ventana.title('Huacariz S.A.C.')
	ventana.minsize(height= 475, width=795)
	ventana.geometry('1000x500+180+80')
	ventana.call('wm', 'iconphoto', ventana._w, PhotoImage(file='logo.png'))	
	app = Ventana(ventana)
	app.mainloop()


