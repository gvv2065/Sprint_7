import pytest
import allure
from api.Api import Api
from asserts.common_asserts import assert_response
from data import get_orders_for_success_create

@allure.feature("Создание заказа")
class TestCreateOder:    

    @pytest.mark.parametrize("order", get_orders_for_success_create())
    @allure.title("Заказ успешно создается")
    def test_create_order(self, order):
        response = Api.create_order(order)
        data = assert_response(response, 201)
        assert data.get("track") != None
    