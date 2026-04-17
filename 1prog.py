#Написано потом і кров'ю Владиславом Дурицьким
#на старому редмі 7а, в термуксі
#у вімі
#0% чатджпт і подібних
#покладаючи великі надії

def askintheloop():
    while True:
        try:
            a = float(input(txt))
        except ValueError:
            print("Ви ввели неправильне значення!")
            continue
        else:
            if a <= 0:
                print("Значення від'ємне! або 0")
                continue
            else:
                return a
#задаємо змінні
vartza1g = 250 
vaganam2 = 15
txt = "Введіть діаметр у м: "

#питаємо діаметр
d = askintheloop()
#і вираховуємо відповіді
s = 3.14*d**2/4
masa = s*vaganam2
vart = masa*vartza1g

#виводимо відповіді
print("Потрібно", round(masa, 2), "г")
print("Вартість насіння", round(vart, 2), "грн")
