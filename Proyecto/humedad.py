import serial

# Configuración del puerto serial
puerto_serial = serial.Serial('COM3', 9600, timeout=1)  # Reemplaza 'COMX' con el nombre correcto del puerto

try:
    while True:
        # Lee una trama de 8 bytes desde el puerto serial
        trama_recibida = puerto_serial.read(8)

        # Muestra los datos de la trama recibida en formato binario
        if trama_recibida:
            datos_binarios = ' '.join(format(byte, '08b') for byte in trama_recibida)
            print(f'Trama recibida (binario): {datos_binarios}')

except KeyboardInterrupt:
    print("Programa interrumpido por el usuario")

finally:
    # Cierra el puerto serial al finalizar
    puerto_serial.close()
