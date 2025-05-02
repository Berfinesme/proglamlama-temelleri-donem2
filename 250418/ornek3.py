saat=int(input("otoparkta kaç saat kaldınız :"))
if saat <1:
    print("1 saate 5 TL")
elif saat >=1 and saat >=5:
    print("4TL")
else:
    print("3TL")