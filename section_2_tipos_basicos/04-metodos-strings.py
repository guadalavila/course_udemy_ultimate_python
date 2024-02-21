

nombre = "María"
animal = "   perroS y gatoS  "
print("MAYUS: "+animal.upper())
print("minus: "+animal.lower())
print("capitalize: "+animal.capitalize())
print("title: "+animal.title())
print("strip: remueve espacios en blanco: "+animal.strip())
print("strip and capitalize: "+animal.strip().capitalize())
print("strip: remueve espacios en blanco derecha: "+animal.rstrip())
print("strip: remueve espacios en blanco izquierda: "+animal.lstrip())
print("find: busca y devuelve indice: ")
print(animal.find("rr"))
print(animal.find("CH"))
print(animal.replace("rr", "RRRRRRRRR"))
print("er" in animal)
print("hola" in animal)
print("juan" not in nombre)
