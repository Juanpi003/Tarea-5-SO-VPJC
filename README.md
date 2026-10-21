# Tarea-5-SO-VPJC
Implementación del algoritmo de cadena de referencias en Python

## Compilación y ejecución

Para compilar el código solo se necesita ejecutar el archivo como 
```
python3 cadena\_referencias.py
```

O 

```
python cadena\_referencias.py
```

El código funciona en tres pasos, primero te pregunta el tamaño de página y luego la lista de direcciones referenciadas, en el orden en que ocurren. Después, una función recorre la lista y, para cada dirección, hace la división:

$$
\text{Página} = \frac{\text{Dirección}}{\text{Tamaño de la página}}
$$

y como ultimo paso, se imprime una tabla que relaciona cada dirección con su página y, al final, la cadena de referencias completa.
