import pytest
from Methods.Methods import Methods
from Config.TestData import TestData


@pytest.fixture
def api():
    return Methods(base_url=TestData.BASE_URL, headers={'Authorization': f'Bearer {TestData.ACCESS_TOKEN}'})
