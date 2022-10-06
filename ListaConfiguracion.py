from itertools import tee
import re

from ListaClientes import Lista

listaclientes=Lista()
class Company:
    def __init__(self,id=None, name=None, abbreviation=None):
        self.id = id;
        self.name = name;
        self.abbreviation = abbreviation;
        self.service_points = ListarObjetos();
        self.transactions = ListarObjetos();    
       
class Service_Point:
    def __init__(self,id=None,name=None,address=None):
        self.id = id;
        self.name = name;
        self.address = address;
        self.desks = ListarObjetos();
        
class Desk:
    def __init__(self,id=None,identification=None,manager=None):
        self.id = id;
        self.identification = identification;
        self.manager = manager;

class Transaction:
    def __init__(self,id=None,name=None,time=None):
        self.id = id;
        self.name = name;
        self.time = time;

class Node:        
    def __init__(self, object):
        self.object=object;
        self.next:Node = None;
        self.previous:Node = None;
        
class ListarObjetos:
    def __init__(self):
        self.first:Node = None;
        self.last:Node = None;
        self.size = 0;
        
    def Insert_End(self, object):
        nuevo = Node(object);
        
        if(self.size == 0):
            self.first = self.last = nuevo;
        else:
            self.last.next = nuevo;
            nuevo.previous = self.last;
            self.last = nuevo;
        self.size +=1;
    def Eliminar(self):
        tmp=self.first
        while tmp!=None:
            borrar=tmp
            tmp=tmp.next
            borrar=None
            self.size-=1
        #print("Ha sido borrados los datos de configuración ")
        

    def getEmpresa(self,empresa,punto):
        tmp=self.first
        
        
        while tmp is not None:
            if tmp.object.name.strip()==empresa:
                tmp2=tmp.object.service_points.first
                while tmp2 is not None:
                    if tmp2.object.name.strip()==punto:
                        return tmp,tmp2
                    tmp2=tmp2.next
                
            tmp=tmp.next
        return None
    def EscritoriosInactivos(self,empresa,punto,listactivos):
        tmp=self.first
        contar=0
       
        while tmp is not None:
            if tmp.object.id.strip()==empresa:
                tmp2=tmp.object.service_points.first
                while tmp2 is not None:
                    if tmp2.object.id.strip()==punto:
                        tmp3=tmp2.object.desks.first
                        while tmp3 is not None:
                            if tmp3.object.id.strip() in listactivos:
                                tmp3=tmp3.next
                            else:
                                inactivo=tmp3.object.id
                                contar+=1
                                
                                tmp3=tmp3.next
                        print("Inactivos: ",contar)
                        

                        #return tmp,tmp2
                    tmp2=tmp2.next
                
            tmp=tmp.next
        return None
    def ActivarInactivos(self,empresa,punto,listactivos,idescritorio):
        tmp=self.first
        contar=0

        while tmp is not None:
            if tmp.object.id.strip()==empresa:
                tmp2=tmp.object.service_points.first
                while tmp2 is not None:
                    if tmp2.object.id.strip()==punto:
                        tmp3=tmp2.object.desks.first
                        while tmp3 is not None:
                            if tmp3.object.id.strip() in listactivos:
                                tmp3=tmp3.next
                                
                            else:
                                if tmp3.object.id==idescritorio:
                                    escritorio=tmp3.object.id
                                tmp3=tmp3.next
                        

                        return listactivos
                    tmp2=tmp2.next
                
            tmp=tmp.next
        return None
               
    def DesactivarEscritorio(self,empresa,punto,listactivos,idescritorio):
        tmp=self.first
        contar=0
        listaactivar=[]
        
        
        while tmp is not None:
            if tmp.object.id.strip()==empresa:
                tmp2=tmp.object.service_points.first
                while tmp2 is not None:
                    if tmp2.object.id.strip()==punto:
                        tmp3=tmp2.object.desks.first

                        if idescritorio in listactivos:
                            print(listactivos)
                            while tmp3 is not None:
                                while tmp3.object.id==idescritorio:
                                    tmp3.object.id==None
                                    listactivos.remove(idescritorio)
                                    tmp3=tmp3.next
                                tmp3=tmp3.next
                            print(listactivos)

                      
                    tmp2=tmp2.next
                
            tmp=tmp.next
        return None
    def MostrarTransacciones(self,idempresa,idpunto):
        tmp=self.first
        
        while tmp is not None:
            if tmp.object.id.strip()==idempresa:
                tmp2=tmp.object.transactions.first
                
                while tmp2 is not None:
                    print("Id transacciones: ",tmp2.object.id, "Nombre Transacciones: ",tmp2.object.name)
                    tmp2=tmp2.next
                return
            tmp=tmp.next
    def CalcularTiempoPromedio(self,empresa,listatrans):
        tmp=self.first
        contar=0
        contarespera=0
        tiempopromedio=0
        tiempo=0
        timpopromedioespera=0
        minimoatencion=0
        maximoatencion=0
        listatiempo=[]

        while tmp is not None:
            if tmp.object.id.strip()==empresa:
                tmp2=tmp.object.transactions.first

                for element in listatrans:

                    while tmp2.object.id.strip()!=element[0]:
                        tmp2=tmp2.next
                        if tmp2==None:
                            tmp2=tmp.object.transactions.first

                    tiempo+=int(tmp2.object.time)*int(element[1])
                    listatiempo.append(int(tmp2.object.time))
                    maximoatencion=max(listatiempo)
                    minimoatencion=min(listatiempo)

                    contar+=int(element[1])
                    contarespera+=1
                    tiempopromedio=tiempo/contar
                    timpopromedioespera=tiempo/contarespera
                print("Tiempo Promedio atencion: ",tiempopromedio," minutos")   
                print("Tiempo Promedio de espera: ",timpopromedioespera," minutos")  
                print("Tiempo Maximo de Espera: ",tiempo, " minutos")
                print("Tiempo minimo de Espera: ",minimoatencion, " minutos")
                print("Tiempo maximo de atención: ",maximoatencion," minutos")
                print("Tiempo Minimo de atención: ",minimoatencion," minutos")          
                 
            tmp=tmp.next
        return None
   
    def Show(self):
        temporal = self.first;
        if (self.size != 0):
            if temporal==None:
                return
            
            if (type(temporal.object) == Company):
                print("EMPRESA"+"="*65);
                while (temporal != None):
                    print("|{:<10}|{:<30}|{:<30}|".format(temporal.object.id,temporal.object.name,temporal.object.abbreviation));
                    temporal.object.service_points.Show();
                    temporal.object.transactions.Show();
                    temporal = temporal.next;
                    
            elif (type(temporal.object) == Service_Point):
                print("     PUNTOS DE SERVICIO"+"="*56);
                while(temporal != None):
                    print("     |{:<10}|{:<30}|{:<30}|".format(temporal.object.id,temporal.object.name,temporal.object.address));
                    temporal.object.desks.Show();
                    temporal = temporal.next;
                    
            elif (type(temporal.object) == Desk):
                print("           ESCRITORIOS"+"_"*63);
                while (temporal != None):
                    print("           |{:<10}|{:<30}|{:<30}| ".format(temporal.object.id, temporal.object.identification, temporal.object.manager))
                    temporal = temporal.next;
                    
            elif (type(temporal.object) == Transaction):
                print("     Transacción"+"="*56);
                while(temporal != None):
                    print("     |{:<10}|{:<30}|{:<30}|".format(temporal.object.id,temporal.object.name,temporal.object.time));
                    temporal = temporal.next;

                    
        else:
            print("="*20+" No se cuentan con Datos de Sistema"+"="*20);
            
Empresas_Lista = ListarObjetos();