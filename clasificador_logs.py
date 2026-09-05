import os
import shutil

ruta_origen = "logs_origen"

carpetas_destino = {
    ".log_app_1": "App1_Logs",
    ".log_app_2": "App2_Logs",
    ".log_app_3": "App3_Logs"
}

archivos = os.listdir(ruta_origen)

for archivo in archivos:
    ruta_completa = os.path.join(ruta_origen, archivo)

    if os.path.isdir(ruta_completa):
        continue

    nombre, extension = os.path.splitext(archivo)

    if extension in carpetas_destino:
        carpeta_destino = carpetas_destino[extension]

        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)

        shutil.move(ruta_completa, os.path.join(carpeta_destino, archivo))
        print(f"Movido: {archivo} -> {carpeta_destino}")
    else:
        print(f"Extension no reconocida, se omite: {archivo}")

print("Clasificacion de logs finalizada.")