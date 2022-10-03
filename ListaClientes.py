import string

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



class Clientes():         #---------------------------------------------------------------TRATAR COMO COLA
    dpiCliente:int
    nombreCliente:string
    transaccionesARealizar:Lista
    def __init__(self,dpiCliente,nombreCliente):
        self.dpiCliente=dpiCliente
        self.nombreCliente=nombreCliente
        self.transaccionesARealizar=Lista()



class TransaccionesCliente():
        ideTransaccionARealizar:int
        nveces:int
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
    ideEscritorioActivo:int

    def __init__(self,ideEscritorioActivo):
        self.ideEscritorioActivo=ideEscritorioActivo