from fixture.load_dll import DllHelper
from fixture.work_with_db import DbHelper
import pytest


@pytest.fixture
def fix(request):
    fixture = DllHelper()
    # функция disconnect передается в качестве параметра
    request.addfinalizer(fixture.disconnect)
    return fixture

@pytest.fixture
def fixdb(request):
    fixture = DbHelper()
    # функция disconnect передается в качестве параметра
    request.addfinalizer()
    return fixture