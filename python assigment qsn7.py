'''7.	Given list of items purchased in a file display the following: No of items purchased, No of free items, Amount to pay, Discount given, Final amount paid
Concepts: files, dictonary

Sample output for purchase-1.txt file:
No of items purchased: 5 
No of free items: 2
Amount to pay: 485
Discount given: 80
Final amount paid: 405

(Test your program on below given purchase-1.txt and purchase-2.txt)'''

# Program to read items purchased from file and calculate billing details

with open("items.txt", "w") as f:
    print("Enter item name and price (example: soap,40)")
    print("Type 'stop' to finish\n")

    while True:
        line = input("Enter item & price: ")
        if line.lower() == "stop":
            break
        f.write(line + "\n")


filename = "items.txt"

items = {}  

with open(filename, "r") as file:
    for line in file:
        data = line.strip().split(",")
        item_name = data[0].strip()
        price = int(data[1].strip())
        items[item_name] = price

num_items = len(items)
free_items = sum(1 for price in items.values() if price == 0)
amount_to_pay = sum(price for price in items.values() if price != 0)


if amount_to_pay > 500:
    discount = amount_to_pay * 0.10
else:
    discount = int(input("discount: "))

final_amount = amount_to_pay - discount

print(" Purchase Summary ")
print("Number of items purchased :", num_items)
print("Number of free items      :", free_items)
print("Amount before discount     : ₹", amount_to_pay)
print("Discount given             : ₹", discount)
print("Final amount to be paid    : ₹", final_amount)

