from ast import Break, Return
import os
import string
from typing_extensions import Self




class Nodo():
    def __init__ (self,dato=None,sig=None):
        self.dato=dato
        self.sig=sig

class Lista():
    def __init__(self):
        self.head=None
    def AgregarInicio(self,dato):
        self.head=Nodo(dato=dato,sig=self.head)

    def AgregarFinal(self,dato):
        if not self.head:
            self.head=Nodo(dato=dato)
            return
        actual=self.head
        while actual.sig:
            actual=actual.sig 
        actual.sig =Nodo(dato=dato)
    
    def RetornaUltimoNodo(self):
        temporal=self.head 
        while(temporal.sig is not None):
            temporal=temporal.sig 
        return temporal.dato

    def ImprimirLista(self,especifico):
        nodo = self.head
        while nodo != None:
            print(getattr(nodo.dato,especifico))
            nodo = nodo.sig

    def ParaSeleccionar(self,especifico1,especifico2):
        nodo = self.head
        while nodo != None:
            print(getattr(nodo.dato,especifico1),getattr(nodo.dato,especifico2))
            nodo = nodo.sig
  
    def Limpiar(self):
        self.head=None
        print("YA SE LIMPIO")
   
    def getConfiguracion(self,idempresa,idpunto):
        tmp=self.head
        while tmp is not None:
            if tmp.dato.ideEmpresaConfiguracion==idempresa and tmp.dato.idePuntoDEAtencionConfiguracion==idpunto:
                return tmp
            tmp=tmp.sig
        return None

    def MeterCliente(self,idempresa,idpunto):
            contar=0
            dpi=input("DPI: ")
            nombre=input("Nombre: ")
            tmp=self.head
            while tmp is not None:
                if tmp.dato.ideEmpresaConfiguracion.strip()==idempresa:
                    if tmp.dato.idePuntoDEAtencionConfiguracion.strip()==idpunto:
                        idtrans=input("Ingrese ID de transaccion a realizar: ")
                        cantrans=input("Ingrese Cantidad de transaccion: ")
                        idconfig=self.getConfiguracion(idempresa,idpunto)
                        ClienteNuevo=Clientes(dpi,nombre)
                        idconfig.dato.FilaClientes.AgregarFinal(ClienteNuevo)

                        Transacciones=TransaccionesCliente(idtrans,cantrans)
                        ClienteNuevo.transaccionesARealizar.AgregarFinal(Transacciones)

                        return

                    tmp=tmp.sig
                tmp=tmp.sig
    def MostrarActivos(self,idempresa,idpunto):
        tmp=self.head
        
        while tmp is not None:
            if tmp.dato.ideEmpresaConfiguracion.strip()==idempresa:
                if tmp.dato.idePuntoDEAtencionConfiguracion.strip()==idpunto:
                    tmp2=tmp.dato.EscritoriosActicos.head
                    
                    while tmp2 is not None:
                        print("ESCRITORIO: ",tmp2.dato.ideEscritorioActivo)
                        tmp2=tmp2.sig
                    return
                tmp=tmp.sig
            tmp=tmp.sig
    def ClientesFaltantes(self,idempresa,idpunto):
        tmp=self.head
        
        while tmp is not None:
            if tmp.dato.ideEmpresaConfiguracion.strip()==idempresa:
                if tmp.dato.idePuntoDEAtencionConfiguracion.strip()==idpunto:
                    tmp2=tmp.dato.FilaClientes.head
                    
                    while tmp2 is not None:
                        print("Clientes: ",tmp2.dato.nombreCliente)
                        tmp2=tmp2.sig
                    
                    return
                
                tmp=tmp.sig
            tmp=tmp.sig

    def DesactivarEscritorio(self,idempresa,idpunto):
        tmp=self.head
        
        while tmp is not None:
            if tmp.dato.ideEmpresaConfiguracion.strip()==idempresa:
                if tmp.dato.idePuntoDEAtencionConfiguracion.strip()==idpunto:
                    tmp2=tmp.dato.EscritoriosActicos

                    while tmp2 is not None:
                        escritorio=tmp2.head.dato.ideEscritorioActivo
                        borrar=tmp2.head
                        tmp2.head=tmp2.head.sig
                        borrar=None                         
                        print("El ",escritorio," fue desactivado")
                        break
                    return
                tmp=tmp.sig
            tmp=tmp.sig

    def ActivarEscritorio(self,idempresa,idpunto,idescritorio):
        contar=0
        tmp=self.head
        while tmp is not None:
            if tmp.dato.ideEmpresaConfiguracion.strip()==idempresa:
                if tmp.dato.idePuntoDEAtencionConfiguracion.strip()==idpunto:
                    idconfig=self.getConfiguracion(idempresa,idpunto)
                    tempEscritoriosActivos=EscritorioActivo(idescritorio)
                    idconfig.dato.EscritoriosActicos.AgregarInicio(tempEscritoriosActivos)
                    return

                tmp=tmp.sig
            tmp=tmp.sig

    def EscritoriosActivos(self,idempresa,idpunto):
        contar=0
        tmp=self.head
        listaactivos=[]
        while tmp is not None:
            if tmp.dato.ideEmpresaConfiguracion.strip()==idempresa:
                if tmp.dato.idePuntoDEAtencionConfiguracion.strip()==idpunto:
                    tmp2=tmp.dato.EscritoriosActicos.head
                    while tmp2!=None:
                        activos=tmp2.dato.ideEscritorioActivo
                        listaactivos.append(activos)
                        contar+=1
                        tmp2=tmp2.sig
                    print("Activos: ",contar)
                    return listaactivos
                    
                tmp=tmp.sig
            tmp=tmp.sig
    def Atender(self,idempresa,idpunto):
        contar=0
        tmp=self.head
        listaactivos=[]
        while tmp is not None:
            if tmp.dato.ideEmpresaConfiguracion.strip()==idempresa:
                if tmp.dato.idePuntoDEAtencionConfiguracion.strip()==idpunto:
                    tmp2=tmp.dato.FilaClientes
                    while tmp2!=None:
                        if tmp2.head!=None:
                            cliente=tmp2.head.dato.nombreCliente
                            borrar=tmp2.head
                            tmp2.head=tmp2.head.sig
                            borrar=None
                            print("El cliente: ",cliente," fue atendido")
                            break
                        else:
                            print("Ya no hay clientes")
                            break
                    return                 
                tmp=tmp.sig
            tmp=tmp.sig
    def ClientesEspera(self,idempresa,idpunto):
        tmp=self.head
        contar=0
        while tmp is not None:
            if tmp.dato.ideEmpresaConfiguracion.strip()==idempresa:
                if tmp.dato.idePuntoDEAtencionConfiguracion.strip()==idpunto:
                    tmp2=tmp.dato.FilaClientes.head
                    while tmp2!=None:
                        activos=tmp2.dato.dpiCliente
                        #print(activos)
                        contar+=1
                        tmp2=tmp2.sig
       
                tmp=tmp.sig
                print("Clientes en espera: ",contar)
                break;
            tmp=tmp.sig
        return None
    
    def CantidadTransacciones(self,idempresa,idpunto):
        tmp=self.head
        contar=0
        transacciones=[]
        while tmp is not None:
            if tmp.dato.ideEmpresaConfiguracion.strip()==idempresa:
                if tmp.dato.idePuntoDEAtencionConfiguracion.strip()==idpunto:
                    tmp2=tmp.dato.FilaClientes.head
                    while tmp2!=None:
                        tmp3=tmp2.dato.transaccionesARealizar.head
                        while tmp3!=None:
                            transa=tmp3.dato.ideTransaccionARealizar
                            cantidad=tmp3.dato.nveces
                            #print(activos)
                            transacciones.append([transa,cantidad])
                            tmp3=tmp3.sig
                        tmp2=tmp2.sig
                    return transacciones
                    
                tmp=tmp.sig
                #return transa,cantidad
                break;
            tmp=tmp.sig
        return None

    def graficar(self,idempresa,idpunto):
        tmp=self.head
        cont = 0
        cadena = ""
        
        while tmp is not None:
            if tmp.dato.ideEmpresaConfiguracion.strip()==idempresa:
                if tmp.dato.idePuntoDEAtencionConfiguracion.strip()==idpunto:
                    tmp2=tmp.dato.FilaClientes.head
                    file = open('Cola.dot', 'w')
                    cadena = cadena + 'graph G { \n'
                    while tmp2 is not None:
                        tmp3=tmp2.dato.transaccionesARealizar.head
                        cadena = cadena + 'Node'+str(cont)+'[dir=both shape=box label=\"'+str(tmp2.dato.nombreCliente)+"\n"+str(tmp2.dato.dpiCliente)+"\n"
                        while tmp3!=None:
                            transa=tmp3.dato.ideTransaccionARealizar
                            cantidad=tmp3.dato.nveces
        
                            cadena=cadena+' '+str(transa)+" Cantidad: "+str(cantidad)+"\n"
                            tmp3=tmp3.sig
                        cadena=cadena+'\"];\n'
                        if(tmp2!=tmp.dato.FilaClientes.head):
                            cadena = cadena + 'Node'+str(cont-1)+' -- '+'Node'+str(cont)+';\n'
                        tmp2 = tmp2.sig
                        cont+=1
                    cadena = cadena + '}'
                    file.write(cadena)
                    file.close()
                    os.system('dot -Tpng Cola.dot -o Cola.png')
                    os.startfile("Cola.png")
                    return
                tmp=tmp.sig
            tmp=tmp.sig       

class Clientes(): 

    def __init__(self,dpiCliente,nombreCliente):
        self.dpiCliente=dpiCliente
        self.nombreCliente=nombreCliente
        self.transaccionesARealizar=Lista()



class TransaccionesCliente():
        def __init__(self,ideTransaccionARealizar,nveces):
            self.ideTransaccionARealizar=ideTransaccionARealizar
            self.nveces=nveces

class Configuracion():
    
    def __init__ (self,codigoConfiguracion,ideEmpresaConfiguracion,idePuntoDEAtencionConfiguracion):
        self.codigoConfiguracion=codigoConfiguracion
        self.ideEmpresaConfiguracion=ideEmpresaConfiguracion
        self.idePuntoDEAtencionConfiguracion=idePuntoDEAtencionConfiguracion
        self.EscritoriosActicos=Lista()
        self.FilaClientes=Lista()

class EscritorioActivo():

    def __init__(self,ideEscritorioActivo):
        self.ideEscritorioActivo=ideEscritorioActivo