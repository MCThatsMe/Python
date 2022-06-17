response = {}
polling_active = True

while polling_active:

    name = input("What is your name? ")
    print(f"\nHello, {name.title()}.")
    vacSpot = input("\nWhere would you like to go for vacation? ")

    response[name] = vacSpot

    repeat = input("\nIs there anyone else to add? (yes/no)")
    if repeat == "no":
        polling_active = False

print("\n-------Results!--------")
for name, vacSpot in response.items():
    print(f"{name.title()} would like to visit {vacSpot} some day.")