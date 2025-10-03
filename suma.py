print("--- Calculadora de Promedio ---")

# 1. Asignación de las 10 notas a variables
nota1 = 8.0
nota2 = 6.0
nota3 = 9.5
nota4 = 7.0
nota5 = 5.5
nota6 = 10.0
nota7 = 8.5
nota8 = 6.5
nota9 = 7.5
nota10 = 9.0

# 2. Calcular la SUMA de todas las notas
# math.fsum suma con alta precisión y acepta un 'iterable' de valores.
# Aquí creamos un 'iterable' temporal usando paréntesis (una tupla) con todas las notas.
suma_total = ((nota1+ nota2+ nota3+ nota4+ nota5+ nota6+ nota7+ nota8+ nota9+ nota10))

# 3. Determinar la cantidad de notas
cantidad_notas = 10 # Se mantiene fija

# 4. Calcular el PROMEDIO
promedio = suma_total / cantidad_notas

# 5. Mostrar el resultado
print("\n--- Detalle y Resultado ---")
print(f"La Suma Total de las 10 notas es (usando fsum): {suma_total:.2f}")
print(f"El **Promedio** general es: **{promedio:.2f}**")
print("---------------------------")