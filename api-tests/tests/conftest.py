import os
import pytest

@pytest.fixture
def base_url():
    return os.environ.get("BASE_URL", "https://jsonplaceholder.typicode.com")