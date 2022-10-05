from tkinter import N
from turtle import pu
import xml.etree.ElementTree as ET
from ListaClientes import Clientes, Configuracion, EscritorioActivo, Lista, TransaccionesCliente
from ListaConfiguracion import Company, Desk, ListarObjetos, Service_Point, Transaction
from xml.dom import minidom



def LeerXmlPruebas(file,listaIniciaPrograma):

    archivoLeido =minidom.parse(file)
    PruebaInicial= archivoLeido.getElementsByTagName('configInicial')
    
    for configInicial in PruebaInicial:
        idConfiguracion=configInicial.getAttribute('id')
        ideEmpresaConfiguracion=configInicial.getAttribute('idEmpresa')
        idPuntoConfiguracion=configInicial.getAttribute('idPunto')
        #print(idConfiguracion,ideEmpresaConfiguracion,idPuntoConfiguracion)
        temporalConfig=Configuracion(idConfiguracion,ideEmpresaConfiguracion,idPuntoConfiguracion)
        listaEscritoriosConfiguracion=configInicial.getElementsByTagName('escritorio')

        for escritorio in listaEscritoriosConfiguracion:
            ideEscritorioConfiguracion=escritorio.getAttribute('idEscritorio')  
            #print(ideEscritorioConfiguracion)
            tempEscritoriosActivos=EscritorioActivo(ideEscritorioConfiguracion)
            temporalConfig.EscritoriosActicos.AgregarFinal(tempEscritoriosActivos)
            listadoClientes=configInicial.getElementsByTagName('cliente')       
        
        for cliente in listadoClientes:
            dpi=cliente.getAttribute('dpi')
            nombre=cliente.getElementsByTagName('nombre')[0].childNodes[0].nodeValue
            #print(dpi,nombre)
            temporalCliente=Clientes(dpi,nombre)
            listadoTransacciones=cliente.getElementsByTagName('transaccion')
            temporalConfig.FilaClientes.AgregarFinal(temporalCliente)
        
            for transaccion in listadoTransacciones:
                idtransaccionConfiguracion=transaccion.getAttribute('idTransaccion')
                cantidad=transaccion.getAttribute('cantidad')
                #print(idtransaccionConfiguracion,cantidad)
                temporalTransaacionC=TransaccionesCliente(idtransaccionConfiguracion,cantidad)
                temporalCliente.transaccionesARealizar.AgregarFinal(temporalTransaacionC)
            listaIniciaPrograma.AgregarFinal(temporalConfig)
    ImprimePruebaDeSistema(listaIniciaPrograma)

def ImprimePruebaDeSistema(listaIniciaPrograma):

    temp1=listaIniciaPrograma.head
    print("????????????????????????????????????????????????????????????????????????????????????")
    while temp1 != None:
        print("----------------------------CONFIGURACIÓN--------------------------------")
        print('CODIGO: ',temp1.dato.codigoConfiguracion)
        print('ID EMPRESA: ',temp1.dato.ideEmpresaConfiguracion)
        print('ID ATENCION: ',temp1.dato.idePuntoDEAtencionConfiguracion)
        lEsciroeiosA=temp1.dato.EscritoriosActicos
        temp2=lEsciroeiosA.head
        print("         Escritorios Activos------------------------")        
        while temp2!=None:
            
            print('         ID: ',temp2.dato.ideEscritorioActivo)
            lC=temp1.dato.FilaClientes
            temp3=lC.head
            temp2=temp2.sig
        
        while temp3!=None:
            print("         CLIENTE--------------------------------")
            print('             DPI: ',temp3.dato.dpiCliente)
            print('             NOMBRE: ',temp3.dato.nombreCliente)

            
            ltR=temp3.dato.transaccionesARealizar
            temp4=ltR.head
           
            print("             TRANSACCIONES DEL CLIENTE-----------------------------")
            while temp4!=None:
                

                print('             ID TRANSACCION: ',temp4.dato.ideTransaccionARealizar,'  A REALIZAR : ' ,temp4.dato.nveces,'  VECES')
                temp4=temp4.sig   
            temp3=temp3.sig    
            temp1=temp1.sig   


def CargarArchivoConfiguracion(file, xmlconfiguracion):
    tree = ET.parse(file)
    root = tree.getroot()
    for company in root:
        xmlconfiguracion.Insert_End(Return_Company(company));

    xmlconfiguracion.Show(); 
