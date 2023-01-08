from db import db
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models.store import StoreModel
from schemas import StoreSchema
from sqlalchemy.exc import SQLAlchemyError,IntegrityError


blp = Blueprint("Stores", __name__, description="Operations on Stores")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store

    def delete(self, store_id):
        item = StoreModel.query.get_or_404(store_id)
        raise NotImplementedError("Delete has not been implemented")


@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return stores.values()

    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)
    def post(self, store_data):        
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message="This name exists already")
        except SQLAlchemyError:
            abort(500, message="An error occurred")
        
        return store