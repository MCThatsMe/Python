def sandwich_items(*ingredients):
    print("Your order contains these items: ")
    for ingredient in ingredients:
        print(f"- {ingredient}",sep='\n')    
    
sandwich_items('ham', 'salami', 'cheese', 'mayo')

print("What do you want on your sandwich?")
print("Enter 'q' when done with your order")

product = []
while True: 
    item = input("Add an item: ")
    if item == 'q':
        break
    else:
        product.append(item)
    

sandwich_items(product)
