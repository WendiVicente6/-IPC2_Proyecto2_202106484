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
1. Cargar Archivo de Configuración
2. Cargar Archivo Inicial
        """)

        opcion = input("Ingrese una opcion: ")

        if opcion == '1':
            filename = input("Ingrese el archivo: ")
            file = './' + filename
            CargarArchivoConfiguracion(file,listaconfi)
            
        elif opcion == '2':
            pass
        
        elif opcion == '3':
            pass        
        elif opcion == '4':
            pass
        
        elif opcion == '5':
            pass
        elif opcion != '6':
            print("Opcion incorrecta\n")

if __name__ == '__main__':
    Menu()