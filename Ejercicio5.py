def pluralize(lista_original):
  """
  INPUT
  Esta función recibe una lista de strings
  OUTPUT
  Esta función retorna una lista con los strings sin repetir, y los que haya más de 1 se agrega una s
  """
  if not isinstance(lista_original,list):
    return None, "No se recibió una lista"
  lista_plural = []
  for i in lista_original:
    if not isinstance(i,str):
      return None, "hay elementos en la lista que no son strings"
    if lista_plural.count(i) == 0 and lista_plural.count(i+"s") == 0:
      lista_plural.append(i)
    elif lista_plural.count(i) > 0:
      lista_plural[lista_plural.index(i)] += "s"
  return lista_plural