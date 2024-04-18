from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app here

client = TestClient(app)

def test_getChatbot():
    response = client.get("/getChatbot", headers={"question": "How often should I change my oil?"})
    assert response.status_code == 200
    assert "change" in response.json()['response']

def test_customChat():
    response = client.get("/customChat", headers={
        "question": "What do I do if my AC is not working?",
        "carIssue": "AC not cooling",
        "carDetails": "2017 Toyota Camry",
        "carDiagnosis": "Refrigerant leak"
    })
    assert response.status_code == 200
    assert "check" in response.json()['response']

def test_getDiagnosis():
    response = client.get("/getDiagnosis", headers={
        "carIssue": "Heavy smoke from exhaust",
        "carDetails": "2015 BMW X5"
    })
    assert response.status_code == 200
    assert "smoke" in response.json()['response']

def test_getParts():
    response = client.get("/getParts", headers={
        "carIssue": "Engine overheating",
        "carDetails": "2013 Ford Escape",
        "carDiagnosis": "Faulty thermostat"
    })
    assert response.status_code == 200
    assert isinstance(response.json()['response'], list)

def test_getMech():
    response = client.get("/getMech", headers={
        "longitude": "123.45",
        "latitude": "-54.321"
    })
    assert response.status_code == 200
    assert "top 5 car auto repairs" in response.json()['response']

# You can use pytest to run these tests.
