#Podstawa: 10 x masa ciała + 6.25 x wzrost w cm – 5 x wiek + S
#współczynnik S: dla kobiet = -161, dla mężczyzn= +5
#Podstawę, czyli liczbę kalorii zużywaną na same procesy życiowe należy pomnożyć przez rodzaj aktywności fizycznej:
#Praca siedząca, brak dodatkowej aktywności fizycznej	1,2
#Praca niefizyczna, mało aktywny tryb życia	1,4
#Lekka praca fizyczna,  regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu	1,6
#Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu	1,8
#Praca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu	2,0
print("Podaj masę ciała w kg")
masa=(input())
print("Podaj wzrost w cm")
wzrost=(input())
print("ile masz lat?")
wiek=(input())
print("jakiej jesteś płci? m/k")
plec= str(input())
if plec == "m":
    y=5
else:
    y=-161
print("Jaki prowadzisz tryb życia\n1.Praca siedząca, brak dodatkowej aktywności fizycznej\n2.Praca niefizyczna, mało aktywny tryb życia\n3.Lekka praca fizyczna, regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu\n4.Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu	\n5.Praca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu	")
tryb=int(input())
if tryb == 1:
        z=1.2
elif tryb == 2:
        z=1.4
elif tryb == 3:
        z=1.6
elif tryb == 4:
        z=1.8
elif tryb == 5:
        z=2
x=(10*float(masa))+(6.25*float(wzrost))-(5*int(wiek))+int(y)
B=x*z
print('Twoje zapotrzbowanie kaloryczne to:',B , "kcal")
input("prompt: ")
#działa zajebiście :D
