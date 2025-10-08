erdemjegy = int(input("(1-5): "))
# 8

if erdemjegy == 1:
    print("elegtelen")
elif erdemjegy == 2:
    print("elegseges")
elif erdemjegy == 3:
    print("kozepes")
elif erdemjegy == 4:
    print("jo")
elif erdemjegy == 5:
    print("jeles")

# 9

fok = float(input("mennyi a viz foka °C-ban: "))
if fok <= 0:
    print("szilárd")
elif fok < 100:
    print("folyékony")
else:
    print("gáz")

# 10

a = float(input("3"))
b = float(input("4"))
c = float(input("5"))

if a + b > c and a + c > b and b + c > a 
    print("szerkesztheto haromszog.")
else:
    print("nem szerkesztheto haromszog.")

# 11


fahrenheit = float(input("a homerseklet fahrenheitben:"))
celsius = (fahrenheit - 32) * 5/9
print("celsiusban: 100,0", celsius)

# 12

celsius = float(input("a homerseklet celsiusban:"))
fahrenheit = celsius * 9/5 + 32
print("Fahrenheitben:212,0", fahrenheit)

# 13

masodperc = int(input("ido masodpercben: "))

ora = masodperc // 3600
perc = (masodperc % 3600) // 60
masodperc = masodperc % 60

print(ora, "óra", perc, "perc", mp, "másodperc")