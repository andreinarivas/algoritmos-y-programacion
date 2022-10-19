def is_oblongo(number):
  is_true=True
  for x in range(1, number+1):
    if x*(x+1)==number:
      is_true=True
      break
    else:
      is_true=False
  return is_true

def is_perfect(number):
  is_true=True
  sum=0
  for x in range(1,number):
    if number%x==0:
      sum+=x
  if sum==number:
    is_true=True
  else:
    is_true=False
  return is_true

      

def main():
  estructura_base = {
  'objeto_1': ([126, 306, 832, 264], [679, 592, 280, 562, 25], [6, 918, 984, 251], [490, 13, 822], [454, 495, 633, 357, 186], [949], [926, 940, 215, 725], [21, 18, 467, 660, 370], [915], [132, 437, 467], [], [530, 304, 345, 398, 466], [256, 899], [], [925], [45], [824, 245, 447, 981, 84], [468, 364], [158, 15], [704, 367, 812, 46], [], [], [601, 717, 423, 212]),
  'objeto_2': ([854], [633], [279], [741], [601, 258, 917], [522, 72, 848], [138, 558, 707, 708, 86], [91, 63, 855, 205], [555, 152, 159], [211, 175, 570, 620], [589, 95, 373], [856, 100, 788], [990, 544, 266], [619, 312, 106, 205], [223, 139, 893, 35, 921], [379, 129, 836, 948], [86, 593, 897], [342, 734, 942, 210, 839], [486], [124], [777, 764, 852, 235], [947, 922], [993, 918, 387]),
  'objeto_3': ([426, 804, 806], [978, 963], [986, 156, 53], [755, 238], [106, 803, 5, 747, 317], [126], [964, 832, 132, 904, 599], [], [740, 797, 784], [523, 551], [172], [487, 347], [255, 438, 464, 450], [835], [], [619, 24], [256, 264, 985, 240], [554, 135, 260, 383, 183], [953, 882, 877], [607, 156, 106, 536], [677, 516], [701], [128]),
  'objeto_4': ([348, 768], [721, 832, 637, 477], [29], [973, 407], [107, 447], [], [970], [994, 534], [], [482, 399, 389, 788], [], [], [956, 87], [480], [86, 937], [], [143, 868, 596], [639, 434, 150, 462, 651], [908, 551, 195, 454], [83, 245, 901], [538, 525, 83], [53], [786]),
  'objeto_5': ([462, 255, 625, 146, 456], [688, 440, 89, 5], [812], [713, 426, 492], [952, 284, 489], [119], [], [506, 920], [], [719, 546, 218], [201], [977, 271, 31, 733, 216], [121, 660, 22, 24, 431], [993, 199], [484, 978], [], [234, 141], [], [58, 300, 280, 147], [], [888, 231, 322], [631, 137, 531, 991, 857], []),
  'objeto_6': ([681, 916, 184, 730, 940], [603, 663, 334, 865, 937], [786, 365, 791, 472], [328], [], [433, 518, 342, 555], [966], [392, 599, 689, 113], [593, 503, 395, 431, 697], [983, 981], [821, 629, 692, 564], [], [], [835, 922, 496, 983], [475], [539, 531, 500], [688, 648], [411], [400, 110], [392], [], [511], [419, 936]),
  'objeto_7': ([457, 405, 775, 235], [803], [121, 572, 641, 7, 273], [589, 756, 163], [218, 718, 711], [], [84, 111, 983], [751, 881], [387], [215, 179, 256], [159, 207], [863], [186, 126], [976, 876, 667, 158], [913, 329, 503], [], [564, 999, 696, 885, 263], [836, 636, 960], [429, 789, 445], [], [808, 657, 590, 15, 230], [492, 101, 641, 157], [509, 115])
  }
  num_of_numbers=0
  for object, tuple in estructura_base.items():
    oblongos=[]
    perfectos=[]
    for list in tuple:
      num_of_numbers+=len(list)
      for number in list:
        oblongo=is_oblongo(number)
        perfecto=is_perfect(number)
        if oblongo:
          oblongos.append(number)
        if perfecto:
          perfectos.append(number)
    print('\n')
    print('Oblongos in {}: {}'.format(object, len(oblongos)))
    print('Perfectos in {}: {}'.format(object, len(perfectos)))
  print(num_of_numbers/7)


 


main()