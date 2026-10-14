### Step 1: Creating a menu using a dictionary:-----

```

menu = {    'tea': 10,    'pizza': 100,    'burger': 120,    'pop corn': 75,    'chicken roll': 100,    'chicken puff': 50}

```

Here, we create a Python dictionary named `menu`.

A dictionary stores data as key-value pairs.

- Key: The name of the food item.
- Value: The price of that food item.

For example:

```

'tea': 10'pizza': 100'burger': 120

```

This means tea costs ₹10, pizza costs ₹100, and a burger costs ₹120.

You can access a food item's price using its key:

```

print(menu\\\['tea'])

```

Output:

```

10

```

Concept used: Dictionary (`dict`).

### Step 2: Displaying the welcome message:-----

```

print('Welcome to our Modern Cafe')

```

The `print()` function displays text on the screen.

Output:

```

Welcome to our Modern Cafe

```

### Step 3: Displaying the menu:-----

```

print('tea: 10\\\\npizza: 100\\\\nburger: 120\\\\npop corn: 75\\\\nchicken roll: 100\\\\nchicken puff: 50')

```

This line displays all food items and their prices.

The special character `\\\\n` means new line. It moves the following text to the next line.

For example:

```

print('tea: 10\\\\npizza: 100')

```

Output:

```

tea: 10

pizza: 100

```

### Step 4: Initializing the total bill:-----

```

order\\\_total = 0

```

Here, we create a variable named `order\\\_total` and assign it the value `0`.

It stores the total price of all the food items ordered by the customer.

For example, if the customer orders tea for ₹10 and pizza for ₹100:

- Initial total = ₹0
- After tea = ₹10
- After pizza = ₹110

We start with zero because no items have been ordered yet.

### Step 5: Using the `while True` loop:-----

```

while True:

```

A `while` loop repeatedly executes a block of code while its condition is true.

Here, `True` is always true, so the loop continues indefinitely until we explicitly stop it using `break`.

Why do we use this loop?

Because a customer may order multiple items, such as tea, pizza, and a burger, before finishing the order.

The loop allows the customer to enter one item at a time.

### Step 6: Taking input from the customer:-----

```

order\\\_item = input('Enter your item: ').lower()

```

This line contains three important concepts.

- `input()` — accepts text entered by the customer.
- `order\\\_item` — stores the entered food name.
- `.lower()` — converts the entered text into lowercase letters.

For example:

```

order\\\_item = input('Enter your item: ').lower()

```

If the customer enters:

```

PIZZA

```

Python stores:

```

order\\\_item = 'pizza'

```

This helps the program accept different letter cases, such as `PIZZA`, `Pizza`, or `pizza`.

Note: `.lower()` does not remove extra spaces. An entry like `" pizza "` will not match the dictionary key without additional whitespace handling.

### Step 7: Checking whether the item exists:-----

```

if order\\\_item in menu:

```

This is an `if` conditional statement.

The expression:

```

order\\\_item in menu

```

checks whether the entered item exists among the dictionary's keys.

For example:

```

order\\\_item = 'pizza'

```

The condition is `True` because `pizza` is a key in `menu`.

But if:

```

order\\\_item = 'sandwich'

```

The condition is `False` because `sandwich` is not in the menu.

Python then chooses which block to execute.

### Step 8: Adding the item's price:-----

```

order\\\_total += menu\\\[order\\\_item]

```

This is one of the most important lines in the program.

It retrieves the item's price from the dictionary and adds it to the current total.

The shorthand operator `+=` means add the right-hand value to the existing variable.

It is equivalent to:

```

order\\\_total = order\\\_total + menu\\\[order\\\_item]

```

For example, if the customer orders pizza:

```

order\\\_total = 0order\\\_total += menu\\\['pizza']

```

Since `menu\\\['pizza']` equals `100`, the calculation is:

```

order\\\_total = 0 + 100

order\\\_total = 100

```

If the customer then orders tea:

```

order\\\_total = 100 + 10

order\\\_total = 110

```

The total keeps increasing with each valid item.

### Step 9: Displaying a success message:-----

```

print(f'{order\\\_item} added to your order.')

```

This uses an f-string, which allows variables to be inserted into a string using curly braces `{}`.

If `order\\\_item` is `pizza`, the output is:

```

pizza added to your order.

```

Another example:

```

name = 'tea'print(f'{name} added to your order.')

```

Output:

```

tea added to your order.

```

### Step 10: Handling an invalid item with `else`:-----

```

else:    print('You entered a wrong item.')

```

The `else` block runs when the `if` condition is false.

For example, if the customer enters `sandwich`, the program displays:

```

You entered a wrong item.

```

The program does not add anything to `order\\\_total` for an invalid item.

