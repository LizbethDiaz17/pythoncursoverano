descuento:float = 0
name: str = input("ingresa tu nombre:")
precioDeManzanas: int= int(input("ingresa el precio de las manzanas :"))
cantidadDeManzanas :int= int(input("cuantas manzanas vendieron:"))

if name =="liz" or cantidadDeManzanas == 18 :
    descuento = (precioDeManzanas * cantidadDeManzanas) * .2
    
elif cantidadDeManzanas > 10 :
    descuento = (precioDeManzanas * cantidadDeManzanas) * .1



if descuento ==0 :
    print("el descuento fue de : {descuento}") 
    

print("total a pagar : " + str(precioDeManzanas * cantidadDeManzanas))








