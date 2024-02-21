from flask.views import MethodView
from flask_smorest import Blueprint

from utils.api.shipstation import get_ss_orders

blp = Blueprint("shipstation", __name__, url_prefix="/shipstation")


@blp.route("/")
class ShipStationResource(MethodView):

    def get(self):

        return get_ss_orders()
