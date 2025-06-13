import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_calculate():
    with app.test_client() as client:
        response = client.get('/api/calculate?num1=2&num2=3')
        assert response.status_code == 200
        data = response.get_json()
        assert data['result'] == 5
