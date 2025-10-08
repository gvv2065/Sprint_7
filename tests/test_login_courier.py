import pytest
import allure
from api.Api import Api
from asserts.common_asserts import assert_response, assert_response_200
from helper import generate_courier, generate_courier_without_field
from models.requests_models import CourierRequest
from data import Courier

@allure.feature("Логин курьера")
class TestLoginCourier:
    @allure.title("Курьер успешно логинится")
    def test_login_courier(self):
        response = Api.login_courier(Courier.LOGIN, Courier.PWD)
        assert assert_response_200(response).get('id') == 624199
        
    @allure.title("Логин с неправильным паролем")
    def test_login_courier_with_wrong_password(self):
        response = Api.login_courier(Courier.LOGIN, "wrongPwd")
        assert assert_response(response, 404).get("message") == 'Учетная запись не найдена'
       
    @pytest.mark.parametrize("remove_field", [
        "login",
        "password",
    ])
    @allure.title("Валидация обязательных полей")
    def test_create_courier_required_fields(self, remove_field):
        auth = {"login": Courier.LOGIN, "password": Courier.PWD}
        auth[remove_field] = None
        response = Api.login_courier(**auth)
        data = assert_response(response, 400)
        assert data.get("message") == "Недостаточно данных для входа"        