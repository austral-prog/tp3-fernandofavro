def check_vowels():
    nombre = input("Ingrese un nombre: ")
    nombre = nombre.lower()  # pasar todo a minúscula

    for vocal in "aeiou":
        print(f"Contiene {vocal}: {vocal in nombre}")
check_vowels()