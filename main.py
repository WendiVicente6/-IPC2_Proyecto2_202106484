import xml.etree.ElementTree as ET
from ListaConfiguracion import Company, Desk, ListarObjetos, Service_Point, Transaction


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
    print("""----------------------------PROYECTO NO. 2 ------------------------------""")
    while opcion != '6':
        print("")
        print("""Menú principal:
1. Cargar archivo de configuración del sistema
2. Limpiar Sistema
3. Crear nueva empresa
        """)

        opcion = input("Ingrese una opcion: ")

        if opcion == '1':
            filename = input("Ingrese el archivo: ")
            file = './' + filename
            CargarArchivoConfiguracion(file,listaconfi)
            
        elif opcion == '2':
            listaconfi.Eliminar()
        
        elif opcion == '3':
            listaconfi.Insert_End(Return_Company_individual())
            listaconfi.Show()

   
        elif opcion == '4':
            pass
        
        elif opcion == '5':
            pass
        elif opcion != '6':
            print("Opcion incorrecta\n")

if __name__ == '__main__':
    Menu()