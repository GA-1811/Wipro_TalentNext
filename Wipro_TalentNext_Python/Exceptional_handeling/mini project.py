# You have saved the items and their price details in a text file, which you purchased yesterday from a nearby 
# supermarket. You need to know:

# How many items did you purchase?
# How many items are free?
# What is the total amount you had to pay?
# What is the discount amount?
# What is the final ammount did you pay after the discount?

def analyze_purchase(file_name):
    try:
        with open(file_name, "r") as file:
            total_items = 0
            free_items = 0
            total_cost = 0.0
            discount = 0.0

            for line in file:
                parts = line.strip().split()
                if len(parts) != 2:
                    continue 

                item, price = parts[0], float(parts[1])
                total_items += 1

                if price == 0:
                    free_items += 1
                    discount += 0
                else:
                    total_cost += price

            final_amount = total_cost

            print(f"No of items purchased: {total_items}")
            print(f"No of free items: {free_items}")
            print(f"Amount to pay: {total_cost:.2f}")
            print(f"Discount given: {discount:.2f}")
            print(f"Final amount paid: {final_amount:.2f}")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("Unexpected error:", e)

filename = input("Enter the purchase file name: ")
analyze_purchase(filename)

