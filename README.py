# 🚀 Automated Job Application System

## 📋 Descripción
Herramienta de automatización desarrollada en **Python** para optimizar la búsqueda laboral. 
El script permite el envío masivo pero personalizado de correos electrónicos, adjuntando CV y Carta de Presentación específicos, iterando sobre una base de datos de contactos en Excel.

Este proyecto resuelve la problemática del envío manual repetitivo, reduciendo el tiempo de postulación en un 90% y eliminando errores humanos.

## 🛠️ Tecnologías
* **Python 3.x**
* **Pandas:** Manipulación y limpieza del dataset de contactos (ETL).
* **Smtplib:** Gestión del protocolo de envío de correos (Gmail).
* **Regex:** Validación y sanitización de emails.

## ⚙️ Funcionalidades
✅ **Personalización Inteligente:** Detecta si existe el nombre del reclutador o la empresa y adapta el saludo/asunto automáticamente.
✅ **Manejo de Adjuntos:** Envía CV y Carta de Presentación en un solo correo.
✅ **Clean Data:** Limpia espacios vacíos y errores de tipeo en los emails.
✅ **Anti-Spam:** Incluye pausas de seguridad entre envíos.

## 🚀 Cómo usar este código
1. Clonar el repositorio.
2. Instalar dependencias: `pip install -r requirements.txt`
3. Crear un archivo `contactos.xlsx` con las columnas: `Nombre`, `Email`, `Empresa`.
4. Ejecutar `main.py` e ingresar las credenciales de aplicación de Google.

---
*Desarrollado por [Rocío Livingston](https://www.linkedin.com/in/rociolivingston/)*
