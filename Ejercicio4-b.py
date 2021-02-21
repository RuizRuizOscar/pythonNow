#Ejercicio 4-b
def formatNumber2(number,char):
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
  number_as_str = str(number)
  length = len(number_as_str)
  if length <= 3:
    return number_as_str
  loops = length // 3
  if length % 3 == 0:
    loops -= 1
  result_string = number_as_str[:length%3]
  i=0
  while loops>0:
    result_string += char + number_as_str[i*3+(length%3):i*3+(length%3)+3]
    loops -= 1
    i += 1
  return result_string