def check_vowels():
    nombre = input("Ingrese un nombre: ")
    nombre = nombre.lower()
    for vocal in "aeiou":
        print(f"Contiene {vocal}: {vocal in nombre}")