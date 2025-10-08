import requests 
from data import Url
from models.requests_models import CourierRequest
import json
import allure

class Api:
    @staticmethod
    @allure.step("api: получение списка заказов")
    def get_orders() -> requests.Response:
        response = requests.get(Url.ORDERS)
        return response.json() 
    
    @staticmethod
    @allure.step("api: создание курьера")
    def create_courier(courier: CourierRequest) -> requests.Response:
        response = requests.post(Url.COURIER, data=courier.__dict__)
        return response