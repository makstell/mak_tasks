import datetime

name = input("Cześć, jak masz na imię?")
age = int(input("Ile masz lat? " + name + "!"))
year_today = datetime.datetime.now().year

if 0 <= age <= 99:
    data_actual = str(year_today + (100 - age))
    print("Wiesz, że w roku "
          + data_actual
          + " będziemy obchodzić Twoje setne "
          + "(100lat!) urodziny.")
elif age < 0:
    print("Fajny żart, nie ma takich lat")
elif 100 <= age <= 199:
    print("Gratulacje, przekroczyłeś pierwszą setkę")
else:
    print("Kurcza, naprawde jesteś Dunkanem Maklaudem)")
