#Ejercicio1
def largo_numero(number):
  """
  Este método recibe un número entero positivo y regresa None si ocurre un error o si se recibe correctamente regresa una variable con el número 
  """
  if type(number) != int:
    return None
  if number < 0:
    return None
  count = 0
  for i in str(number):
    count += 1
  return count