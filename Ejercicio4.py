#Ejercicio 4
def format_number(number,char):
  """
  INPUT
  Esta función recibe un número entero positivo y un caracter en formato string (""). 
  OUTPUT
  Esta función Retorna el número recibido formateado como un string, con el caracter (2o argumento) delimitador cada 3 caracteres para que el número se lea más fácilmente
  """
  if not isinstance(number,int):
    return None
  if not isinstance(char,str):
    return None
  result_string = ""
  length = len(str(number))
  i=0
  if length<=3:
    return str(number)
  result_string = str(number)[i-3:]
  loops = length // 3
  while loops > 1:
    loops -= 1
    i -= 3
    result_string = str(number)[i-3:i] + char + result_string
  i -= 3
  if length%3 > 0:
    result_string = str(number)[i-(length%3):i] + char + result_string
  return result_string