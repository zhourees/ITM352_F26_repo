# Calculating an extended price for a product (with tax)
# Name: Reesa Zhou
# Date: October 17, 2026

product = {
    "name": 'small gumball', 
    "price": 0.34
}

tax_rate = 0.045

total = product["price"] + product["price"] * tax_rate

print(f"A {product["name"]} costs ${total}")
