from app import app

def test_calculate():
    client = app.test_client()
    response = client.get('/api/calculate?num1=2&num2=3')
    assert response.status_code == 200
    assert response.json['result'] == 5.0
