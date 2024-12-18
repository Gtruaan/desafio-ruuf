# ¿Cuántos paneles caben? 🤠

Hecho por Gustavo Truan para la postulación a Junior Dev en Ruuf.

[Click aquí para el video de explicación](https://youtu.be/eVajIn7CYU0)

## Información de la solución 📝

La solución fue programada en Python 3.10.7. Las funciones pedidas se encuentran `functions.py`. Cada función recibe los siguientes parámetros:
* `cont_x`: Largo del techo
* `cont_y`: Ancho del techo
* `tile_x`: Largo de los paneles
* `tile_y`: Ancho de los paneles
Se programaron las tres funciones sugeridas:
* `rectangle_fit`: Cuantos paneles caben en un techo rectangular.
* `isosceles_fit`: Cuantos paneles caben en un techo con forma de triángulo isósceles.
* `intersection_fit`: Cuantos paneles caben en un techo con forma de rectángulos intersectados.

## Supuestos 🤔

Se realizan los siguientes supuestos:
* Los paneles sólo pueden ser rotados en 90°.
* Los paneles tienen dimensiones enteras.
* Para la función que cubre la intersección de dos rectángulos, se asume que los rectángulos se intersectan en un cuarto de su área, con un vértice de un rectángulo en el centro del otro.