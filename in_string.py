def check_vowels():
    nombre = "Matias"
    nombre = nombre.lower()
    return {v: v in nombre for v in "aeiou"}
check_vowels()