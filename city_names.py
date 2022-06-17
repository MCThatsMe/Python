from typing import final


def city_country(city, country):
    full_city_country = f"{city}, {country}"
    return full_city_country.title()
    
while True:
    print("\nHello. Please tell me if you want to go to 'Columbia', 'Puerto Rico', 'Mexico', or 'Cuba'")
    print("Enter 'q' to quit'")
    get_country = input("\nEnter the country: ")
    get_country.lower()
    

    if get_country == 'q':
        break

    elif get_country == 'columbia':
        city = "bogota"
        final_value = city_country(city = city, country = get_country)
        print(f"\nCool! The capitol of {get_country.title} is {city.title}. ")
        print(f"\nWhy don't you travel to {final_value.title()} sometime?")
    elif get_country == 'puerto rico':
        city = "san jose"
        final_value = city_country(city = city, country = get_country)
        print(f"\nCool! The capitol of {get_country.title} is {city.title}. ")
        print(f"\nWhy don't you travel to {final_value.title()} sometime?")
    elif get_country == 'mexico':
        city = "Mexico DF"
        final_value = city_country(city, get_country)
        print(f"\nCool! The capitol of {get_country.title} is {city.title}. ")
        print(f"\nWhy don't you travel to {final_value.title()} sometime?")
    elif get_country == 'Cuba':
        city = "havana"
        final_value = city_country(city, get_country)
        print(f"\nCool! The capitol of {get_country.title} is {city.title}. ")
        print(f"\nWhy don't you travel to {final_value.title()} sometime?")
    