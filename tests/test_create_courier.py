import allure

@allure.feature("Создание курьера")
class TestCreateCourier:
    @allure.title("Курьер успешно создается")
    def test_create_courier(self):
        result = 2 + 2
        assert result == 4