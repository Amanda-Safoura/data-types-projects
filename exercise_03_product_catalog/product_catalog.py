from collections import namedtuple, defaultdict


def expensive_products(products, limit):
    return [p.name for p in products if p.price > limit]


def sorted_by_price(products):
    return [p.name for p in sorted(products, key=lambda x: x.price)]


def order_by_category(products):
    categories_products = defaultdict(list)
    
    for p in products:
        categories_products[p.category].append(p.name)
        
    return categories_products


products = [
    ("Laptop", 1200, "IT"),
    ("Mouse", 25, "IT"),
    ("Chair", 150, "Furniture"),
    ("Desk", 300, "Furniture")
]

Product = namedtuple('Product', ['name', 'price', 'category'])
products = [Product(name, price, category) for name, price, category in products]

print(expensive_products(products, 500))

sorted_products = sorted_by_price(products)
print(sorted_products)

categories = order_by_category(products)
print(categories)