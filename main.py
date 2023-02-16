palabra="ithamar"

# print(palabra[0])
# print(palabra[1])
# print(palabra[2])
# print(palabra[3])
# print(palabra[4])
# print(palabra[5])

indice=0

for letra in palabra:
    print(letra,indice)
    indice=indice + 1 

marcas= ["bmw","honda","nissan"]

for marca in marcas:
  print(marca)

for indice,letra in enumerate(palabra):
    print(indice,letra)