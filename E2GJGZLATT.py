try: 

    import requests 

except ImportError: 

    os.system('pip install requests') 

    print('Installing requests...') 

    print('Ejecuta de nuevo tu script...') 

    exit()
try: 

    import os 

except ImportError: 

    os.system('pip install os') 

    print('Installing os...') 

    print('Ejecuta de nuevo tu script...') 

    exit() 

try: 

    import sys 

except ImportError: 

    os.system('pip install sys') 

    print('Installing sys...') 

    print('Ejecuta de nuevo tu script...') 

    exit() 

try: 

    import webbrowser 

except ImportError: 

    os.system('pip install webbrowser') 

    print('Installing webbrowser...') 

    print('Ejecuta de nuevo tu script...') 

    exit()

try: 

    from bs4 import BeautifulSoup as bs 

except ImportError: 

    os.system('pip install BeautifulSoup') 

    print('Installing BeautifulSoup...') 

    print('Ejecuta de nuevo tu script...') 

    exit()
    


""" Gustavo de Jesús González Salazar - Luis Alberto Trejo Tovar
Primero lo que hace el script es que importa los módulos y en caso de que no
esten instalados los instala y se cierra el programa y asi sucesivamente con
los demas import, despues pone dos input en los que el usuario
tiene que introducir de que página a que página quiere buscar las noticias,
y en el tercer input tenemos que ingresar las siglas de la facultad a
investigar, después en el if si el primer rango es un número mayor al otro los
cambia de lugar para que el número más grande siempre vaya al final, luego va
el rango que tomara los valores de inicio de rango y fin de rango para
despues buscar en la página de la UANL en noticias desde esos números, luego
si el estatus de la página marca un error tipo 200 nos imprime que no encontró
la página, despues se utiliza la librería de beautifulsoup para buscar dentro
de las paginas que señalamos anteriormente algo referente con las siglas de
la facultad que ingresamos y si encuentra algo nos abrira en nuestro navegador
los links de donde encontro información y en caso de no ecnotrar información
entra el break y ahi termina el programa :)"""

print("Este script navega en las páginas de noticas de la UANL")
inicioRango = int(input("Pagina inicial para buscar: "))
finRango = int(input("Pagina final para buscar: "))
dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
if inicioRango > finRango:
    inicioRango,finRango = finRango,inicioRango
for i in range (inicioRango,finRango,1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get (url)
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    else:
        soup = bs(pagina.content,"html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content,"html.parser")
                parrafos = soup2.select("p")    
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print ("Abriendo",url2)
                        webbrowser.open(url2)
                        break
    

