from tkinter import *
from tkinter import ttk
import base_datos

#Agregar algo estético

mysql = base_datos.BD()

ventana = Tk()
ventana.title('Mysql con tkinter')
ventana.geometry('600x500')

#Variables, StringVar() Nos permite compartir variables entre tkinter y python
nombre = StringVar()
correo = StringVar()
telefono = StringVar()

#Agregamos LableFrame
marco = LabelFrame(ventana, text = 'Tabla personas')
#tkinter toma como referencia el eje superior izquierdo para acomodar la pantalla
marco.place(x=50,y=50,width=500,height=400)
#Agregamos Label y textinput para nombre, correo y telefono
#El grid es como una cuadricula
lblNombre = Label(marco,text='Nombre: ', fg= 'green')
lblNombre.grid(column=0, row=0, padx=5, pady=5)
txtNombre = Entry(marco, textvariable=nombre)
txtNombre.grid(column=1, row=0)

lblCorreo = Label(marco,text='Correo: ', fg= 'green')
lblCorreo.grid(column=2, row=0, padx=5, pady=5)
txtCorreo = Entry(marco, textvariable=correo)
txtCorreo.grid(column=3, row=0)

lblTelefono = Label(marco,text='Teléfono: ', fg= 'green')
lblTelefono.grid(column=0, row=1, padx=5, pady=5)
txtTelefono = Entry(marco, textvariable=telefono)
txtTelefono.grid(column=1, row=1)

mensaje = Label(marco, text='Contenido de la tabla', fg= 'red')
mensaje.grid(column=0, row=2,columnspan=4)

#Le pasamos que se va a almacenar en marco
#Arbol de vistas (buscar imagen en google para saber que es un arbol de vistas)
tvPersonas = ttk.Treeview(marco)
tvPersonas.grid(column=0, row=3, columnspan=4)
tvPersonas['columns'] = ('Id','Nombre','Correo','Teléfono')
#Como la primer columna esta vacía la "eliminamos" o sea, le ponemos ancho de 0 para que no se vea
tvPersonas.column('#0', width=0, stretch=NO)
tvPersonas.column('Id', width=100, anchor=CENTER)
tvPersonas.column('Nombre', width=100, anchor=CENTER)
tvPersonas.column('Correo', width=100, anchor=CENTER)
tvPersonas.column('Teléfono', width=100, anchor=CENTER)
tvPersonas.heading('Id', text='Id',anchor=CENTER)
tvPersonas.heading('Nombre', text='Nombre',anchor=CENTER)
tvPersonas.heading('Correo', text='Correo',anchor=CENTER)
tvPersonas.heading('Teléfono', text='Teléfono',anchor=CENTER)

btnAgregar = Button(marco,text='Agregar',command=lambda:agregar())
btnAgregar.grid(column=0, row=4,pady=5)

btnAgregar = Button(marco,text='Actualizar',command=lambda:llenar_tabla())
btnAgregar.grid(column=1, row=4,pady=5)

btnAgregar = Button(marco,text='Eliminar',command=lambda:eliminar())
btnAgregar.grid(column=2, row=4,pady=5)

def validar():
    return len(nombre.get()) and len(correo.get()) and len(telefono.get())

def limpiar():
    nombre.set('')
    correo.set('')
    telefono.set('')

def  vaciar_tabla():
    filas = tvPersonas.get_children()
    for fila in filas:
        tvPersonas.delete(fila)

def llenar_tabla():
    vaciar_tabla()
    consulta = mysql.select('personas')
    for fila in consulta:
        id = fila[0]
        tvPersonas.insert('',END,text=id,values=fila)

def agregar():
    if validar():
        variables = nombre.get(), correo.get(), telefono.get()
        sql = 'insert from personas into (nombre,correo,telefono) values (%s,%s,%s)'
        mysql.agregar(sql)
        llenar_tabla()
        limpiar()
        
def actualizar():
    pass

def eliminar():
    #Esto no es para eliminar pero lo estamos haciendo aquí por algún motivo
    item_seleccionado = tvPersonas.focus()
    detalle = tvPersonas.item(item_seleccionado)
    id = detalle.get('values')[0]
    #print(id)
    if id > 0:
        sql = 'delete from personas where id = ' + str(id)
        mysql.eliminar(sql)
        llenar_tabla()

def llenar_tabla():
    pass

ventana.mainloop()

