from credit_card import CreditCard
from customer import Customer
from enumerations import DocumentType, PersonType


def main(credit_card):
    option = -1
    while(option == -1 or option > 1 or option < 0):
        print("MENU PRINCIPAL ENVIOS.CO \n1. Ver menu de opciones \n0. Salir")
        option = int(input("Option -> "))

        if(option == -1 or option > 1 or option < 0):
            print("\nERROR: escoja un opcion valida...\n")

        if (option == 1):
            main_menu()
        if (option == 0):
            exit()


def main_menu():
    option = -1
    while(option == -1 or option < 0 or option > 4):
        print("\nEscoja una opcion: \n1. Hacer un envio \n 2. Agregar una tarjeta \n 3. Agregar una direccion \n 4. Registrarme como cliente\n 0. Regresar al menu anterior\n")
        option = int(input("Opcion -> "))

        if(option == -1 or option > 4 or option < 0):
            print("\nERROR: escoja un opcion valida...\n")
    
        if (option == 1):
            make_delivery()
        if(option == 0):
            main()


def make_delivery():
    print("HACER ENVIO...")
    document_id = input("Ingrese su numero de documento de identidad: ")


if __name__ == "__main__":

    #Creamos un customer
    customer = Customer(national_id=1234567890, id_type=DocumentType.DNI.name, name="Edwin", last_name="Puertas", person_type=PersonType.NATURAL.name, email="epuerta@utb.edu.co")

    #Creamos un tarjeta
    credit_card = CreditCard(cvs = 750, expiry_day=8, expiry_month=7, expiry_year=2027, card_number=4546123678594213, zip_code=130001)

    customer.to_string()

    main(credit_card, customer)