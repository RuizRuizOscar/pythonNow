#Ejercicio 2
def multiples_list(number,multiples):
  """
  INPUT
  Esta función recibe dos argumentos enteros positivos. El primer número será el múltiplo y el segundo es el número de múltiplos que calculará. 
  OUTPUT
  Regresa una lista con los múltiplos del primer argumento porporcionado.
  """
  if type(number) != int or type(multiples) != int:
    return None
  if number<0 or multiples <0:
    return None
  list_of_multiples = []
  counter = 1 
  while counter <= multiples:
    list_of_multiples.append(number*counter)
    counter += 1
  return list_of_multiples