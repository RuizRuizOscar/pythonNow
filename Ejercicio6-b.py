def makeBox2(number):
  """
  INPUT
  Esta función recibe un número entero positivo mayor a 1
  OUTPUT
  Si recibe algo distinto a un número entero positivo mayor a 1, retorna None
  Si recibe un "valor"=número entero positivo mayor a 1, imprime una caja con base y lado de longitud "valor"
  """
  if not isinstance(number,int):
    return None
  if number < 1:
    return None
  box_list = []
  if number == 1:
    box_list.append("#")
  else:
    base = "#"*number
    box_list.append(base)
    lado = "#" + " "*(number-2) + "#"
    i=0
    while i < number-2:
      box_list.append(lado)
      i += 1
    box_list.append(base)
  for i in box_list:
    print(i)