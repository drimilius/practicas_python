import json
def read_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
def write_json(filename, jsdata):
    with open(filename, 'w') as file:
        data = json.dump(jsdata, file, indent=4)
#agragar producto 
def add_product(data, product):
    data["products"].append(product)

#actualizar la cantiadad de productos existentes
def update_product(data, product_id, new_quantity):
    for product in data["products"]:
        if product["id"] == product_id:
            product["quantity"] = new_quantity
            break
    return False

def remove_product(data, product_id):
    data["products"]= [product for product in data["products"] if product["id"] != product_id]
    
#mostrar productos
def show_products(data):
    print("lista de productos")
    for product in data["products"]:
        print(f"ID: {product['id']}, Nombre: {product['name']}, Precio: {product['price']}, Cantidad: {product['quantity']}")
        

#main
filename= "files/json/products.json"
data = read_json(filename)
show_products(data)

update_product(data, 2, 30)
show_products(data)

remove_product(data, 1)
show_products(data)
write_json(filename, data)

new_product = {"id": 4, "name": "Taza", "price": 50, "quantity": 10}
write_json(filename, data)

