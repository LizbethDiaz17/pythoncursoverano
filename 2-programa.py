precioDeManzanas: int= int(input("ingresa el precio de las manzanas"))
cantidadDeManzanas :int= int(input("cuantas manzanas vendieron"))


print("vas a imprimir")

#soy un comentario


#concatenacion

print("las manzanas estan en :" + str(precioDeManzanas))
print("las manzanas estan en : " , precioDeManzanas)
print(f"las manzanas estan en : {precioDeManzanas}")

print("y fueron : " + str(cantidadDeManzanas))
print("total a pagar : " + str(precioDeManzanas * cantidadDeManzanas))