Important: The program still asks whether the customer wants another item, even after an invalid entry.

### Step 11: Asking whether the customer wants more items:-----

```

order = input('Do you want anything else? (yes/no): ').lower()

```

This line asks the customer whether they want to continue ordering.

The answer is stored in the variable `order`.

For example:

```

Do you want anything else? (yes/no): yes

```

The `.lower()` method converts `YES` or `Yes` into `yes`.

### Step 12: Stopping the loop using `break`:-----

```

if order != 'yes':    break

```

The operator `!=` means not equal to.

This condition checks whether the customer's response is anything other than `yes`.

- If the customer enters `yes`, the condition is false, so the loop repeats.
- If the customer enters `no`, the condition is true, so `break` terminates the loop.

For example:

```

order = 'no'if order != 'yes':    break

```

The loop stops.

Strictly speaking, any response other than `yes`, including an unexpected answer like `maybe`, will stop the loop.

### Step 13: Displaying the final bill:-----

```

print(f'Your order value is: Rs. {order\\\_total}')

```

This statement executes after the loop finishes.

It displays the total cost of all valid items ordered by the customer.

For example:

```

Your order value is: Rs. 210

```

##  Complete program flow:---------

1\. Start the program

Create the menu and set total to ₹0

2\. Enter a food item

Convert the input to lowercase

3\. Is the item in the menu?

Yes

Add its price to the total

No

Display an error message

4\. Want another item?

Yes → repeat the loop · No → stop

5\. Print the final bill

### Example execution with output

Suppose a customer orders pizza, tea, and a burger.

PYTHON CONSOLE

Welcome to our Modern Cafe tea: 10 pizza: 100 burger: 120 pop corn: 75 chicken roll: 100 chicken puff: 50  Enter your item: pizza pizza added to your order. Do you want anything else? (yes/no): yes  Enter your item: tea tea added to your order. Do you want anything else? (yes/no): yes  Enter your item: burger burger added to your order. Do you want anything else? (yes/no): no  Your order value is: Rs. 230

Bill calculation

Pizza

₹100

Tea

₹10

Burger

₹120

Total

## ₹230

## 5. Python concepts used in this project

| Concept               | Code example                 | Purpose                          |
| --------------------- | ---------------------------- | -------------------------------- |
| Dictionary            | `menu = {...}`               | Stores food names and prices     |
| `print()`             | `print('Welcome')`           | Displays output                  |
| `input()`             | `input('Enter your item: ')` | Accepts user input               |
| Variable              | `order\\\_total = 0`            | Stores the bill amount           |
| String method         | `.lower()`                   | Converts text to lowercase       |
| `while` loop          | `while True:`                | Repeats ordering                 |
| `if` statement        | `if order\\\_item in menu:`     | Checks whether an item exists    |
| `else` statement      | `else:`                      | Handles invalid items            |
| Membership operator   | `in`                         | Checks whether a key exists      |
| Comparison operator   | `!=`                         | Checks whether two values differ |
| Arithmetic assignment | `+=`                         | Adds a price to the total        |
| `break`               | `break`                      | Exits the loop                   |
| f-string              | `f'{order\\\_total}'`           | Inserts values into text         |

## 6. Important interview questions and answers

Q1. Why do we use a dictionary in this program?

A: To store each food item's name and its corresponding price as key-value pairs.

Q2. Why do we use `while True`?

A: To allow customers to order multiple items until they decide to stop.

Q3. What is the purpose of `.lower()`?

A: It converts the input into lowercase so that entries like `PIZZA` and `Pizza` match the key `pizza`.

Q4. What is the difference between `+=` and `=`?

A: `=` assigns a value, while `+=` adds a value to the variable's existing value.

Q5. What is the purpose of `break`?

A: It immediately terminates the current loop.

Q6. What happens if the customer enters an invalid food item?

A: The program displays an error message and does not add a price to the bill.

Q7. Why is `order\\\_total` initialized to zero?

A: Because the initial bill is zero before the customer orders anything.

## 7. Small improvement to your code

You can improve input handling by using `.strip().lower()`. This removes unwanted spaces before converting the input to lowercase.

Replace:

```

order\\\_item = input('Enter your item: ').lower()

```

with:

```

order\\\_item = input('Enter your item: ').strip().lower()

```

Now, if a customer enters `"  Pizza  "`, Python converts it into `"pizza"` and accepts the order.

You can also improve the program by validating the customer's yes/no response, displaying itemized bills, and adding quantities.

Summary: Your program uses dictionaries, loops, conditional statements, user input, and arithmetic operators to create a simple cafe billing system. It is a good beginner-level Python project and a useful starting point for building a more advanced billing application.
