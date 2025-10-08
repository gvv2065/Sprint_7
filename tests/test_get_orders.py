import allure
from api.Api import Api
from asserts.common_asserts import assert_response

@allure.feature("Список заказов")
class TestGetOders:    

    @allure.title("Заказы успешно получены")
    def test_create_order(self):
        response = Api.get_orders()
        data = assert_response(response, 200)
        order = data.get("orders")[0]
        assert order != None
        fields = [
            "id", 
            "courierId", 
            "firstName", 
            "lastName", 
            "address", 
            "metroStation", 
            "phone", 
            "rentTime", 
            "deliveryDate", 
            "track", 
            "color", 
            "comment", 
            "createdAt", 
            "updatedAt", 
            "status",
        ]

        for field in fields:
            assert field in order, f"Отсутствует поле {field} в ответе"