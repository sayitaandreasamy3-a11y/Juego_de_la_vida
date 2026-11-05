JUEGO DE LA VIDA
 
Bibliotecas principales:Pygame, NumPy y Streamlit  
Integrates:
Andrea Samantha Cruz Arrdondo
Adriana Paola Lopez Jimenez
Hugo Salvador Juarez Velazquez

# RESUMEN
Nuestro proyecto consiste en el desarrollo de una simulación del Juego de la Vida.El programa nos muestra un tablero donde hay células vivas y muertas, las cuales van cambiando dependiendo de ciertas reglas. 

El proyecto cuenta con dos versiones. La primera es una aplicación de escritorio desarrollada con Pygame, en la que el usuario puede interactuar con las células mediante el mouse y controlar la simulación utilizando el teclado. La segunda es una aplicación web desarrollada con Streamlit, que permite visualizar el tablero, generar células aleatorias, avanzar generaciones y observar la evolución del sistema. Donde en ambos nos muestra un tablero donde hay células vivas y muertas, las cuales van cambiando dependiendo de las reglas

Ya que nuestro objetivo fue crear una aplicación en la que se pudiera observar fácilmente cómo van cambiando las células y tener botones para controlar la simulación.


# INTRODUCCIÓN

Planteamiento del problema
El Juego de la Vida representa este comportamiento mediante una cuadrícula de células que pueden estar vivas o muertas. Aunque sus reglas son sencillas, los resultados pueden generar diferentes patrones y comportamientos dependiendo de la posición inicial de las células.

El problema que aborda este proyecto consiste en desarrollar un programa capaz de representar estas células, aplicar sus reglas de evolución y mostrar visualmente los cambios que ocurren en cada generación.

Objetivo general

Nuestro objetivo es representar de manera visual el Juego de la Vida mediante Python, implementando las reglas de evolución de las células y utilizando herramientas  para visualizar el comportamiento del sistema.

Objetivos particulares

-Comprender cómo funciona el Juego de la Vida y las reglas que siguen las células
-Crear un tablero utilizando matrices con NumPy.
-Programar las reglas para que las células puedan nacer, vivir o morir.
-Crear una versión del juego en una ventana utilizando Pygame.
-Permitir que el usuario pueda cambiar las células utilizando el mouse y la tecla de espacio y iniciarlo con la tecla r.
-Crear una versión del juego que se pueda utilizar desde una página web con Streamlit.
-Realizar pruebas para comprobar que el juego funcione correctamente

# SOLUCIÓN Y EVIDENCIA

Para resolverlo se implementó una simulación del juego de la vida en la que se representa un conjunto de células dentro de un tablero dividido en pequeñas celdas incorporando herramientas que permiten visualizar e interactuar con el tablero tanto en una aplicación de escritorio como en una aplicación web
El juego nos permite experimentar con diferentes configuraciones iniciales y observar cómo cambian con el paso de las generaciones. Así, quien lo juegue pueda descubrir diferentes patrones y comportamientos que surgen a partir de reglas sencillas.

Desiciones Tecnicas 
Python: fue el lenguaje que utilizo para programar el juego
NumPy: Permitió trabajar con arreglos y organizar los datos del tablero.
Streamlit: Lo utlizamos para crear la aplicación que se puede visualizar desde el navegador.
Pygame: Lo utlizamos  para  que tambien se desarrollara la versión de escritorio del juego.
GitHub: Finalmente lo utlizamos para guardar el proyecto y tener los archivos organizados en un repositorio.

Resultados obtenidos

Como resultado, se obtuvo un Juego de la Vida funcional, con la que es posible observar los cambios que experimentan las células durante las diferentes generaciones.

Durante las pruebas se puede observar que una célula no permanece necesariamente en el mismo estado, ya que su supervivencia depende de la cantidad de vecinas vivas que tenga. También se pueden generar diferentes patrones a partir de distintas configuraciones iniciales.

