products = {'chips': {'price': 0.50, 'inventory': 10},
            'candy': {'price': 0.75, 'inventory': 5},
            'soda': {'price': 1.00, 'inventory': 7}}

coins = {'nickel': 0.05, 'dime': 0.10, 'quarter': 0.25}

total = 0
sales_log = {}

def display_products():
    print('Product options:')
    for product in products:
        print(product.capitalize(), f'- ${products[product]["price"]:.2f} ({products[product]["inventory"]} left)')

def vend():
    display_products()
    selection = input('Select a product: ').lower()
    if selection not in products:
        print('Invalid selection')
        return
    if products[selection]['inventory'] == 0:
        print('Out of stock')
        return
    print(f'The price of {selection} is ${products[selection]["price"]:.2f}')
    print('Insert coins:')
    for coin in coins:
        print(coin.capitalize(), f'- ${coins[coin]:.2f}')
    amount = 0
    while amount < products[selection]['price']:
        coin = input('Insert a coin: ').lower()
        if coin not in coins:
            print('Invalid coin')
            continue
        amount += coins[coin]
    change = amount - products[selection]['price']
    global total
    total += products[selection]['price']
    if selection in sales_log:
        sales_log[selection] += 1
    else:
        sales_log[selection] = 1
    products[selection]['inventory'] -= 1
    print(f'Dispensing {selection}...')
    if change > 0:
        print(f'Dispensing ${change:.2f} in change')
    print(f'Total amount collected: ${total:.2f}')
    print('Sales log:')
    for product in sales_log:
        print(product.capitalize(), f'- {sales_log[product]} sold')

def refill():
    display_products()
    selection = input('Select a product to refill: ').lower()
    if selection not in products:
        print('Invalid selection')
        return
    count = input(f'Enter the number of {selection}s to refill: ')
    if not count.isdigit():
        print('Invalid count')
        return
    count = int(count)
    products[selection]['inventory'] += count
    print(f'{count} {selection}s added to inventory')
    print(f'The new inventory level of {selection} is {products[selection]["inventory"]}')

def display_total():
    print(f'Total amount collected: ${total:.2f}')

while True:
    print('Menu options:')
    print('1. Vend a product')
    print('2. Refill a product')
    print('3. Display total amount collected')
    print('4. Exit')
    option = input('Select an option: ')
    if option == '1':
        vend()
    elif option == '2':
        refill()
    elif option == '3':
        display_total()
    elif option == '4':
        break
    else:
        print('Invalid option')
