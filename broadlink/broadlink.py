import broadlink
import constantes 

# Conexión al dispositivo Broadlink (verificar direccion ip en archivo de constantes)
def busqueda_dispositivos():
    devices = broadlink.discover(discover_ip_address=constantes.broadcast)
    while(len(devices)==0):
        print("No existen dispositivos disponibles")
        devices = broadlink.discover(discover_ip_address=constantes.broadcast)
    print("Se ha establecido conexion con dispositivo broadlink")
    device=devices[0]
    device.auth()
    return device

# Funciones de control del aire acondicionado (A/C del LST)
def turn_on_AC(device):
    device.send_data(constantes.TURN_ON)
    print("Se ha encendido el aire acondicionado!")

def turn_off_AC(device):
    device.send_data(constantes.TURN_OFF)
    print("Se ha apagado el aire acondicionado!")

def temp_16_AC(device):
    device.send_data(constantes.TEMP_16)
    print("Se ha cambiado la temperatura a 16°C")

def temp_17_AC(device):
    device.send_data(constantes.TEMP_17)
    print("Se ha cambiado la temperatura a 17°C")

def temp_18_AC(device):
    device.send_data(constantes.TEMP_18)
    print("Se ha cambiado la temperatura a 18°C")

def temp_19_AC(device):
    device.send_data(constantes.TEMP_19)
    print("Se ha cambiado la temperatura a 19°C")

def temp_20_AC(device):
    device.send_data(constantes.TEMP_20)
    print("Se ha cambiado la temperatura a 20°C")

def temp_21_AC(device):
    device.send_data(constantes.TEMP_21)
    print("Se ha cambiado la temperatura a 21°C")

def temp_22_AC(device):
    device.send_data(constantes.TEMP_22)
    print("Se ha cambiado la temperatura a 22°C")

def temp_23_AC(device):
    device.send_data(constantes.TEMP_23)
    print("Se ha cambiado la temperatura a 23°C")

def temp_24_AC(device):
    device.send_data(constantes.TEMP_24)
    print("Se ha cambiado la temperatura a 24°C")

#Funcion para receptar datos por infrarojo
def aprenderIR(device):
    device.enter_learning()
    packet = ""
    while (len(packet)==0):
        try:
            packet = device.check_data()
            print(packet)
        except:
            pass

#Funcion para configurar wifi del dispositivo (verificar variables en archivo de constantes)
def broadlinkSetUp():
    broadlink.setup(constantes.myssid, constantes.mynetworkpass, 3)

def main():
    opcion=0
    print("Bienvenido al menu de control del A/C")
    device = busqueda_dispositivos()
    while (opcion!='4'):
        print("Que accion desea realizar?\n1:Controlar A/C\n2:Receptar codigo IR\n3:Configurar wif-fi Broadlink\n4:Salir\n")
        opcion=input('Opcion:')

        if opcion=='1':
            accion=0
            while (accion!='4'):
                print("Que accion desea realizar?\n1:Encender A/C\n2:Apagar A/C\n3:Establecer temperatura\n4:Regresar\n")
                accion=input('Accion:')
                if accion=='1':
                    turn_on_AC(device)
                elif accion=='2':
                    turn_off_AC(device)
                elif accion=='3':
                    temp=0
                    while int(temp)<16 or int(temp)>24:
                        temp=input('A qué temperatura deseas setear el aire? (16-24 °C):')
                        if temp=='16':
                            temp_16_AC(device)
                        elif temp=='17':
                            temp_17_AC(device)
                        elif temp=='18':
                            temp_18_AC(device)
                        elif temp=='19':
                            temp_19_AC(device)
                        elif temp=='20':
                            temp_20_AC(device)
                        elif temp=='21':
                            temp_21_AC(device)
                        elif temp=='22':
                            temp_22_AC(device)
                        elif temp=='23':
                            temp_23_AC(device)
                        elif temp=='24':
                            temp_24_AC(device)
                        else:
                            print("La temperatura esta fuera del rango")

        elif opcion=='2':
            aprenderIR(device)

        elif opcion=='3':
            broadlinkSetUp()

    print("Gracias!")
        
if __name__ == "__main__":
    main()