def Return_Company(company):
    aux_id_company = "";
    aux_name_company = "";
    aux_abbreviation_company = "";
    aux_service_point:ListarObjetos = None;
    
    aux_id_company = company.get("id");
    for information_company in company:
        if (information_company.tag == "nombre"):
            aux_name_company = information_company.text;
        elif (information_company.tag == "abreviatura"):
            aux_abbreviation_company = information_company.text;
        elif (information_company.tag == "listaPuntosAtencion"):
            aux_service_point = Return_List(information_company,1);
        elif (information_company.tag == "listaTransacciones"):
            aux_transaction = Return_List(information_company,2);
            
    aux_company = Company(aux_id_company,aux_name_company,aux_abbreviation_company);
    aux_company.service_points = aux_service_point;
    aux_company.transactions = aux_transaction;
    
    return aux_company;

def Return_Company_individual():
    aux_service_point:ListarObjetos = None;
    idempresa=input("Ingrese ID de la nueva empresa: ")
    nombre=input("Ingrese nombre de la nueva empresa: ")
    abreviatura=input("Ingrese abreviatura de la nueva empresa: ")
    aux_service_point = Return_List_individual(1);

    aux_transaction = Return_List_individual(2);
            
    aux_company = Company(idempresa,nombre,abreviatura);
    aux_company.service_points = aux_service_point;
    aux_company.transactions = aux_transaction;
    
    return aux_company;

def Return_List_individual(status):

    if (status == 1):
        aux_list = ListarObjetos();

        aux_list_desks: ListarObjetos = None;

        idpunto=input('Ingrese ID del punto de atención: ')
        nombrepunto=input('Ingrese nombre del punto de atención: ')
        direpunto=input('Ingrese Dirección del punto de atención: ')

        aux_list_desks = Return_List_individual(3);
            
                
        aux_service_point = Service_Point(idpunto,nombrepunto,direpunto);
        aux_service_point.desks = aux_list_desks;
        aux_list.Insert_End(aux_service_point);

        return aux_list;
    
    elif (status == 2):
        aux_list = ListarObjetos();
        idtran=input('Ingrese ID de la transaccion: ')
        nombretran=input('Ingrese nombre de la transaccion: ')
        tiempo=input('Ingrese tiempo de la transaccion: ')
            
        aux_transaction = Transaction(idtran,nombretran,tiempo);
        aux_list.Insert_End(aux_transaction);

        return aux_list;

    elif (status == 3):
        aux_list = ListarObjetos();

        idescritorio=input('Ingrese ID del escritorio: ')
        identificacion=input('Ingrese nombre del escritorio: ')
        encargado=input('Ingrese encargado del escritorio: ')
                
        aux_desks = Desk(idescritorio,identificacion,encargado);
        aux_list.Insert_End(aux_desks);

        return aux_list;    
def Return_List(root,status):

    if (status == 1):
        aux_list = ListarObjetos();
        for  branch_1 in root:
            aux_id = "";
            aux_name = "";
            aux_other ="";
            aux_list_desks: ListarObjetos = None;
            
            aux_id = branch_1.get("id");
            
            for branch_1_1 in branch_1:
                if (branch_1_1.tag == "nombre"):
                    aux_name = branch_1_1.text;
                elif (branch_1_1.tag == "direccion"):
                    aux_address = branch_1_1.text;
                elif (branch_1_1.tag == "listaEscritorios"):
                    aux_list_desks = Return_List(branch_1_1,3);
                
                    
            aux_service_point = Service_Point(aux_id,aux_name,aux_address);
            aux_service_point.desks = aux_list_desks;
            aux_list.Insert_End(aux_service_point);

        return aux_list;
    
    elif (status == 2):
        aux_list = ListarObjetos();
        for  branch_1 in root:
            aux_id = "";
            aux_name = "";
            aux_other ="";
            
            aux_id = branch_1.get("id");
            
            for branch_1_1 in branch_1:
                if (branch_1_1.tag == "nombre"):
                    aux_name = branch_1_1.text;
                elif (branch_1_1.tag == "tiempoAtencion"):
                    aux_address = branch_1_1.text;
                    
            aux_transaction = Transaction(aux_id,aux_name,aux_address);
            aux_list.Insert_End(aux_transaction);

        return aux_list;

    elif (status == 3):
        aux_list = ListarObjetos();
        for  branch_1 in root:
            aux_id = "";
            aux_name = "";
            aux_other ="";
            
            aux_id = branch_1.get("id");
            
            for branch_1_1 in branch_1:
                if (branch_1_1.tag == "identificacion"):
                    aux_name = branch_1_1.text;
                elif (branch_1_1.tag == "encargado"):
                    aux_address = branch_1_1.text;
                    
            aux_desks = Desk(aux_id,aux_name,aux_address);
            aux_list.Insert_End(aux_desks);

        return aux_list;   


