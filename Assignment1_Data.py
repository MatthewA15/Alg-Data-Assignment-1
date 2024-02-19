#Matthew Allicock
#100860998
import time

#load data from file
def load_data(file_path):
    products = []
    with open(file_path, 'r') as file:
        for line in file:
            id, name, price, category = line.strip().split(',')
            products.append({'ID': id, 'Name': name, 'Price': float(price), 'Category': category})
    return products
#insert function
def insert_product(products, new_product):
    products.append(new_product)
#update function
def update_product(products, product_id, new_details):
    for product in products:
        if product['ID'] == product_id:
            product.update(new_details)
            return "Product updated successfully!"
    return "Product not found."
#delete function
def delete_product(products, product_id):
    for i, product in enumerate(products):
        if product['ID'] == product_id:
            del products[i]
            return "Product deleted successfully!"
    return "Product not found."
#search function
def search_product(products, search_term):
    return [product for product in products if search_term.lower() in product['Name'].lower()]
#sorting implemented (Bubble Sort)
def bubble_sort(products):
    n = len(products)
    for i in range(n):
        for j in range(0, n-i-1):
            if products[j]['Price'] > products[j+1]['Price']:
                products[j], products[j+1] = products[j+1], products[j]
#load data from file path
products = load_data(r"C:\Users\matth\DataStructures\product_data.txt")
#insert product
new_product = {'ID': '99999', 'Name': 'New Gadget', 'Price': 299.99, 'Category': 'Electronics'}
insert_product(products, new_product)
#update product
update_message = update_product(products, '57353', {'Price': 550.00})
print(update_message)
#delete product
delete_message = delete_product(products, '40374')
print(delete_message)
#search product
search_results = search_product(products, 'Camera')
print("Search Results:", search_results)
#sort products by price(Bubble Sort)
bubble_sort(products)
print("Sorted Products:", products)