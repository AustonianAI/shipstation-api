from flask.json import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint

from utils.api.shipstation import get_ss_orders

blp = Blueprint("shipstation", __name__, url_prefix="/shipstation")


@blp.route("/")
class ShipStationResource(MethodView):

    def get(self):

        all_orders = get_ss_orders()

        order_ids = [order.orderId for order in all_orders]

        return jsonify(order_ids)
