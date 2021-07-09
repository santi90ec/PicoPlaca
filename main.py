import datetime
def validatePlate(placa):
    entrada=placa.replace('-',"").lower()
    letras=entrada[0:4]
    numero = entrada[-1:-5:-1]
    if len(entrada)<8 and numero.isdigit() and letras.isalpha():
        numero=int(numero[-1:-2:-1])
        return (numero)
    else:
        return "Error en la Placa"
def validateStatus(day):
    placa=0
    restricciones={
        1 : [1,2],
        2 : [3,4],
        3 : [5,6],
        4 : [7,8],
        5 : [9,0]
    }
    if day in restricciones and placa in restricciones[day]:
        return ("dia Restringuido",placa)
def main():
    try:
        print("*"*50+"\nWelcome to Validation System\n"+"*"*50)

        fecha = input("Introducir Fecha dd-mm-aaaa: ")
        hora = input("Introducir Hora HH:MM ")
        completedate=fecha+hora
        completedate = datetime.datetime.strptime(completedate, "%d-%m-%Y%H:%M")
        dia=int(completedate.strftime("%w"))
        print(validateStatus(dia))
        # placa = input("Introducir la placa del vehiculo ABCD-#### ")
        # print(validatePlate(placa))
    except ValueError as e:
        print(" Error Data \n")
        
main()