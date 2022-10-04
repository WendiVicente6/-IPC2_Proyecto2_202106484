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


        
 




class Clientes():         #---------------------------------------------------------------TRATAR COMO COLA

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