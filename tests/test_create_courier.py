import allure
from api.Api import Api
from asserts.common_asserts import assert_response
from helper import generate_courier
from models.requests_models import Courier

@allure.feature("Создание курьера")
class TestCreateCourier:
    @allure.title("Курьер успешно создается")
    def test_create_courier(self):
        response = Api.create_courier(generate_courier())
        assert_response(response, 201)