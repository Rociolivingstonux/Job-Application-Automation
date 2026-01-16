"""
AUTOMATIZACIÓN DE POSTULACIONES LABORALES
-----------------------------------------
Autor: Rocio Livingston
Descripción: Script para envío masivo y personalizado de correos 
con adjuntos múltiples (CV + Carta de Presentación).
"""

import pandas as pd
import smtplib
import time
import os
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from getpass import getpass

# --- CONFIGURACIÓN ---
ASUNTO_BASE = "CV | Perfil Data Science & Admin"
NOMBRE_CV = "CV_Ejemplo.pdf"     
NOMBRE_CARTA = "Carta_Ejemplo.pdf"

def limpiar_email(email):
    """Elimina espacios y valida formato básico de email."""
    email_limpio = re.sub(r'\s+', '', str(email))
    return email_limpio

def enviar_correos(ruta_excel, tu_email, tu_password):
    # 1. Cargar Base de Datos
    try:
        df = pd.read_excel(ruta_excel)
        df = df.fillna('')
        print(f"✅ Base cargada: {len(df)} registros.")
    except Exception as e:
        print(f"❌ Error al leer Excel: {e}")
        return

    # 2. Conexión SMTP
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(tu_email, tu_password)
        print("✅ Conexión establecida.")
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return

    print("-" * 50)

    # 3. Iteración
    for index, row in df.iterrows():
        email_destino = limpiar_email(row['Email'])
        nombre = str(row['Nombre']).strip()
        empresa = str(row['Empresa']).strip()

        if "@" not in email_destino:
            continue

        # Personalización
        saludo = f"Hola {nombre}," if nombre else "Estimados,"
        
        if empresa:
            texto_empresa = f"al equipo de {empresa}"
            asunto_final = f"{ASUNTO_BASE} - Para {empresa}"
        else:
            texto_empresa = "a su equipo de trabajo"
            asunto_final = ASUNTO_BASE

        # Cuerpo del mail
        cuerpo = f"""
        {saludo}

        Te escribo con entusiasmo para presentar mi postulación {texto_empresa}.
        
        Soy profesional en ...[...]
        
        Adjunto mi CV y Carta de Presentación.
        
        Saludos cordiales,
        """

        msg = MIMEMultipart()
        msg['From'] = tu_email
        msg['To'] = email_destino
        msg['Subject'] = asunto_final
        msg.attach(MIMEText(cuerpo, 'plain'))

        # Adjuntos
        for archivo in [NOMBRE_CV, NOMBRE_CARTA]:
            try:
                with open(archivo, "rb") as f:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename={archivo}")
                msg.attach(part)
            except FileNotFoundError:
                print(f"⚠️ No se encontró: {archivo}")

        # Envío
        try:
            server.send_message(msg)
            print(f"🚀 Enviado a: {email_destino}")
            time.sleep(40) 
        except Exception as e:
            print(f"❌ Error: {e}")

    server.quit()
    print("🏁 Fin del proceso.")

if __name__ == "__main__":
    email = input("Email: ")
    pw = getpass("Contraseña App: ")
    enviar_correos("contactos.xlsx", email, pw)
