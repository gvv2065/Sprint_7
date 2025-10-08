import requests 
from data import Url
from models.requests_models import CourierRequest, OrderRequest
import json
import allure

class Api:
    @staticmethod
    @allure.step("api: получение списка заказов")
    def get_orders() -> requests.Response:
        response = requests.get(Url.ORDERS)
        return response
    
    @staticmethod
    @allure.step("api: создание курьера")
    def create_courier(courier: CourierRequest) -> requests.Response:
        response = requests.post(Url.COURIER, data=courier.__dict__)
        return response
    
    @staticmethod
    @allure.step("api: login курьера")
    def login_courier(login, password) -> requests.Response:
        response = requests.post(Url.COURIER_LOGIN,
            data=json.dumps({"login":login, "password":password}),
            headers={"Content-Type": "application/json"}
        )
        return response
    
    @staticmethod
    @allure.step("api: создание заказа")
    def create_order(order: OrderRequest) -> requests.Response:
        response = requests.post(Url.ORDER_CREATE,
            data=json.dumps(order.__dict__),
            headers={"Content-Type": "application/json"}
        )
        return response