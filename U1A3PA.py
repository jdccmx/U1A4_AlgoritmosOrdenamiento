import timeit
import random
import statistics

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = random.choice(lista)  # pivote aleatorio
    
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    
    return quicksort(menores) + iguales + quicksort(mayores)

def generar_lista_aleatoria(tamano):
    return [random.randint(0, 10000) for _ in range(tamano)]

def generar_lista_invertida(tamano):
    return list(range(tamano, 0, -1))

def medir_tiempo(funcion, lista, repeticiones=5):
    tiempos = []
    
    for _ in range(repeticiones):
        copia = lista.copy()
        
        tiempo = timeit.timeit(
            lambda: funcion(copia),
            number=1
        )
        
        tiempos.append(tiempo)
    
    promedio = statistics.mean(tiempos)
    desviacion = statistics.stdev(tiempos)
    
    return promedio, desviacion

tamanos = [100, 1000, 5000, 10000]

print("RESULTADOS DE RENDIMIENTO\n")

for tam in tamanos:
    
    print(f"\nTamaño: {tam}")
    
    # Escenario 1: lista aleatoria
    lista = generar_lista_aleatoria(tam)
    
    prom_burbuja, des_burbuja = medir_tiempo(bubble_sort, lista)
    prom_quick, des_quick = medir_tiempo(quicksort, lista)
    
    print("Lista aleatoria:")
    print(f"Bubble Sort → Promedio: {prom_burbuja:.6f} s | Desv: {des_burbuja:.6f}")
    print(f"Quicksort   → Promedio: {prom_quick:.6f} s | Desv: {des_quick:.6f}")
    
    
    # Escenario 2: lista invertida
    lista = generar_lista_invertida(tam)
    
    prom_burbuja, des_burbuja = medir_tiempo(bubble_sort, lista)
    prom_quick, des_quick = medir_tiempo(quicksort, lista)
    
    print("Lista invertida:")
    print(f"Bubble Sort → Promedio: {prom_burbuja:.6f} s | Desv: {des_burbuja:.6f}")
    print(f"Quicksort   → Promedio: {prom_quick:.6f} s | Desv: {des_quick:.6f}")
