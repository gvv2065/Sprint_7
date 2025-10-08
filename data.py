
from helper import generate_order_request, generate_order_request_with_override
from models.requests_models import OrderRequest


class Url:
    BASE_API = "https://qa-scooter.praktikum-services.ru/api/v1"
    ORDERS = BASE_API  + "/orders"
    COURIER = BASE_API  + "/courier"
    COURIER_LOGIN = COURIER + "/login"
    ORDER_CREATE = ORDERS
    
class Courier:
    LOGIN = 'gvv'
    PWD = '1234'
    
def get_orders_for_success_create():
    return [
        generate_order_request(),
        generate_order_request_with_override(OrderRequest(color=["BLACK"])),
        generate_order_request_with_override(OrderRequest(color=["GRAY"])),
        generate_order_request_with_override(OrderRequest(color=["GRAY","BLACK"])),
        generate_order_request_with_override(OrderRequest(color=None)),
    ]
    