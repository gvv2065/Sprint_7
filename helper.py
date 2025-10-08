from datetime import datetime, timedelta
import random
import string
from models.requests_models import CourierRequest, OrderRequest
from dataclasses import dataclass, replace
from faker import Faker

def generate_courier() -> CourierRequest: 
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    return CourierRequest(login, password, first_name)

def generate_courier_without_field(field_to_remove) -> CourierRequest: 
    courier = generate_courier()
    return replace(courier, **{field_to_remove: None})

def generate_order_request_with_override(override: OrderRequest) -> CourierRequest:
    return replace(generate_order_request(), **override.__dict__)

def generate_order_request() -> OrderRequest:
    fake = Faker(locale="ru_RU")
    # Генерация случайных данных
    first_name = fake.first_name()
    last_name = fake.last_name()
    address = fake.address()
    metro_station = random.randint(1, 230)
    phone = fake.phone_number()
    
    # Генерация времени аренды
    rent_time = random.randint(1, 30)
    
    # Генерация даты доставки (на ближайшие 7 дней)
    delivery_date = (datetime.now() + timedelta(days=random.randint(1, 7))).strftime('%Y-%m-%d')
    
    comment = fake.sentence()
    
    color = [random.choice(["BLACK", "GREY"])]
    
    return OrderRequest(
        firstName=first_name,
        lastName=last_name,
        address=address,
        metroStation=metro_station,
        phone=phone,
        rentTime=rent_time,
        deliveryDate=delivery_date,
        comment=comment,
        color=color
    )