
menu = {
    'tea': 10,
    'pizza': 100,
    'burger': 120,
    'pop corn': 75,
    'chicken roll': 100,
    'chicken puff': 50
}

print('Welcome to our Modern Cafe')
print('tea: 10\npizza: 100\nburger: 120\npop corn: 75\nchicken roll: 100\nchicken puff: 50')

order_total = 0

while True:
    order_item = input('Enter your item: ').lower()

    if order_item in menu:
        order_total += menu[order_item]
        print(f'{order_item} added to your order.')
    else:
        print('You entered a wrong item.')

    order = input('Do you want anything else? (yes/no): ').lower()

    if order != 'yes':
        break

print(f'Your order value is: Rs. {order_total}')
