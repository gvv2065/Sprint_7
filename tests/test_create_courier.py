import allure
from api.Api import Api
from asserts.common_asserts import assert_response
from helper import generate_courier

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
        