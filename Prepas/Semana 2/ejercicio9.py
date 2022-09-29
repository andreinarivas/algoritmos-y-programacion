codigos_postales = "...._ __... ..... ..___*.____ ___.. ___.. _____*_.... ..___ ...__ _....*..... __... .____ .____*___.. ...._ ____. ____.*"
counter=0
number= ""
for x in range(0, len(codigos_postales),6):
        if codigos_postales[x]==".":
            count=str(codigos_postales[x:x+5].count('.'))
            number+=count
        if codigos_postales[x]=="_":
            count=str(codigos_postales[x:x+5].count('_'))
            if count=="1":
                number+="6"
            elif count=="2":
                number+="7"
            elif count=="3":
                number+="8"
            elif count=="4":
                number+="9"
            else:
                number+="0"
for x in range(0,len(number),4):
    print("*" + number[x:x+4])
