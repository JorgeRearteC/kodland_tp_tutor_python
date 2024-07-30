# KODLAND TP TUTOR

Este es un juego simple desarrollado usando la librería PyGame en Python. 
En el juego, el jugador controla un personaje que puede moverse verticalmente y disparar balas para eliminar enemigos.
El objetivo es eliminar todos los enemigos para ganar.

## Requisitos

Para ejecutar este juego, necesitarás tener Python y PyGame instalados en tu sistema. Aquí están los requisitos:

- **Python**: 3.6 o superior
- **PyGame**: 2.0 o superior

## Instalación

1. **Clona el repositorio con la consola de comandos o terminal**:
   git clone https://github.com/JorgeRearteC/kodland_tp_tutor_python.git
   cd tu-repositorio

2. **Crea y activa un entorno virtual (opcional, pero recomendado)**:
    python -m venv env
    source env/bin/activate  # En Windows: env\Scripts\activate

3. **Instala las dependencias**:
    pip install -r requirements.txt

## Cómo Jugar

1. **Inicia el juego**
    python main.py

2. **Selecciona la cantidad de enemigos**
    Usa las flechas izquierda y derecha para seleccionar el número de enemigos (de 1 a 5).
    Presiona Enter para confirmar tu selección.

3. **Controles**
    Flecha Arriba: Mueve el personaje hacia arriba.
    Flecha Abajo: Mueve el personaje hacia abajo.
    Espacio: Dispara una bala hacia la derecha.

4. **Objetivo**
    El objetivo es eliminar todos los enemigos que aparecen en la pantalla.
    Los enemigos se generarán en posiciones aleatorias y permanecerán estáticos.
    Cuando elimines todos los enemigos, se reiniciará el juego para que puedas jugar nuevamente.

5. **Información en pantalla**
    Balas restantes: Muestra la cantidad de balas que puedes disparar.
    Enemigos restantes: Muestra la cantidad de enemigos que quedan en la pantalla.