from db import db
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models.item import ItemModel
from sqlalchemy.exc import SQLAlchemyError
from schemas import ItemSchema, ItemUpdateSchema


blp = Blueprint("Items", __name__, description="Operations on Items")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
            item = ItemModel.query.get_or_404(item_id)
            return item

    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        raise NotImplementedError("Delete has not been implemented")

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):              
        item = ItemModel.query.get_or_404(item_id)
        raise NotImplementedError("Update has not been implemented")


@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return items.values()

    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred")
        return item