# Programa que deriva la cadena de páginas a partir de una lista de direcciones referenciadas

# Devuelve la lista de página con la siguiente formula: página = dirección // tam_pagina
def cadena_referencias(tam_pagina, direcciones):
    if tam_pagina <= 0:
        raise ValueError("El tamaño de página debe ser positivo.")
    paginas = []
    for d in direcciones:
        if d < 0:
            raise ValueError(f"Dirección inválida: {d}")
        paginas.append(d // tam_pagina)
    return paginas

# Acepta direcciones separadas por comas, espacios o saltos de línea
def leer_direcciones(texto):
    return [int(x) for x in texto.replace(",", " ").split()]


def main():
    # El tamaño de pagina (tam_pagina)
    tam = int(input("Tamaño de página (bytes): "))
    # La dirección
    texto = input("Direcciones referenciadas (separadas por comas o espacios): ")
    direcciones = leer_direcciones(texto)

    cadena = cadena_referencias(tam, direcciones)
    print("\nDirección -> Página")
    for d, p in zip(direcciones, cadena):
        print(f"{d:>8} -> {p}")
    print("\nCadena de referencias:", ", ".join(map(str, cadena)))


if __name__ == "__main__":

    main()