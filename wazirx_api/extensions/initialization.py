import re
from router.orders import orders


# Blueprints registration
def install_blueprints(app):
    app.register_blueprint(orders.orders, url_prefix="/orders")
    return app
