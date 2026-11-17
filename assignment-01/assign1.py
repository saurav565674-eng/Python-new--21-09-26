
orders = [
    {
        'id': 101,
        'customer': 'Asha',
        'status': 'DELIVERED',
        'items': [('keyboard', 2, 1499.0), ('mouse', 1, 599.0)]
    },
    {
        'id': 102,
        'customer': 'Ravi',
        'status': 'CANCELLED',
        'items': [('monitor', 1, 10999.0)]
    },
    {
        'id': 103,
        'customer': 'Asha',
        'status': 'DELIVERED',
        'items': [('cable', 5, 199.0)]
    },
    {
        'id': 104,
        'customer': 'Meera',
        'status': 'SHIPPED',
        'items': [('keyboard', 1, 1499.0), ('monitor', 1, 10999.0)]
    },
    {
        'id': 105,
        'customer': 'Ravi',
        'status': 'DELIVERED',
        'items': [('mouse', 3, 599.0)]
    }
]


def analyse(orders):

    revenue = {}
    products = {}
    customers = set()
    not_delivered = set()

    for order in orders:

        customer = order['customer']
        status = order['status']

        customers.add(customer)

        if status != 'DELIVERED':
            not_delivered.add(customer)

        if status == 'CANCELLED':
            continue

        for item in order['items']:

            name = item[0]
            quantity = item[1]
            price = item[2]

            amount = quantity * price

            if customer not in revenue:
                revenue[customer] = 0

            revenue[customer] += amount

            if name not in products:
                products[name] = 0

            products[name] += quantity

    # Find top 2 products
    sorted_products = sorted(
        products.items(),
        key=lambda x: (-x[1], x[0])
    )

    top_products = sorted_products[:2]

    # Find fully delivered customers
    fully_delivered = sorted(customers - not_delivered)

    result = {
        'revenue': revenue,
        'top_products': top_products,
        'fully_delivered': fully_delivered
    }

    return result


answer = analyse(orders)

print(answer)
