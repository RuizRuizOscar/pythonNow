def make_box(number):
  if not isinstance(number,int):
    return None
  if number < 1:
    return None
  box_list = []
  if number == 1:
    box_list.append("#")
  else:
    base, lado = "", ""
    base = base.zfill(number).replace("0", "#")
    box_list.append(base)
    lado = "#" + lado.zfill(number-2).replace("0", " ") + "#"
    i=0
    while i < number-2:
      box_list.append(lado)
      i += 1
    box_list.append(base)
  for i in box_list:
    print(i)