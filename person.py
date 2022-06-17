def get_formatted_name(first_name, last_name, age = None):
    full_name = f"{first_name} {last_name} age {age}."
    return full_name.title()

while True:
    print('\nPlease tell me your name:')
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    get_age = input("How old are you? ")
    if get_age == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name, get_age)
    print(f"\nHello, {formatted_name}")
