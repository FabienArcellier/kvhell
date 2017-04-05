import pytest
import requests
from faker import Faker


@pytest.fixture(scope="module")
def kv_reset():
    requests.delete('http://localhost:8888')

def test_00_http_request_is_working():
    requests.head('http://localhost:8888')

def benchmark_get_value():
    requests.get('http://localhost:8888/my_value')

def test_put_then_benchmark_then_get_value(benchmark, kv_reset):
    requests.put('http://localhost:8888/my_value', data="")
    benchmark(benchmark_get_value)

def benchmark_put_1_key_then_read_1000():
    fake = Faker()
    requests.put('http://localhost:8888/1', data=fake.text())

    for i in range(0, 1000, 1):
        requests.get('http://localhost:8888/1').content

def test_benchmark_put_1_key_then_read_1000(benchmark, kv_reset):
    benchmark.pedantic(benchmark_put_1_key_then_read_1000, iterations=1, rounds=3)

def benchmark_put_10_keys_then_read_1000():
    fake = Faker()
    for i in range(0, 10, 1):
        requests.put('http://localhost:8888/{0}'.format(i % 10), data=fake.text())

    for i in range(0, 1000, 1):
        requests.get('http://localhost:8888/{0}'.format(i % 10)).content

def test_benchmark_put_10_keys_then_read_1000(benchmark, kv_reset):
    benchmark.pedantic(benchmark_put_10_keys_then_read_1000, iterations=1, rounds=3)

def test_benchmark_put_500_keys(benchmark, kv_reset):
    benchmark.pedantic(benchmark_put_500_keys, iterations=1, rounds=3)

def benchmark_put_500_keys():
    fake = Faker()
    for i in range(0, 500, 1):
        requests.put('http://localhost:8888/{0}'.format(fake.name()), data=fake.text())

def test_benchmark_put_500_keys(benchmark, kv_reset):
    benchmark.pedantic(benchmark_put_500_keys, iterations=1, rounds=3)

def benchmark_put_500_keys_then_read_each_key():
    for i in range(0, 500, 1):
        requests.put('http://localhost:8888/{0}'.format(i), data="fake {0}".format(i))

    for i in range(0, 500, 1):
        assert "fake {0}".format(i) == requests.get('http://localhost:8888/{0}'.format(i)).content

def test_benchmark_put_500_keys_then_read_each_key(benchmark, kv_reset):
    benchmark.pedantic(benchmark_put_500_keys_then_read_each_key, iterations=1, rounds=3)

def benchmark_put_1000_keys_then_read_10():
    fake = Faker()
    for i in range(0, 1000, 1):
        requests.put('http://localhost:8888/{0}'.format(i % 10), data=fake.text())

    for i in range(0, 10, 1):
        requests.get('http://localhost:8888/{0}'.format(i % 10)).content

def test_benchmark_put_1000_keys_then_read_10(benchmark, kv_reset):
    benchmark.pedantic(benchmark_put_1000_keys_then_read_10, iterations=1, rounds=3)