Lo que nos permitio:
-Crear configuraciones aleatorias de células.
-Avanzar paso a paso entre generaciones.
-Observar la evolución automática de 30 generaciones.
-Limpiar el tablero para comenzar una nueva simulación.
-Explorar los diferentes patrones que se forman durante el juego.

Estos resultados permiten comprobar que las reglas programadas producen cambios en el tablero y que la simulación cumple con su propósito de representar visualmente el Juego de la Vida.

Reglas del Juego de la Vida
1.-Una célula con menos de dos vecinos vivos muere.
2.-Una célula con dos o tres vecinos sobrevive.
3.-Una célula con más de tres vecinos muere.
4.-Una célula muerta con exactamente tres vecinos revive
Repositorio
https://github.com/sayitaandreasamy3-a11y/Juego_de_la_vida.git


# CONCLUSIONES

El desarrollo del Juego de la Vida nos permitio aplicar nuestros conocimientos de programación, incluso nos llevo al punto de investigar y conocer conceptos y tambien ejecutar cosas que se nos complicaban.

Durante el desarrollo comprendimos la importancia de utilizar matrices para representar información y de aplicar correctamente las reglas que determinan los cambios de cada generación.

También se trabajamos con diferentes bibliotecas de Python, lo que permitió desarrollar visualmente el juego de la vida pero mediante Pygame y posteriormente volver a adaptar el proyecto para visualizarlo en una aplicación web utilizando Streamlit.

Finalmente este proyecto nos permitió fortalecer los conocimientos de programación y comprender cómo una serie de reglas sencillas puede producir diferentes comportamientos dentro de un sistema.

# REPRODUCIBILIDAD

1.-Para ejecutar el proyecto se necesita:

- Sistema operativo Windows.
- Python 3.13.
- Visual Studio Code (recomendado).
- Git para administrar el repositorio.
- Conexión a Internet para instalar las bibliotecas.

2.-Ingresar a la carpeta del proyecto:
```bash
- cd Juego_de_la_vida

3.-Crear un entorno virtual:
- python -m venv .venv

4.-Activar el entorno virtual en Windows:
- .venv\Scripts\Activate.ps1

Instalar las bibliotecas necesarias para la aplicación web:
- pip install -r requirements.txt

Para ejecutar la versión de escritorio también se necesita instalar Pygame:
- pip install pygame


## 5.3 Ejecución de la versión de escritorio

Para ejecutar el juego original desarrollado con Pygame, utilizar el siguiente codigo en la terminal:
- python Juego_vida.py

Después de ejecutarlo aparecerá una ventana con el tablero del Juego de la Vida, donde se podrán colocar células y controlar el juego por medio de los controles

Como jugarlo:
-Clic del mouse: permite activar o desactivar una célula.
-Barra de espacio: inicia o pausa la simulación.
-Tecla R: genera una nueva distribución aleatoria de células.
-Cerrar ventana: termina la ejecución del programa.

## 5.4 Ejecución de la versión web

Para ejecutar la aplicación web localmente utilizamos:
streamlit run app.py

El comando abrirá la aplicación en el navegador, donde se podrá interactuar con los controles y observar la evolución de las células.

Como usarlo:
-Aleatorio: genera una distribución de células en el tablero.
-Siguiente generación: calcula y muestra la generación siguiente.
-Ejecutar 30 generaciones: reproduce una secuencia de 30 generaciones.
-Limpiar:elimina todas las células y reinicia el contador.

#Dependencias

Las bibliotecas principales que utilizamos son:
streamlit
numpy
pygame
El archivo `requirements.txt` contiene las dependencias de la versión web. 

## Repositorio y streamlit

Repositorio de GitHub:
https://github.com/sayitaandreasamy3-a11y/Juego_de_la_vida.git


**Aplicación publicada en Streamlit:**

Local URL: http://localhost:8501
  Network URL: http://192.168.1.82:8501



