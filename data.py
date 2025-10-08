
class Url:
    BASE_API = "https://qa-scooter.praktikum-services.ru/api/v1"
    ORDERS = BASE_API  + "/orders"
    COURIER = BASE_API  + "/courier"
    COURIER_LOGIN = COURIER + "/login"
    
class Courier:
    LOGIN = 'gvv'
    PWD = '1234'