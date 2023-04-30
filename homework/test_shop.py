"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart(product):
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity_positive(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(999)

    def test_product_check_quantity_border(self, product):
        assert product.check_quantity(1000)

    def test_product_check_quantity_negative(self, product):
        assert not product.check_quantity(1001)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(900)
        assert product.quantity == 100

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


"""
  TODO Напишите тесты на методы класса Cart
      На каждый метод у вас должен получиться отдельный тест
      На некоторые методы у вас может быть несколько тестов.
      Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
  """


class TestCart:

    def test_add_new_product(self, cart, product):
        cart.add_product(product, 200)
        assert cart.products[product] == 200

    def test_add_product(self, cart, product):
        cart.add_product(product, 200)
        cart.add_product(product, 100)
        assert cart.products[product] == 300

    def test_remove_product(self, cart, product):
        cart.add_product(product, 1000)
        cart.remove_product(product)
        assert cart.products.get(product, None) is None

    def test_remove_product_more_than_available(self, cart, product):
        cart.add_product(product, 1000)
        cart.remove_product(product, 1001)
        assert cart.products.get(product, None) is None

    def test_remove_product_nothing(self, cart, product):
        with pytest.raises(ValueError):
            cart.remove_product(product)

    def test_remove_product_part(self, cart, product):
        cart.add_product(product, 200)
        cart.remove_product(product, 50)
        assert cart.products.get(product, None) == 150

    def test_clear(self, cart, product):
        cart.add_product(product)
        cart.clear()
        assert cart.products == {}

    def test_get_total_price(self, cart, product):
        cart.add_product(product, 10)
        assert cart.get_total_price() == 1000

    def test_buy(self, cart, product):
        cart.add_product(product, 2)
        cart.buy()
        assert cart.products == {} and product.quantity == 998

    def test_negative_buy(self, cart, product):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            cart.buy()