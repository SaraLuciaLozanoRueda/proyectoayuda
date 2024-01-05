import funciones.corefile as cf
import os
clientes={
}
cliente={
    'cc':'00',
    'nombre':'',
    'apellidos':'',
    'telefono':[],
    'emailpersonal':'',
    'emailcorporativo':'',
    'edad':0 
}
telefono={
    'descripcion':'',
    'numero':'000'
}
cf.MY_DATABASE='data/clientes.json'
def NewCustomer():
    pass

def validarArchivoClientes():
    if(cf.checkFile()):
        print('ok')
        os.system('pause')
    else:
        cf.NewFile(clientes)