import pytest
import allure
from api.Api import Api
from asserts.common_asserts import assert_response
from helper import generate_courier, generate_courier_without_field
from models.requests_models import CourierRequest

@allure.feature("Создание курьера")
class TestCreateCourier:
    @allure.title("Курьер успешно создается")
    def test_create_courier(self):
        response = Api.create_courier(generate_courier())
        assert_response(response, 201)
    
    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_existed_courier(self):
        courier = generate_courier()
        response = Api.create_courier(courier)
        assert_response(response, 201)
        response = Api.create_courier(courier)
        data = assert_response(response, 409)
        assert data.get("message") == "Этот логин уже используется"
        
    
    remove_field = [
        "login",
        "password",
    ]
    @pytest.mark.parametrize("remove_field", remove_field)
    @allure.title("Проверка обязательности полей")
    def test_create_courier_required_fields(self, remove_field):
        courier = generate_courier_without_field(remove_field)
        response = Api.create_courier(courier)
        data = assert_response(response, 400)
        assert data.get("message") == "Недостаточно данных для создания учетной записи"
        