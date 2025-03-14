import datetime

# Ask user for name and age
name = input("Cześć, jak masz na imię?")
age = int(input("Ile masz lat? " + name + "!"))
year_today = datetime.datetime.now().year

# Main condition
if 0 <= age <= 99:
    data_actual = str(year_today + (100 - age))
    message = ("Wiesz, że w roku " 
               + data_actual 
               + " będziemy obchodzić Twoje setne " 
               + "(100lat!) urodziny.")
elif age < 0:
    message = "Fajny żart, nie ma takich lat"
elif 100 <= age <= 199:
    message = "Gratulacje, przekroczyłeś pierwszą setkę"
else:
    message = "Kurcza, naprawde jesteś Dunkanem Maklaudem)"

# Extra task
repeat_count = int(input("Ile razy chcesz, żebyśmy Ci pogratulowali? "))

# Multi-line string 

final_output = "\n".join([f"{i+1}. {message}" for i in range(repeat_count)])

# Print on screen
print("\n" + final_output)

# Save to a file
with open("message_output.txt", "w", encoding="utf-8") as file:
    file.write(final_output)

print("\nWiadomość została zapisana w pliku message_output.txt")
