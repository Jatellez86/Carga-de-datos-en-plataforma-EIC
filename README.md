# Carga-de-datos-en-plataforma-EIC
Este escrip realizar una carga automatica, basados en flujo logico de informacion que reposa en una carpeta con archivos y con datos en columnas en un .csv

# 🤖 Selenium Web Automation for Transmitools

## 📝 Descripción

Este script de Python 🐍 utiliza Selenium para automatizar tareas en la página web de Transmitools. Realiza acciones como login y actualización de información basado en un DataFrame de Pandas 🐼.

## 🛠️ Dependencias

- Python 3.x 🐍
- Selenium 🌐
- pandas 🐼
- datetime ⏰
- os 💻
- shutil 📂
- glob 🌐

## 🔄 Funcionamiento

1. **🔒 Autenticación**: Utiliza un nombre de usuario y contraseña predefinidos para hacer login en Transmitools.
2. **📅 Fechas**: Calcula la fecha actual y la fecha anterior.
3. **📂 Directorio de trabajo**: Busca archivos `.csv` específicos en un directorio y subdirectorios.
4. **📊 DataFrame de Pandas**: Carga un archivo `.csv` en un DataFrame de Pandas.
5. **🌐 Automatización Web**: Navega a través de diferentes páginas y formularios en Transmitools, llenando campos basados en el DataFrame.
6. **📤 Subir Archivos**: Sube archivos al formulario web desde una ruta local.

## 🚀 Cómo usar

1. Instale todas las dependencias 🛠️.
2. Actualice las variables `user` y `password` con su nombre de usuario y contraseña de Transmitools 🔒.
3. Modifique `ruta_directorio` para apuntar al directorio donde desea buscar los archivos `.csv` 📂.
4. Ejecute el script 🚀.

## ⚠️ Nota

Este script tiene tiempos de espera (`time.sleep()`) para asegurar que las páginas web tengan tiempo de cargar. Puede necesitar ajustar estos valores según su conexión a Internet.

