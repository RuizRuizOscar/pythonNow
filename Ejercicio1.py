#Ejercicio1
def largo_numero(number):
  """
  Este método recibe un número entero positivo y regresa None si ocurre un error o si se recibe correctamente regresa una variable con el número 
  """
  if number < 0 :
    print("El número es menor a 0")
    return None
  if type(number) != int:
    print("No se recibió un entero")
    return None
  count = 0
  for i in str(number):
    count += 1
  return count