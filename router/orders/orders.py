import json
from os import name
from flask import Blueprint

from router.orders.OrdersUtils import Order


orders = Blueprint("orders", __name__)


@orders.route("/statistics", methods=["GET"])
def statistics():
    my_symbols = ["xrpinr", "shibinr", "adainr"]
    res = Order.getOrders(symbols=my_symbols, limit=2)
    print(res.json())
    res = Order.getProfits(res.data)
    return res.json()
