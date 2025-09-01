def check_vowels(nombre):
    nombre = nombre.lower()
    return {v: v in nombre for v in "aeiou"}