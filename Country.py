# Aaron Kotz, CIS261, Country

def display_menu():
    print("\n--- The Country Program ---")
    print("COMMAND MENU")
    print("list - List all countries")
    print("view - View a country")
    print("add - Add a country")
    print("del - Delete a country")
    print("exit - Exit program\n")

def prepopulate_countries():
    return {"US": "United States", "CA": "Canada", "MX": "Mexico"}

def list_countries(countries):
    print("\nList of countries:")
    for key in countries:
        print(f"{key} - {countries[key]}")
    print()

def view_country(countries):
    list_countries(countries)
    key = input("Enter country code: ").upper()
    if key in countries:
        print(f"\nThe country for code {key} is {countries[key]}\n")
    else:
        print("\nInvalid country code.\n")

def add_country(countries):
    key = input("\nEnter country code: ").upper()
    if key in countries:
        print(f"\n{key} already exists.\n")
    else:
        country_name = input("Enter country name: ")
        countries[key] = country_name
        print(f"\n{country_name} was added.\n")

def delete_country(countries):
    key = input("\nEnter country code to delete: ").upper()
    if key in countries:
        del countries[key]
        print(f"\n{key} was deleted.\n")
    else:
        print("\nInvalid country code.\n")

def main():
    countries = prepopulate_countries()
    display_menu()
    while True:
        command = input("Command: ").lower()
        if command == "list":
            list_countries(countries)
        elif command == "view":
            view_country(countries)
        elif command == "add":
            add_country(countries)
        elif command == "del":
            delete_country(countries)
        elif command == "exit":
            print("\nBye!\n")
            break
        else:
            print("\nNot a valid command. Please try again.\n")

if __name__ == "__main__":
    main()



