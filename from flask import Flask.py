
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

products = [ {"id": 1, "name": "Laptop", "price": 999.99, "stock": 10}, 
              {"id": 2, "name": "Smartphone", "price": 499.99, "stock": 20}, 
              {"id": 3, "name": "Tablet", "price": 299.99, "stock": 15}
              ]

@app.route("/getAllProducts", methods=['GET'])

def getAllProducts(sort, price):
    
    return jsonify(products)

 

@app.route("/getProductById/<productId>", methods=['GET'])
def getProductById(productId):
    for product in products:
        if (product['id'] == int(productId)):
            return jsonify(product)
        
    return 'no data found'
        
@app.route("/addProduct", methods=['POST'])
def addProduct():

    # request and response

    product = request.json

    products.append(product)

    return jsonify(" The new product has been added")

if __name__=='__main__':
  app.run(debug=True)