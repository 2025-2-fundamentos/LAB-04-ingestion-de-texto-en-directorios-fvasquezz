# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import os
import pandas as pd

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    data_set=generar_dataset()
    entrega_base(data_set)

def encontrar_elementos(x):
    if "test" in x:
        return "test"
    elif "train" in x:
        return "train"
    else:
        print("Se encontro una carpeta no esperada")
        return "Unknown"
    
def find_target(x):
    if "negative" in x:
        return "negative"
    elif "positive" in x:
        return "positive"
    elif "neutral" in x:
        return "neutral"
    else:
        print("Se encontro un target inesperado")
        return "Unknown"
    
def generar_dataset():    
    carpeta="files/input"
    subcarpetas=os.listdir(carpeta)
    datasets={}

# Inicializar listas vacías para cada subcarpeta de manera 
# que tenga todas las claves necesasrias y las frases en un mismo lugar
    for i in subcarpetas:
        datasets[i]=[]

#Entro en cada subcarpeta
    for root, _, files in os.walk(carpeta):
# Entro en cada archivo y uno por uno leo lo que hay en ellos        
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
# Hago una "pequeña limpieza" de cada linea
                for line in f:
                    phrase=line.strip()
# Busco el target y carpetas correspondiente a cada una de las frases 
# para finalmente agregarlas al diccionario
                    target=find_target(file_path)
                    enc_carpeta=encontrar_elementos(file_path)
                    datasets[enc_carpeta].append([phrase,target])
    return datasets

def entrega_base(x):
    columnas =["phrase","target"]
    carpeta_salida="files/output"
    dfs= {}
    #Creo la carpeta de salida si no existe
    os.makedirs(carpeta_salida, exist_ok=True)
    for nombre, datos in x.items():
        df=pd.DataFrame(datos, columns=columnas)
    #Se crea la ruta completa del archivo y posteriormente se guarda el DataFrame en un archivo CSV
    #como CSV con el indice desactivado
        archivo=os.path.join(carpeta_salida, f"{nombre}_dataset.csv")
        df.to_csv(archivo, index=False)
    #Se almacena el DataFrame en el diccionario de DataFrames por si 
    #se quiere usar despues para algún análisis
        dfs[nombre]=df
    return dfs