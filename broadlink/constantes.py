#Constantes

#Datos Broadlink
#myssid =                                   //Ingresar ssid de la red a configurar
#mynetworkpass =                            //Ingresar password de la red a configurar
#ip =                                       # Dirección IP del dispositivo Broadlink
broadcast = '192.168.100.255'               # Dirección IP de broadcast

#cambios de estado del A/C
TURN_OFF = b'&\x00\xba\x01\x0e\x0f\r+\x10\x0e\r\x0f\x0e\x0f\r\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\x0e\x0f\r\x0e\x0e\x10\r+\x11\x0c\x0e\x0e\x0f\x0f\x0c\x0f\x0e\x0f\x0e\x0f\r\x0f\r+\x0f+\r+\x0f\x0e\x0f\x0e\x0e*\x0f\x0f\x0c\x11\r\x0e\r\x10\x0e\x10\r\x0e\x0e\x0e\r\x11\r\x0f\r\x0f\x0e\x0f\x0c\x11\r\x0e\x0c\x12\r\x0e\x0e\x0f\x0e\x0e\r\x0f\x0f\x0f\x0c\x0f\x10\r\r\x10\x0e\x0e\r\x10\r\x0f\x0e\x10\r\x0e\r\x0f\x0e\x0f\r\x12\x0b,\x0e+\r\x0f\r\x10\x0e\x0e\r\x0f\x0f\x0e\r\x00\x01Vq:\x0e\x0e\r+\x0f\x0f\x0c\x0f\x10\x0e\r\x10\x0c\x11\x0c\x0f\r\x10\x0c\x10\x0e\x0f\r\x0e\r\x13\x0b,\r\x0e\x0e\x10\x0c\x10\r\x11\x0c\x0f\x0c\x11\r\x10\r*\x0e,\x0e*\x0e\x0f\x0e\x0f\r+\x10\r\x0e\x0e\x0f\x0f\r\x0f\r\x0f\x0c\x11\r\x0f\x0e\x0e\x0f\x0f\x0c\x0f\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0f\r\x10\r\x0f\r+\x0f*\x0e,\r\x11\x0c\x0e\x0e\x0e\x0f*\x0c\x11\x0e,\x0e\x0e\x0e+\x0f\x0e\r\x0f\r\x0f\r\x11\x0c\x0f\x0e\x0f\r\x10\x0e\x0e\x0e\x0e\x0f+\x0c,\x0f*\x0e+\x0e+\r-\x0c\x10\x0e+\x0e\x0e\r\x10\x0e\x0e\r\x10\x0f\x0e\x0e\r\r\x11\x0c\x10\x0e\x0e\x0e\x0f\x0e\x0e\x0c\x11\x0e\x0e\r\x11\r\x0e\r\x0f\x0f\x0e\x0f\x10\x0c+\r+\x0f*\x0f\x0e\x0e\x0e\x0e\x0f\r\x12\x0b\x0e\x0f\x0f\r\x0f\r\x10\x0e\x0e\r,\r+\x0e+\x0e\x10\r\x0f\x0f\x0e\x0c\x10\x0e\x0e\r\x10\r\x10\r\x0f\r\x10\r\x10\x0c\x10\r\x0e\x0e\x10\x0c\x10\x10\r\x0c\x10\r+\x0f\x10\x0c\x0e\x0e\x11\x0c\x0f\x0e\x0f\x0c\x10\r+\x0f\x10\x0c\x0f\x0e\x0f\r\x0e\x10\x0e\x0c\x10\r\x0f\r\x10\r\x10\r\x0f\r\x10\r\x0e\r\x11\r\x0f\r\x10\x0e\x0e\r\x0f\r,\x0e+\x0e\x0e\x0e+\x0e,\x0e\x0e\x0e+\r\x00\r\x05'
TURN_ON = b'&\x00\xbc\x01o:\x0e\x10\x0c,\x0e\x0e\r\x10\x0e\x0f\r\x0f\r\x10\x0c\x10\x0e\x0e\x0e\x0f\r\x10\r\x14\t\x0e\r,\x0e\x0f\x0f\x0e\r\x0f\r\x0f\x0e\x0f\x0e\x0e\r\x0f\x0e,\r+\x10)\x0e\x0e\x0e\x11\x0c+\x0f\x0e\r\x10\r\x0f\x0e\x0e\x0e\x10\x0c\x10\r\x10\r\x10\x0c\x0f\x0e\x0f\x0e\x0e\x0e\x0f\x0c\x11\r\x0f\r\x10\r\x0f\x0e\x0e\r\x0f\r\x10\x0e\x0f\x0c\x11\r\x0f\r\x11\x0b\x10\x0c\x11\x0c\x10\x0c\x10\x0e\x10\x0b\x10\x0e\x0f\x0c-\x0c,\r\x10\x0e\x11\n\x10\r\x0f\x10\r\x0e\x00\x01Tq:\r\x10\x0e,\r\x0e\r\x0f\x0f\x0e\r\x10\r\x0f\r\x11\x0c\x0e\x0e\x10\x0f\r\r\x10\x0e\x0e\r,\r\x11\x0c\x10\r\x0f\r\x0e\x0e\x12\x0b\x0f\r\x10\x0c,\x0e+\x0e+\x0e\x0f\r\x10\r+\r\x0f\x10\x0e\r\x0f\x0f\x0e\r\x0e\x0f\x0f\r\x0f\r\x0f\x0e\x0f\x0e\x10\x0b\x0f\x0e\x10\r\x0f\x0e*\r\x11\r\x0f\x0e+\r+\x10)\r\x11\x0c\x0f\x0e\x10\r+\r-\r+\x10\r\r+\x0e\x10\x0c\x10\r\x0f\r\x10\r\x10\r\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e,\x0e)\x0e,\x0e*\x10*\x0e*\x10\x0f\r*\x0f\x0f\r\x11\x0b\x0f\r\x10\r\x0f\x0e\x0f\r\x10\x0e\x0e\r\x0e\x0f\x0e\x0e\x0f\r\x0f\r\x10\x0e\x0e\x0e\x0f\x0e\x0f\x0c\x0f\x0f\x0f\r+\r,\x0f+\x0c\x11\r\x0f\r\x0e\r\x11\x0c\x11\x0c\x12\x0c\x0f\r\x0f\x0c\x10\x0e,\x0f(\x0e+\x11\x0c\x0f\x0e\r\x0f\x0e\x0f\r\x10\x0c\x10\x0e\x0e\x0e\x0e\x0f\x0e\r\x11\x0c\x0f\x0f\x0e\x0e\x0e\r\x0f\x0f\x0e\x0e\x0e\x0e+\x0e\x0f\r\x10\x0e\x0e\x0f\x0e\r\x11\x0c\x10\r*\x0e\x0f\x0e\x0e\x0e\x0f\r\x10\r\x10\x0c\x11\r\r\x0e\x0f\r\x10\x0e\x0f\x0c\x10\x0e\x0f\x0c\x10\x0e\x0f\r\x0e\x0f\x0f\r,\r+\x0f\x0e\x0e+\x0c,\x0e,\x0e\x0f\x0c,\r\x00\r\x05'
TEMP_16 = b'&\x00\xbc\x01m:\x0e\x0f\r,\x0e\x0e\r\x10\x0c\x10\r\x10\x0e\x0e\x10\r\x0e\x0e\x0e\x0f\r\x0f\r\x10\x0e\x0e\r,\x0e\x0e\x0e\x0f\r\x0f\x0e\x0f\x0e\x0e\x0f\x0e\x0f\x0e\x0e*\x0e+\x0e+\x0e\x0f\r\x10\x0f)\x0e\x0f\x0e\x0f\x0c\x0f\x0f\x0f\r\x10\r\x0e\r\x11\r\x0f\r\x0e\x10\x0e\r\x0e\x0f\x0e\x0e\x0e\x0e\x10\x0c\x0f\x0f\x0f\x0c\x0f\x0f\x0f\r\x0f\r\x0f\r\x10\x0e\x0e\r\x0f\x0f\x0e\x0e\x0f\x0e\x0e\x0e\x0e\x0e\x0f\x0e\x10\x0c\x0f\x0e+\r+\x0f\x0e\x0e\x0f\x0e\x0f\r\x0f\x0e\x11\x0c\x00\x01Tq:\x0e\x0f\x0e*\x0f\x0e\r\x10\r\x0f\r\x10\x0c\x10\x0e\x0e\r\x10\x0c\x11\x0c\x11\r\x0f\x0c\x11\r+\x0e\x0e\r\x0f\x0e\x0f\x0e\x0e\x0e\x10\r\x0e\x0e\x0f\r,\r,\x0e*\x0f\x0f\r\x10\x0c,\x0e\x0f\r\x0f\r\x0f\x0e\x0f\r\x10\r\x10\r\x0f\r\x0f\r\x10\r\x11\x0c\x0f\x0e\x0e\x0e\x0f\r,\r\x0f\r\x0f\r-\r+\r-\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0e\x0e\x10\r\x0f\x0e+\r\x0f\x0f\x0e\x0f\r\x0f\r\x0f\x0e\r\x10\x0e\x0f\r\x0f\r\x10\x0b,\x0e,\r,\r,\r+\x0e,\x0e\x0f\r+\x0e\x0f\r\x0f\r\x10\r\x10\r\x0f\r\x10\x0c\x10\x0e\x0f\r\x10\x0c\x10\x0c\x11\x0f\r\r\x0f\r\x0f\r\x10\r\x10\x0c\x0f\r\x11\r,\x0c,\x0f*\x0e\x0e\x0e\x10\r\x0f\r\x0f\x0e\x0f\x0e\x0e\r\x0f\x0f\x0f\r\x0f\x0c,\x10*\x0e+\x0e\x0f\r\x0f\r\x0f\x0e\x0e\x0e\x0f\x0e\x0f\r\x0f\x0e\x10\x0c\x0f\x0f\x0e\r\x0f\x0c\x11\r\x0f\x0e\x0f\r\x0e\x0e\x10\r+\x0f\x0e\x0e\x0f\x0c\x0f\x0e\x10\r\x0e\x0f\x0e\r,\r\x10\x10\x0c\x0e\x0f\r\x10\r\x10\x0c\x0f\x0e\x0f\x0e\x0e\r\x10\x0e\x0f\x0c\x10\x0e\x0e\r\x11\r\x0f\x0c\x10\x0e\x0e\r,\r\x0f\x0e+\x0f*\x0f\x0e\r,\r\x0f\x0e+\x0e\x00\r\x05'
TEMP_17 = b'&\x00\xbc\x01m;\r\x10\r,\r\x0e\r\x11\r\x0f\r\x11\x0b\x10\x0c\x10\r\x10\r\x10\r\x0e\r\x12\n\x11\x0c,\x0e\x0f\r\x10\x0c\x10\r\x0f\x0e\x0e\x0e\x10\r\x0f\r,\r,\r,\r\x0e\x0e\x10\r,\r\x0e\x0e\x11\x0b\x11\r\x10\x0c\x0f\x0e\x10\x0c\x0f\r\x10\r\x11\x0b\x10\x0b\x11\x0e\x0e\x0f\x0e\x0e\x0f\x0c\x10\x0e\x0f\r\x0f\x0c\x11\x0c\x10\r\x0f\r\x10\r\x0f\r\x11\x0c\x0f\r\x11\r\x0e\r\x11\r\x0f\r\x0f\x0e\x0e\r,\x0f*\x0f\x0e\r\x0f\x0e\x0e\x0f\x0e\r\x0f\x0e\x00\x01Tr;\r\x0f\r,\r\x0e\x0e\x10\r\x0f\r\x10\r\x10\r\x0e\x0e\x10\x0c\x10\x0b\x11\x0e\x10\x0b\x10\x0e+\r\x10\x0c\x0f\x0e\x10\x0c\x10\x0e\x0e\r\x12\x0c\x0e\x0f*\r+\x10)\x10\x0f\r\x0e\r,\r\x10\r\x0f\r\x10\x0e\x0e\r\x11\x0c\x0f\x0e\x0f\x0c\x11\r\x0f\r\x0f\r\x10\x0c\x11\r\x10\x0c+\r\x11\x0e\x0e\r,\r,\r+\r\x12\n\x11\r\x0f\r,\x0e\x0f\x0c\x10\r\x10\x0c,\x0e\x0f\r\x10\r\x0f\r\x10\x0c\x10\r\x10\r\x0f\r\x0f\x0e\x0f\r+\x0e-\r+\x0e+\r,\r,\x0c\x10\x0e+\r\x11\x0b\x10\r\x11\x0c\x0f\x0f\x0f\x0b\x11\r\x10\x0b\x10\x0e\x0e\r\x10\r\x10\x0c\x10\x0e\x0f\x0b\x11\x0e\x0f\x0c\x10\r\x10\x0c\x11\x0c,\r,\x0e+\x0e\x0e\x0e\x10\r\x0e\x0f\x0e\r\x10\r\x0f\x0e\x0f\r\x10\x0c\x0f\x0e+\x0e*\x0f*\x10\x0e\r\x10\r\x0e\x10\x0e\x0e\x0e\r\x10\x0e\x0e\r\x0f\x10\x0e\x0c\x10\x0c\x11\x0c\x11\x0c\x0f\x0c\x11\x0e\x0e\r\x0f\r,\x0e\x0f\x0c\x10\x0e\x10\x0c\x0e\x0f\x0f\r\x0f\r,\x0e\x0f\x0c\x11\r\x0f\x0c\x11\r\x0f\x0c\x10\r\x0f\r\x10\x0e\x0f\x0c\x11\x0c\x0f\x0e\x0e\x0f\x0e\x0e\x10\x0c\x0f\r\x10\r,\r+\x0f*\x0e+\r\x12\x0c+\x0e\x0f\x0c-\r\x00\r\x05'
TEMP_18 = b'&\x00\xbc\x01p9\x0e\x0e\x0e,\r\x0f\x0e\x0f\x0e\x0e\x0e\x0e\x0f\x0f\r\x0e\x0e\x0e\x0f\x0f\r\x0e\x0e\x10\x0f\r\x0e*\x10\r\x0e\x0e\x0f\x0e\x0e\x0f\x0e\x0f\r\x0e\x0e\x11\x0c+\x0e+\x0e+\x0f\r\x0e\x10\x0e*\x0e\x0f\x0e\x0f\x0e\x0e\x0e\x0f\x0e\r\x0f\x0f\r\x0f\r\x0f\x0e\x0e\x0f\x0f\r\x0e\x10\x0e\r\x0f\r\x10\x0c\x0f\x0f\x0f\r\x0e\x0f\x0f\r\x0e\x0e\x10\x0c\x10\x0e\x0e\r\x10\x0f\x0e\x0e\r\x0e\x0f\r\x0f\x0f\x0e\x0e\x0e\x0f\x0f\x0c,\r,\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\r\x0f\x0f\x00\x01Ts7\x0f\x0f\x0c,\x0e\x0f\r\x0f\r\x10\r\x11\r\r\x0f\x0f\r\x0e\x0f\x0e\x0e\x10\x0c\x0f\x0e\x0f\r+\x0f\x0f\x0c\x0f\x0f\x0f\r\x0f\r\x0f\x0f\x0e\r\x0f\x0f*\r-\r+\r\x0f\x0f\x0e\x0f*\x0e\x0f\x0e\x0e\r\x10\r\x10\x0c\x10\x0e\x0e\r\x10\x0e\x0e\r\x0f\x0f\x0e\r\x10\x0e\x0e\r\x0f\x0f*\x0e\x0f\r\x11\r+\x0e*\x0e+\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f+\x0e\x0f\x0c\x0f\x0f*\x0e\x0f\r\x0f\x0f\x0e\r\x10\r\x0f\r\x10\x0e\x0e\r\x10\x0c\x10\x0e+\r+\x0e+\x0e+\x0f*\x0f*\x0e\x0f\r,\x0e\x0e\x0e\x10\x0c\x10\x0e\x0f\x0c\x10\x0e\x0f\x0c\x10\r\x0f\x0e\x10\x0c\x0f\r\x10\x0e\x0e\r\x0f\x0e\x10\x0c\x0f\x0f\x0f\r\x0f\r\x0f\x0e+\r,\r,\r\x0f\x11\x0c\x0e\x10\x0c\x0f\r\x10\r\x0f\r\x10\x0e\x0e\r\x0f\x0f*\x0f*\x0e,\x0e\x0e\x0e\x0f\x0e\x0e\r\x0f\x0f\x0e\r\x0f\x0e\x10\x0c\x10\r\x0e\x0e\x10\x0e\x0e\r\x10\x0e\x0f\x0c\x0f\x0f\x0e\r\x0f\x0e+\x0e\x0e\x0e\x0f\x0e\x0f\r\x0f\r\x10\r\x0f\x0e+\x0e\x10\x0c\x10\x0f\x0c\x0e\x0f\x0e\x10\r\x0e\r\x10\r\x0f\r\x10\x0e\x0f\r\x0e\x0e\x10\r\x10\r\x0e\x0e\x0f\x0e\x0e\r,\r\x0f\x0e\x10\r\x0e\x0e,\x0e*\x0e\x0f\r,\x0e\x00\r\x05'
TEMP_19 = b'&\x00\xbc\x01n:\r\x0f\x0f*\x0e\x0f\r\x0f\x10\r\x0e\x0f\r\x0f\x0f\x0e\x0e\x0e\r\x0f\x0f\x0f\x0c\x0f\x0f\x0e\r+\x0f\x0f\r\x0e\x0e\x10\r\x0f\r\x0f\x0f\x0e\r\x0f\r,\x0e,\r+\x0f\r\x0f\x0e\x0f*\x0f\r\x0e\x10\r\x0e\x0f\x0f\r\x0e\x0e\x10\r\x0e\x0e\x10\r\x0f\r\x10\r\x0e\x0f\x0e\x0f\r\x0f\x0f\r\x0e\x10\x0e\r\x0f\r\x0f\x0e\x0e\x0e\x10\x0c\x0f\x10\x0e\x0e\r\x0f\x0e\x0e\x0e\x0f\x0f\r\x0e\x0e\x0f\x0f\r\x0f\x0f\x0c,\r,\r\x10\r\x10\x0c\x0f\x0f\x0f\x0c\x0f\x0f\x00\x01Sr9\x0e\x0f\x0e,\r\x0f\x0e\x0f\r\x0e\x0f\x0f\x0e\x0e\r\x10\x0e\r\x0e\x0f\x0e\x0e\x0f\x10\x0c\x0e\x0e+\x0e\x0f\x0e\x0f\r\x0f\x0e\x0e\x0e\x10\r\x0e\x0f\x0f\r,\r+\x0e+\x0e\x0e\x0e\x10\r+\x0e\x0e\x0f\x0f\r\x0e\x0e\x0f\x0e\x0e\x0e\x10\r\x0e\x0f\x0e\r\x10\x0e\x0e\r\x0f\x0f\x0f\r\x0e\x0e+\x0e\x10\x0c\x0f\x0e,\x0e*\x0f*\x0e\x0f\x0e\x0e\x0f\x0e\r,\x0f*\r\x0f\x0e\x0f\x0f*\x0e\x0e\x0f\x0e\r\x10\x0e\x0e\r\x10\x0e\x0e\x0e\x0e\x0f\x0f\x0c\x0f\x0e+\x0f*\x0f*\x0e+\x0f*\x10)\x0f\r\x0e,\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0f\r\x0e\x10\r\x0e\x0e\x10\r\x0e\x0e\x10\x0e\x0f\x0c\x0f\x0e\x0f\r\x10\r\x0e\x0f\x0f\r\x0e\x0f*\x0e+\x0e+\x0e\x0f\x0e\x0e\x0f\x0f\r\x0e\r\x11\x0c\x0f\x10\r\x0e\x0e\x0e\x0f\x0e,\x0e*\r-\r\x0e\x0f\x0e\r\x0f\x0f\x0f\x0c\x0f\x0f\x0f\r\x0e\x0f\x0e\r\x0f\x0f\x0e\r\x0f\x0f\x0e\x0c\x10\x0e\x0f\r\x0f\x0f\x0e\r,\x0e\x0e\x0f\x0f\x0c\x0f\x0e\x0e\x0e\x11\x0c\x10\x0c+\x0f\x0e\x0f\x0e\r\x0f\x0f\x0e\r\x0f\x0f\x0e\r\x0f\x0f\x0e\r\x10\x0e\r\x10\r\x0e\x0e\x0f\x0f\x0e\x0e\r\x0f\x0f\x0e\x0e*\x0f*\x10\x0e\r\x0e\x0e,\r,\r\x0f\x0f+\x0f\x00\r\x05'
TEMP_20 = b'&\x00\xbc\x01p8\x0f\x0e\x0e,\r\x0e\x0f\x0f\r\x0f\r\x0f\r\x10\r\x0f\x0f\x0e\x0e\x0e\r\x0f\x0e\x0f\x0e\x0e\x0f+\r\x0f\r\x10\r\x0f\x0e\x0f\r\x10\x0e\r\x0e\x10\x0c,\x0e+\x0e+\r\x10\x0e\x0f\x0e*\x0f\x0e\x0e\x0e\x0e\x0e\x0f\x0e\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0f\r\x0f\x0e\x0e\x0f\r\x0f\x0e\x10\r\x0e\x11\x0b\x0e\x0f\r\x10\x0e\x0e\x0e\x0f\x0e\x0e\r\x10\r\x0f\r\x0f\x0e\x0f\x0e\x0e\x0f\r\x0e\x10\x0c\x10\r\x10\x0e\r\x0e+\x0f*\x0e\x0f\x0e\x0e\x0e\x10\r\x0f\r\x10\r\x00\x01Tr:\x0f\r\x0f*\x0e\x0f\r\x0f\x0e\x0f\x0e\x0f\x0e\x10\x0c\x0f\x0c\x10\x0e\x0e\x0e\x10\x0c\x0f\x0f\r\x10*\r\x0f\r\x10\x0e\x0e\r\x10\x0e\x0e\x0e\x0f\r\x0f\x0e+\x0f*\r,\x0e\x0f\r\x0f\x0e+\x10\x0c\x0e\x0e\x0f\x0f\r\x0f\x0e\x0f\r\x0f\x0f\x0e\r\x0f\x0b\x13\x0c\x0f\x0e\x0f\r\x0e\x0f\x0f\r,\r\x0e\x10\x0f\r*\x0f*\x0f+\r\x0e\r\x11\r\x11\x0c\x0e\x0f\x0e\x0e*\x0f\x0e\x0e,\r\x0f\x0e\x0f\r\x0f\x0e\x0e\x0f\x0f\x0c\x0f\r\x10\x0e\x0e\r\x10\r,\x0f*\x0e+\r,\r+\x10)\x0f\x0e\x0e+\x0e\x0f\r\x0f\x0f\x0e\x0e\x0f\x0e\x0f\r\x0f\x0c\x10\r\x0f\r\x10\r\x0f\x0e\x10\r\x0e\r\x10\x0e\x0e\x0f\r\x0e\x0f\r\x10\r\x10\x0c,\x0e+\r+\x0f\x0f\x0e\x0e\x0e\x0f\r\x0e\x0f\x0e\x0e\x0f\x0e\x10\r\x0e\r\x10\r,\r,\r+\x0e\x0f\x0e\x0f\r\x0e\x0f\x0f\r\x0e\x0f\x10\x0c\x10\r\x0f\x0e\x0e\r\x0f\x0e\x0f\x0e\x0e\x0e\x0e\r\x11\r\x0e\x0e\x11\r+\x0c\x10\x0e\x0e\r\x10\r\x0f\x0e\x0f\x0e\x0f\r,\x0c\x10\x0e\x0e\r\x10\x0e\x0e\r\x10\x0e\x0e\r\x11\r\x0e\r\x0f\x0f\x0e\r\x11\x0c\x10\x0c\x10\r\x0f\r\x10\r\x10\r,\r\x0f\x0f)\x0f\x0e\x0e+\x0f*\x0f\x0e\r+\x0e\x00\r\x05'
TEMP_21 = b'&\x00\xbc\x01n<\r\x0e\r+\x0e\x10\x0f\r\r\x10\r\x0e\x10\x0e\r\x0f\r\x11\x0c\x0f\r\x11\x0c\x0f\r\x10\x0c,\r\x10\r\x10\r\x0f\r\x10\x0e\x0f\r\x0f\x0c\x0f\x0e+\x0f*\x0f*\x0e\x0f\r\x10\r+\x0e\x10\r\x0e\x0e\x10\r\x0f\r\x10\r\x0f\x0e\x0f\r\x0f\r\x0f\x0e\x0e\x0e\x0f\x0e\x0f\x0e\x0e\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x10\x0e\x0e\r\x0f\r\x10\r\x10\r\x0f\r\x0e\r\x11\x0f\x0c\x0e\x10\r\x10\r\x0f\x0e*\x0e+\x0e\x0e\x0e\x11\x0c\x0e\x0f\x0f\r\x0f\r\x00\x01Ur:\r\x0f\x0e*\x10\r\r\x10\x0e\x0f\r\x0f\r\x10\x0c\x0f\x0e\x0f\x0e\x10\x0c\x0f\r\x10\r\x0f\x0e+\x0e\x0f\r\x10\r\x0f\x0c\x10\r\x11\x0b\x10\r\x11\x0c+\x0e+\x0f*\x0f\x0e\r\x11\x0c,\x0c\x10\x0e\x0f\r\x10\r\x0f\r\x10\x0c\x0f\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0f\r\x0f\x0e\x0f\x0c\x10\x0e+\x0e\x10\x0c\x0f\x0e+\x0e*\r,\x10\x0e\x0c\x11\x0e\x0e\x0c,\r\x11\r+\r\x10\r,\x0e\x0f\x0c\x10\x0c\x10\x0e\x0e\r\x11\r\x0f\x0c\x10\x0e\x0f\r\x0f\r+\x0f+\x0e*\x0f*\x0f*\x0f+\r\x0f\x0e+\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x10\x0c\x0f\r\x10\x0e\x0e\r\x11\x0c\x0f\x0e\x0e\x0e\x0f\x0e\x0f\x0e\x0e\r\x0f\x0f\x0e\r\x11\x0c\x0f\r,\x0e*\x0f+\x0e\x10\x0c\x0f\r\x0f\x0e\x0f\x0e\x11\x0b\x10\x0c\x0f\r\x10\x0e\x0f\x0e*\r-\r+\r\x11\r\x0f\r\x0f\x0e\x0f\x0c\x11\r\x0f\x0c\x10\r\x10\r\x0f\x0e\x0f\x0c\x11\r\x0f\x0c\x10\x0f\x0e\r\x0f\x0e\x0f\x0c,\r\x11\x0c\x10\x0c\x11\x0c\x0f\x0e\x10\r\x0f\x0c,\x0e\x0f\x0e\x0e\r\x10\r\x0f\x0e\x0e\x0e\x0f\r\x11\x0b\x10\r\x10\r\x0f\r\x10\x0e\x0e\r\x10\r\x0f\x0e\x0f\r\x0f\r+\x0e-\r+\x11\x0c\r,\r+\r\x10\x0e*\x0f\x00\r\x05'
TEMP_22 = b'&\x00\xbc\x01o;\r\x0e\r,\x0f\x0e\r\x0f\x0f\x0e\x0e\x0e\r\x10\x0e\x0e\r\x0f\x0f\x0e\r\x11\r\x0e\x0f\x0e\r,\r\x0f\x0f\x0e\x0e\x0e\x0e\x0e\x0e\x0f\r\x11\x0b\x10\x0f)\x0e,\r,\x0e\x0f\x0e\x0e\x0e*\x0e\x10\r\x10\x0c\x11\x0b\x10\r\x11\r\x0f\r\x0e\x0f\x0e\r\x0f\x0e\x0f\x0e\x0f\r\x0f\r\x0f\x0e\x0f\x0e\x0f\x0e\x0e\x0e\x0e\x0e\x0f\x0e\x10\x0c\x0f\r\x10\x0b\x11\r\x10\x0c\x10\x0e\x0e\r\x10\x0e\x0f\r\x0f\r\x10\r\x0f\x0f*\r,\x0e\x0f\x0e\x0f\r\x0f\x0c\x10\r\x12\x0b\x00\x01Up:\x0e\x10\r*\x0e\x10\r\x0f\x0f\x0e\r\x0f\r\x10\x0b\x12\x0c\x10\r\x0e\x0f\x0f\r\x10\r\x10\x0c,\r\x0f\x0e\x0f\x0c\x10\r\x10\r\x10\x0c\x10\r\x0e\x0e+\x10)\x0e+\r\x11\x0c\x0f\x0e+\x0e\x10\x0e\x0e\r\x0f\r\x10\r\x10\x0c\x0f\x0e\x10\x0c\x11\r\x0f\r\x0f\r\x10\r\x0f\r\x10\r+\x0e\x0e\x0f\x0e\x0e+\x0e,\x0c,\x0f\r\x0e\x0f\x0e\x0f\r\x10\r+\x0e*\x0e\x10\r,\r\x0f\x0e\x0f\x0e\x10\x0c\x0f\r\x0e\x0f\x0f\r\x0e\x0f\x0f\r\x0f\x0e+\r+\x0e+\x0f+\x0e,\r*\x0f\x0f\r,\r\x0f\r\x10\r\x0e\x0f\x0f\r\x0e\x0f\x0f\x0c\x11\r\x0f\x0c\x0f\x0e\x10\r\x0f\x0e\x0f\r\x0e\x0f\x0f\r\x12\x0b\x0f\x0c\x10\x0e\x0f\r,\r+\x0f*\x0e\x0f\x0e\x0f\x0c\x10\x0e\x0f\r\x0f\r\x10\r\x10\x0c\x0f\x0e\x10\x0c-\r*\x0e+\x0f\x0f\x0c\x10\r\x0f\x0e\x0e\x0f\x0e\x0e\x10\x0c\x0f\x0e\x0f\r\x0f\x0e\x0e\x0e\x0f\x0f\x0e\r\x0f\x0e\x10\x0b\x10\r\x11\x0c+\x0e\x0f\x0e\x0e\x0e\x10\r\x0f\r\x0f\r\x11\x0c+\x0f\x0e\x0e\x0f\r\x10\x0c\x10\x0c\x11\r\x0f\x0c\x10\r\x0f\r\x10\x0e\x0f\x0c\x11\x0c\x10\x0c\x10\r\x11\x0b\x11\x0c\x10\x0c,\x0e\x0f\x0e\x0f\x0c-\x0c-\x0c,\r\x11\r*\x0f\x00\r\x05'
TEMP_23 = b'&\x00\xbc\x01p8\x0f\r\x0e,\x0e\x0e\x0e\x0e\x0f\x0e\x0e\x0f\r\x0f\x0f\r\x0e\x0f\x0e\x0e\x0f\x10\x0c\x0e\x0f\x0f\r+\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x10\r\x0e\x0e\x10\r\x0e\x0e+\x0e+\x0e+\x0f\x0f\r\x0e\x0f*\x0e\x10\r\x0e\x0e\x0f\x0f\x0e\r\x11\x0b\x0f\x0e\x0f\x0e\x0e\x0f\x0f\x0c\x0f\x10\r\x0f\x0f\r\x0e\x0f\x0e\r\x0f\x0e\x0f\x0f\x0e\x0c\x0f\x0e\x10\r\x0e\x0e\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0f\r\x0e\x0f\x0e\x0e\x0f\r\x0e\x11\x0c+\x0f+\r\x0e\x0f\x0e\x0e\x0f\x0e\x10\x0c\x0e\x0f\x00\x01Tr9\x0e\x0e\x0f*\x0e\x10\r\x0e\x0e\x10\r\x0e\x0e\x0f\r\x0f\x0f\x0f\r\x0e\x0e\x10\r\x0e\x0e\x10\r,\x0c\x10\x0e\x0e\r\x0f\x0f\x0f\x0c\x10\x0f\x0e\r\x0f\r+\x0f*\x0f*\x10\r\x0e\x0f\r+\x10\r\x0e\x0e\x0e\x0f\r\x0f\r\x10\r\x0f\x0f\x0e\r\x10\x0f\r\x0e\x0f\r\x0f\x0e\x0e\x0e\x0f\r,\r\x0f\x0e\x0f\x0e*\x0f*\x0f+\x10\x0c\x0f\x0e\r\x0f\x0f*\x0e+\x0f*\x0e\x0f\r+\x0f\x0e\x0e\x0e\x0f\x0f\r\x0e\x0f\x0f\x0e\r\x0f\x0f\r\x10\x0c\x0f\r,\x0e+\r,\x0e+\x0e+\x0e,\r\x0e\x0f*\x0f\x0f\x0c\x10\x0f\r\x0e\x0f\x0e\x0e\r\x0f\x0e\x10\x0c\x0f\x0e\x10\x0e\r\x0f\x0e\x0e\x0f\x0e\x0e\x0f\r\x0f\x0e\x0e\x0e\x0e\x0f\r\x0f\x0f*\x0f*\x0f*\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0e\x0f\r\x0f\x0e\x0f\r\x10\x0e\r\x0e+\x0f*\x0f+\r\x0f\x0f\x0e\r\x0f\x0f\x11\x0c\r\x0e\x0f\x0e\x0e\x0f\x0e\x0e\x0f\x0e\x0e\r\x0f\x0e\x0f\x0e\x0e\r\x10\r\x0f\r\x0f\x10)\x0f\x0e\r\x11\x0c\x0f\x0e\x0f\x0e\x0e\r\x10\x0e*\x0f\x0e\r\x10\r\x0f\r\x11\x0c\x0f\x0f\x0f\x0c\x0f\r\x10\x0e\x0f\x0c\x10\x0f\x0e\x0c\x0f\x10\r\x0e\x13\t\x0f\x0e\x10\x0c+\x0f*\x0f\x0e\r,\x0e+\x0e+\r\x0f\x0f*\x0f\x00\r\x05'
TEMP_24 = b'&\x00\xbc\x01o9\x0f\x0f\r,\r\x0e\x0e\x10\r\x0f\r\x0f\x0e\x10\x0c\x0f\x0e\x10\x0c\x10\r\x0e\x0f\x0f\x0f\x0c\x0f*\x0f\x0e\r\x10\x0e\x0e\x0e\x0e\x0e\x10\r\x0e\x0e\x10\r+\r,\x0e+\x10\r\x0e\x0f\r,\r\x0e\x0e\x10\r\x10\r\x0e\r\x10\x0e\x0f\x0c\x0f\r\x11\x0b\x10\x0e\x10\x0f\r\r\x0f\r\x10\x0e\x0e\r\x12\x0b\x0f\r\x0f\x0f\x0f\r\x0e\x0e\x10\x0c\x10\x0e\x0e\x0e\x0e\x0e\x0f\r\x10\x0e\x0e\x0f\r\x0e\x0f\r\x0f\x0f\x0e\r,\r,\x0f\r\x0e\x0f\r\x0f\x0e\x0f\r\x10\x0e\x00\x01Ss8\x0e\x10\r,\r\x0f\x0e\x0f\x0e\x0e\r\x10\r\x0f\r\x11\x0c\x0e\r\x11\r\x0e\r\x11\x0c\x12\x0b+\x0e\x0f\r\x10\r\x10\r\x0e\x0f\x0f\r\x0f\x0e\x0f\x0c,\x0e+\x0e,\r\x0e\x10\r\x0e+\r\x0f\x0f\x0e\x0e\x0e\x10\x0e\x0b\x11\r\x0f\x0e\x0e\x0e\x0f\x0e\x11\x0c\x0e\r\x10\x0e\x0e\x0e\x0e\x0e+\x0f\x0f\r\x0e\r-\x0e*\x0e+\x0f\x10\x0c\x0e\x0e\x0f\x0e\x0f\x0e\x0f\x0c\x0f\x0e+\x0f*\x0e\x0f\x0e\x0f\r\x0f\r\x0f\x0e\x0e\x0e\x11\x0c\x0f\x0e\x0e\r\x10\x0f)\x0e,\x0f+\x0c+\x0f*\x0f*\x0f\x0e\r,\x0e\x0f\r\x10\x0c\x10\r\x0f\r\x10\x0e\x0e\x0e\x0f\r\x10\r\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\x0e\x0e\r\x10\x0e\x0e\x0e\x0f\x0f\r\x0e+\x0e+\r,\x0f\x0e\r\x0e\x0e\x10\x0e\x0f\r\x0e\x0e\x0f\x0e\x0f\r\x0e\x0e\x10\x0b.\r+\x0e+\x0e\x0e\x0e\x10\r\x0f\x0f\x0e\r\x0e\x10\x0e\x0f\x0e\r\x0e\r\x0f\x0f\x0e\x0e\x10\r\x0f\r\x0e\x0e\x10\r\x0e\r\x11\x0c,\x0f\x0e\r\x10\x0c\x0f\x10\x0e\x0c\x0f\x0f\x0f\r+\r\x10\x0e\x0e\r\x10\x0e\x0f\x0c\x11\x0c\x10\x0c\x0f\x0e\x10\x0c\x11\x0c\x10\x0c\x10\x0e\x0e\r\x11\r\x0e\r\x0f\r\x11\x0c,\x0e\x0f\x0e+\x0e*\x11(\x0f*\x0f\x0e\x0e+\x0e\x00\r\x05'