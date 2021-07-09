import datetime
def validatePlate(placa):
    try:
        entrada = placa[-1:-5:-1]
        return entrada[::-1]
    except ValueError:
        print("La placa es incorrecta")
def main():
    try:
        print("*"*50+"\nWelcome to Validation System\n"+"*"*50)

        fecha = input("Introducir Fecha dd-mm-aaaa: ")
        hora = input("Introducir Hora HH:MM ")
        completedate=fecha+hora
        completedate = datetime.datetime.strptime(completedate, "%d-%m-%Y%H:%M")
        placa = input("Introducir la placa del vehiculo ABCD-#### ")
        placa=placa.replace('-',"").lower()
        print(validatePlate(placa))
    except:
        print ("Invalid Data\n")
main()