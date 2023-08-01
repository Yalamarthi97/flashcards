import sys


# setting path
sys.path.append("../rest_api")
from app import app


def test_base():
    response = app.test_client().get("/")
    print(response.status, response.get_data())
    assert response.status_code == 200
    assert response.get_data("utf-8") == "Working Perfectly!!"
