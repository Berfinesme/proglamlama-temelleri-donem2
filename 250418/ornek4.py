kenar1=int(input("birinci kenar uzunlugu="))
kenar2=int(input("ikinci kenar uzunlugu="))
kenar3=int(input("üçüncü kenar uzunlugu="))
if kenar1 == kenar2 and kenar1 == kenar3:
    print("eşkenar")
elif kenar1 != kenar2 and kenar1 != kenar3 and kenar2 != kenar3:
    print("çeşitkenar")
else:
    print("ikizkenar")