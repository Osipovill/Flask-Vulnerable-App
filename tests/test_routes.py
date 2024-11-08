import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_main_page(client):
    response = client.get('/')
    a = response
    assert response.status_code == 200
    assert "Главное меню" in response.data.decode("utf-8")

def test_complex_theory(client):
    response = client.get('rce/complex')
    assert response.status_code == 200

def test_complex_practice_get(client):
    response = client.get('rce/complex/practice')
    assert response.status_code == 200

def test_complex_practice_post(client):
    response = client.post('rce/complex/practice', data={'env_var': 'test'})
    assert response.status_code == 200
    assert b'test' in response.data

def test_level1_theory(client):
    response = client.get('sqli/level1')
    assert response.status_code == 200

def test_level1_practice_get(client):
    response = client.get('sqli/level1/practice')
    assert response.status_code == 200

def test_level1_practice_post(client):
    response = client.post('sqli/level1/practice', data={'name': 'admin'})
    assert response.status_code == 200

def test_level2_theory(client):
    response = client.get('sqli/level2')
    assert response.status_code == 200

def test_level2_practice_post(client):
    response = client.post('sqli/level2/practice', data={'username': 'admin', 'password': 'password'})
    assert response.status_code == 200

def test_level3_theory(client):
    response = client.get('sqli/level3')
    assert response.status_code == 200

def test_level3_practice_post(client):
    response = client.post('sqli/level3/practice', data={'user_id': '1'})
    assert response.status_code == 200

def test_level3hard_theory(client):
    response = client.get('sqli/level3hard')
    assert response.status_code == 200

def test_level3hard_practice_post(client):
    response = client.post('sqli/level3hard/practice', data={'user_id': '1'})
    assert response.status_code == 200

def test_ssti_level1_theory(client):
    response = client.get('ssti/level1')
    assert response.status_code == 200

def test_ssti_level1_practice(client):
    response = client.get('ssti/level1/practice?name=Admin')
    assert response.status_code == 200
    assert b"Admin" in response.data

def test_ssti_level2_theory(client):
    response = client.get('ssti/level2')
    assert response.status_code == 200

def test_ssti_level2_practice(client):
    response = client.get('ssti/level2/practice?name=Admin')
    assert response.status_code == 200
    assert b"Admin" in response.data

def test_xss_level1_theory(client):
    response = client.get('xss/level1')
    assert response.status_code == 200

def test_xss_level1_practice(client):
    response = client.post('xss/level1/practice', data={'comment': '<b>Test Comment</b>'})
    assert response.status_code == 200
    assert b"<b>Test Comment</b>" in response.data

def test_xss_level2_theory(client):
    response = client.get('xss/level2')
    assert response.status_code == 200

def test_xss_level2_practice(client):
    client.post('xss/level2/practice', data={'comment': '<b>Test Comment</b>'})
    response = client.get('xss/level2/practice')
    assert response.status_code == 200
    assert b"<b>Test Comment</b>" in response.data

def test_xss_level3_theory(client):
    response = client.get('xss/level3')
    assert response.status_code == 200

def test_xss_level3_practice(client):
    client.post('xss/level3/practice', data={'comment': '<script>alert("XSS")</script>'})
    response = client.get('xss/level3/practice')
    assert response.status_code == 200
    assert b'<script>' not in response.data

def test_delete_comments(client):
    client.post('xss/level2/practice', data={'comment': 'Test Comment'})
    response = client.post('xss/delete_comments')
    assert response.status_code == 302
    response = client.get('/level2/practice')
    assert b'Test Comment' not in response.data

def test_scan_route(client):
    response = client.get('/scan')
    assert response.status_code == 200
