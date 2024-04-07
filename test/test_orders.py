import pytest
from orders import Orders


@pytest.fixture
def fetch_orders():
    return Orders()

def test_default_scenario(fetch_orders):
    orders = [70, 30, 10]
    n_max = 100
    expected_trips = 2
    actual_trips = fetch_orders.combine_orders(orders, n_max)
    assert actual_trips == expected_trips

def test_orders_empty_requests(fetch_orders):
    orders = []
    n_max = 100
    expected_trips = 0
    actual_trips = fetch_orders.combine_orders(orders, n_max)
    assert actual_trips == expected_trips

def test_orders_with_maximum_request(fetch_orders):
    orders = [100, 100, 100]
    n_max = 100
    expected_trips = 3
    actual_trips = fetch_orders.combine_orders(orders, n_max)
    assert actual_trips == expected_trips
