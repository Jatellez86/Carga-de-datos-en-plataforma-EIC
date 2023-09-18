# Importa las bibliotecas necesarias para la automatización del navegador con Selenium
# **********************************************************************************************
#  @Nombre: Boot carga de datos ICS
#  @Autor: Javier Tellez
#  @Fecha: 20230325
#  @Cambios:
#  @Ayudas:
# **********************************************************************************************
#----------------------------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time 
import os
import shutil
from datetime import date
from datetime import datetime, timedelta
import pandas as pd 
import os
import glob


# Definicion de variables ---------------------------------------------------------------------
driver = False
session_id = False
loginState = False
user = 'user_prueba'
password = 'pwd_prueba'
fecha_actual = date.today()
fecha_anterior = fecha_actual - timedelta(days=1)

# carpeta a correr

# Definir la ruta del directorio
ruta_directorio = r"G:\Unidades compartidas\GM_OP_ANALISIS_DE_DATOS\21.1 validacion kms\RESPUESTA_UF17"

# Obtener los elementos del directorio
elementos = os.listdir(ruta_directorio)

# Filtrar sólo las carpetas
carpetas = [carpeta for carpeta in elementos if os.path.isdir(os.path.join(ruta_directorio, carpeta))]

# Crear una lista vacía para almacenar las rutas de los archivos encontrados
rutas_archivos_encontrados = []

# Verificar si existe algún archivo .csv que contenga la cadena en cada carpeta
for carpeta in carpetas:
    ruta_carpeta = os.path.join(ruta_directorio, carpeta)
    archivos_csv = glob.glob(os.path.join(ruta_carpeta, "*resumen_respuestas.csv*"))

    if archivos_csv:
        for archivo in archivos_csv:
            rutas_archivos_encontrados.append(archivo)

# Imprimir la lista de rutas de archivos encontrados
print("Rutas de archivos encontrados:")
for ruta_archivo in rutas_archivos_encontrados:
    print(ruta_archivo)


print(type(rutas_archivos_encontrados))

# Obtén el primer elemento de la lista
primer_archivo_csv = rutas_archivos_encontrados[0]

# Leer el archivo CSV con Pandas
df_objecion = pd.read_csv(primer_archivo_csv)

columnas = ['fecha_viaje', 'id_fase_v', 'km_a_reclamar', 'respuesta', 'servicio_retoma', 'ruta']

lista_objeciones = df_objecion[columnas]

print(lista_objeciones.head(5))

# Características en el Web Driver ------------------------------------------------------------
session_id = False
loginState = False
driver = False
options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# Functions -----------------------------------------------------------------------------------
def openBrowser():
    global session_id
    global loginState
    global driver    
    try:
        if session_id == False:        
            driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options)
            driver.implicitly_wait(40)  # seconds
            driver.maximize_window()
            session_id = driver.session_id
        return True
    except Exception as e: 
        print(str(e))
        return False

# Logic --------------------------------------------------------------------------------
openBrowser()


# pagina principal de Transmitools
driver.get('http://transmitools.transmilenio.gov.co/')
time.sleep(1)


# enviar llaves de usuario y contraseña

driver.find_element('xpath','//*[@id="texto"]/form/div[1]/input').send_keys(user)
time.sleep(1)
driver.find_element('xpath','//*[@id="texto"]/form/div[2]/input').send_keys(password)
time.sleep(1)
driver.find_element('id','ingresar').click()
time.sleep(1)


for i in lista_objeciones['id_fase_v']:
    
    try:
        driver.refresh()
        id_fase_v = lista_objeciones[lista_objeciones['id_fase_v'] == i]
        id = id_fase_v['id_fase_v'].iloc[0]
        id_str = str(id)
        observacion = id_fase_v['respuesta'].iloc[0]
        km_reclamar = id_fase_v['km_a_reclamar'].iloc[0]

        driver.get('http://transmitools.transmilenio.gov.co/EIC/ShowInfoKpif5.jsp?IdKpi=10')
        time.sleep(2)
        driver.find_element('xpath','//*[@id="wizard"]/form/div[1]/ul/li[2]/a/div').click()
        time.sleep(2)
        driver.find_element('xpath','//*[@id="info_etapa1_filter"]/label/input').clear()
        time.sleep(2)
        driver.find_element('xpath','//*[@id="info_etapa1_filter"]/label/input').send_keys(id_str)
        time.sleep(2)
        driver.find_element('xpath','//*[@id="info_etapa1_filter"]/label/input').send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element('xpath','//*[@id="info_etapa1"]/tbody/tr/td[50]/a').click()
        time.sleep(2)
        driver.find_element('id','observacion').send_keys(observacion)
        time.sleep(2)
        driver.find_element('xpath','//*[@id="reclamar"]/tbody/tr[2]/td[2]/div/label').click()
        time.sleep(2)
        driver.find_element('id','textkma').clear()
        time.sleep(2)
        driver.find_element('id','textkma').send_keys(km_reclamar)
        time.sleep(2)
        driver.find_element('xpath','//*[@id="reclamar"]/tbody/tr[3]/td[2]/div/label').click()
        time.sleep(2)

        #ruta original
        ruta = id_fase_v['ruta'].iloc[0]

        # Reemplazar las barras invertidas simples con barras invertidas dobles
        ruta_normalizada = ruta.replace("\\", "\\\\")

        # Imprimir la ruta normalizada
        print(ruta_normalizada)

        driver.find_element('id','file').send_keys(ruta_normalizada)
        time.sleep(2)
        driver.find_element('id','form-file').click()
        time.sleep(2)
        driver.find_element('id','LoadFile').click()
        time.sleep(30)
        driver.find_element('xpath','/html/body/div[9]/div[2]/div/a').click()
        time.sleep(30)

        print(id)
    except Exception as e:
        print("Error:", str(e))
        continue
            
        
