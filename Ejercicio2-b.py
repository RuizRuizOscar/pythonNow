#Ejercicio 2
def multiplesList2(number,multiples):
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
  print( [i*number for i in range(1,multiples+1) ] )



  # list_of_multiples = []
  # counter = 1 
  # while counter <= multiples:
  #   list_of_multiples.append(number*counter)
  #   counter += 1
  # return list_of_multiples