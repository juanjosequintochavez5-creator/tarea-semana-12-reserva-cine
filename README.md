# Tarea Semana 12 - Reserva de un asiento en sala de cine

## Estudiante

Juan José Quinto Chávez

## Objetivo

Desarrollar un programa en Python que permita reservar un asiento
en una sala de cine de 3 filas por 4 columnas utilizando una matriz
y bucles anidados.

## Descripción

El programa crea una matriz de 3 filas y 4 columnas.

El valor 0 representa un asiento libre.

El valor 1 representa un asiento reservado.

El usuario debe ingresar la fila y la columna del asiento que desea
reservar. Luego, el programa cambia el valor de ese asiento a 1 y
muestra el estado completo de la sala.

## Funcionamiento

El programa solicita:

- La fila del asiento, de 0 a 2.
- La columna del asiento, de 0 a 3.

Después registra la reserva y muestra la matriz completa.

## Ejemplo

Si el usuario selecciona:

Fila: 1

Columna: 2

El resultado será:

0 0 0 0
0 0 1 0
0 0 0 0

## Archivo principal

El programa se encuentra en el archivo:

reserva_cine.py

## Cómo ejecutar

Abrir una terminal en la carpeta del proyecto y ejecutar:

python reserva_cine.py