def Menu():
    print("")
    
    opcion = ''
    listaconfi=ListarObjetos()
    listaIniciaPrograma=Lista()
    print("""----------------------------PROYECTO NO. 2 ------------------------------""")
    while opcion != '6':
        print("")
        print("""Menú principal:
1. Cargar archivo de configuración del sistema
2. Cargar archivo de configuración del sistema
3. Limpiar Sistema
4. Crear nueva empresa
5. Realizar Operaciones
6. Graficara 1


        """)

        opcion = input("Ingrese una opcion: ")

        if opcion == '1':
            filename = input("Ingrese el archivo: ")
            file = './' + filename
            CargarArchivoConfiguracion(file,listaconfi)
               
        elif opcion == '2':
            filename = input("Ingrese el archivo: ")
            file = './' + filename

            LeerXmlPruebas(file,listaIniciaPrograma)
            
        elif opcion == '3':
            listaconfi.Eliminar()
            listaconfi.Show()
        elif opcion == '4':
            listaconfi.Insert_End(Return_Company_individual())
            listaconfi.Show()


        
        elif opcion == '5':
            contar=0
            activos=[]
            transacciones=[]
            empresa=input("Ingrese nombre de la empresa: ")
           
            punto=input("Ingrese punto de atención: ")
            (empr,pun)=listaconfi.getEmpresa(empresa,punto)
            print("ID de la empresa Elegido: ",empr.object.id,"ID del punto de servicio elegido: ",pun.object.id)

             
            activos=listaIniciaPrograma.EscritoriosActivos(empr.object.id,pun.object.id)
            
            listaconfi.EscritoriosInactivos(empr.object.id,pun.object.id,activos)
            listaIniciaPrograma.ClientesEspera(empr.object.id,pun.object.id)
            transacciones=listaIniciaPrograma.CantidadTransacciones(empr.object.id,pun.object.id)
            listaconfi.CalcularTiempoPromedio(empr.object.id,transacciones)
            pregunta=input("Desea Activar algun escritorio: (S/N) ")
            if pregunta=="S":
                idescritorio=input("Ingrese ID de escritorio: ")
                listaIniciaPrograma.ActivarEscritorio(empr.object.id,pun.object.id,idescritorio)
                #listaconfi.ActivarInactivos(empr.object.id,pun.object.id,activos,idescritorio)
                listaIniciaPrograma.MostrarActivos(empr.object.id,pun.object.id)
            pregunta2=input("Desea Desactivar algun escritorio: (S/N) ")
            if pregunta2=="S":
                listaIniciaPrograma.DesactivarEscritorio(empr.object.id,pun.object.id)
                listaIniciaPrograma.MostrarActivos(empr.object.id,pun.object.id)
            atender=input("Desea Empezar a atender Clientes: (S/N) ")
            if atender=="S":
                while atender!="N":
                    listaIniciaPrograma.Atender(empr.object.id,pun.object.id)
                    listaIniciaPrograma.ClientesFaltantes(empr.object.id,pun.object.id)
                    atender=input("Desea Empezar a atender Clientes: (S/N) ")

            solicitud=input("Desea ingresar un nuevo cliente: (S/N) ")
            if solicitud=="S":
                
                listaconfi.MostrarTransacciones(empr.object.id,pun.object.id)
                listaIniciaPrograma.MeterCliente(empr.object.id,pun.object.id)
                listaIniciaPrograma.ClientesFaltantes(empr.object.id,pun.object.id)


        elif opcion == '6':
            idemmpresa=input("Ingrese ID de la empresa: ")
            idpunto=input("Ingrese punto de la empresa: ")
            listaIniciaPrograma.graficar(idemmpresa,idpunto)

        elif opcion != '7':
            print("Opcion incorrecta\n")

if __name__ == '__main__':
    Menu()