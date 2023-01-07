from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items":[
            {
                "name": "Chair",
                "price": 15.99
            },
            {
                "name": "Table",
                "price": 158.9
            }
        ]
    },
    {
        "name": "eBay Store",
        "items":[
            {
                "name": "Curtains",
                "price": 23.98
            },
            {
                "name": "Cupboard",
                "price": 250.70
            }
        ]
    }
]


@app.get("/store")
def get_stores():
    return {"stores": stores}


@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items":[]}
    stores.append(new_store)
    return new_store, 201


@app.post("/store/<string:name>")
def create_item(name):
    pass