import os
import models
from db import db
from flask import Flask
from flask_smorest import Api
from resources.item import blp as ItemBluePrint
from resources.store import blp as StoreBluePrint


def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Store REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist"    
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(ItemBluePrint)
    api.register_blueprint(StoreBluePrint)

    return app


'''
# Retrieve all the existing stores
@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}, 201

# Add a new store 
@app.post("/store")
def create_store():
    store_data = request.get_json()
    if "name" not in store_data:
        abort(400, message="Bad request, name is missing")
    
    for store in stores.values():
        if store_data["name"] == store["name"]:
            abort(400, message=f"Store already exists")
    store_id = uuid.uuid4().hex
    store = {**store_data, "id":store_id}
    stores[store_id] = store
    return store, 201

# Delete a store
@app.delete("/store/<string:store_id>")
def delete_store(store_id):    
    try:   
        del stores[store_id]             
        return {"message": "Store deleted"}, 201
    except KeyError:
        abort(404, message="Store not found")

# Add a new item to a given store
@app.post("/item")
def create_item():
    item_data = request.get_json()    
    if("price" not in item_data or "store_id" not in item_data or "name" not in item_data):
        abort(400, message="Bad request, something is missing")
    
    for item in items.values():
        if(item_data["name"] == item["name"] and item_data["store_id"] == item["store_id"]):
            abort(400, message=f"Item already exists")
    
    if item_data["store_id"] not in stores:
        abort(404, message="Store not found")

    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item
    return item, 201

# Retrieve all the existing items
@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}, 201

# Retrieve an individual store for the given store name
@app.get("/store/<string:store_id>")
def get_store(store_id):    
    try:                
        return {stores[store_id]}, 201
    except KeyError:
        abort(404, message="Store not found")

# Retrieve the item of a store
@app.get("/item/<string:item_id>")
def get_item(item_id):    
    try:                
        return items[item_id], 201
    except KeyError:
        abort(404, message="Item not found")

# Delete an item
@app.delete("/item/<string:item_id>")
def delete_item(item_id):    
    try:   
        del items[item_id]             
        return {"message": "Item deleted"}, 201
    except KeyError:
        abort(404, message="Item not found")

# Update an item
@app.put("/item/<string:item_id>")
def update_item(item_id):
    item_data = request.get_json()
    if("price" not in item_data or "store_id" not in item_data or "name" not in item_data):
        abort(400, message="Bad request, something is missing")
    try:
        item = items[item_id]
        item |= item_data
        return item
    except KeyError:
        abort(404, message="Item not found")
'''