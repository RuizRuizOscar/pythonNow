def factorial(number):
  """
  Esta función regresa el factorial de un número. Debe ser entero y positivo
  """
  if not isinstance(number,int):
    return None
  if number>1:
    return number * factorial(number-1)
  else:
    return 1
  