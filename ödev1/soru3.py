def TemizVeri():
   
    ilk_string ="Ah5me4t"
    ikinci_string ="M9eHm4eT"
    ucuncu_string ="Ha3K5a1n"
    Birlesmis_deger = ""

    ilk_rakamsiz = ""
    ikinci_rakamsiz = ""
    ucuncu_rakamsiz = ""

    for harf in ilk_string:
        if harf.isalpha():
            ilk_rakamsiz += harf
        else:
            pass
            
    
    for harf in ikinci_string:
        if harf.isalpha():
            ikinci_rakamsiz += harf
        else:
            pass

    for harf in ucuncu_string:
        if harf.isalpha():
            ucuncu_rakamsiz += harf
        else:
            pass

    ilk_rakamsiz = ilk_rakamsiz.lower()
    ilk_rakamsiz = ilk_rakamsiz.capitalize()
    
    ikinci_rakamsiz = ikinci_rakamsiz.lower()
    ikinci_rakamsiz = ikinci_rakamsiz.capitalize()

    ucuncu_rakamsiz = ucuncu_rakamsiz.lower()
    ucuncu_rakamsiz = ucuncu_rakamsiz.capitalize()

    Birlesmis_deger = ilk_rakamsiz+ "-" + ikinci_rakamsiz + "-" + ucuncu_rakamsiz
    
    return Birlesmis_deger


print(TemizVeri())