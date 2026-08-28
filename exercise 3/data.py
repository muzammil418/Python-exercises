import random

# solution to 0a
customers = []
orders = [
        {"order_id": 5001, "customer_id": 1, "item": "Keyboard", "amount": 49.99},
    ]


def make_customers(n):

    for i in range(n):
        customer = {
            "id": i + 1,
            "name": random.choice(["Alex Turner","Maya Patel","Liam Gallagher","Sophia Chen","Ethan Brooks","Olivia Vance","Lucas Reed","Emma Rodriguez","Benjamin Hayes","Chloe Dubois","Noah Sterling","Ava Tanaka","Jackson Cole",]),
            "city": random.choice(["Tokyo","Paris","Cairo","Sydney","Toronto","Rio de Janeiro","Seoul","London","Buenos Aires","Nairobi",]),
            "signup_year": random.randint(2015, 2025)
        }
        customers.append(customer)



def make_orders(m, num_customers):
    num_order = m - 5

    for i in range(num_order):
        order = {
            "order_id": i + 1,
            "customer_id": customers[random.randint(0, num_customers - 1)]["id"],
            "item": random.choice(["Keyboard", "Mouse", "Monitor", "Laptop", "Cable", "Webcam"]),
            "amount": random.randint(5, 500)
        }
        orders.append(order)


    for i in range(num_order, m):
        order = {
            "order_id": i + 1,
            "customer_id": num_customers + 100 + i,
            "item": random.choice(["Keyboard", "Mouse", "Monitor", "Laptop", "Cable", "Webcam"]),
            "amount": random.randint(5, 500)
            }
        orders.append(order)


make_customers(20)
make_orders(15, 20)

# solution to 0b
customer_ids = [customer["id"] for customer in customers]
orphans_count = [order for order in orders if order["customer_id"] not in customer_ids]

print(len(orphans_count))


# solution to 1a

names = [customer["name"] for customer in customers]

# solution to 1b

latest = max(customers, key=lambda customer: customer["signup_year"])
earliest = min(customers, key=lambda customer: customer["signup_year"])

# solution to 1c

last_five = customers[-5:]

# solution to 1d

laptop_orders = len([order for order in orders if order["item"] == "Laptop"])

# solution to 1e

total_amount = sum([order["amount"] for order in orders])

# solution to 1f

highest_order = max(orders, key=lambda order: order["amount"])

# solution to 1g

cities = set([customer["city"] for customer in customers])

# solution to 1h

customer_7 = next((customer for customer in customers if customer["id"] == 7), None)





