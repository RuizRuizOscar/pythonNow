#Ejercicio 2
def multiplesList3(number,multiples):
  """
  INPUT
  Esta función recibe dos argumentos enteros positivos. El primer número será el múltiplo y el segundo es el número de múltiplos que calculará. 
  OUTPUT
  Regresa una lista con los múltiplos del primer argumento porporcionado.
  """
  if not(isinstance(number,int) and isinstance(multiples,int)):
    return None
  if number<0 or multiples <0:
    return None
  return [i for i in range(number,number*multiples+1,number) ] 