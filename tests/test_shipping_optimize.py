"""
    Testing ground;
    INPUTS contains contract inputs[i]
    OUTPUT contians output outputs[i]

    each test case asserts inputs[i] == outputs[i]
"""

INPUTS = [[
    {"name": "Contract1", "start": 0, "duration": 5, "price": 10},
    {"name": "Contract2", "start": 3, "duration": 7, "price": 14},
    {"name": "Contract3", "start": 5, "duration": 9, "price": 8},
    {"name": "Contract4", "start": 5, "duration": 9, "price": 7}],
[
    {"name": "Contract1", "start": 0, "duration": 2, "price": 100},
    {"name": "Contract2", "start": 0, "duration": 4, "price": 200}, 
    {"name": "Contract3", "start": 0, "duration": 6, "price": 300}, 
    {"name": "Contract4", "start": 0, "duration": 10, "price": 500}],
[
    {"name": "Contract1", "start": 0, "duration": 1, "price": 100},
    {"name": "Contract2", "start": 0, "duration": 2, "price": 200}, 
    {"name": "Contract3", "start": 0, "duration": 2, "price": 300}, 
    {"name": "Contract4", "start": 1, "duration": 2, "price": 500}],
[
    {"name": "Contract1", "start": 0, "duration": 5, "price": 10},
    {"name": "Contract2", "start": 3, "duration": 7, "price": 14},
    {"name": "Contract3", "start": 2, "duration": 9, "price": 8},
    {"name": "Contract4", "start": 0, "duration": 9, "price": 7}],
[
    {"name": "Contract1", "start": 0, "duration": 2, "price": 10},
    {"name": "Contract2", "start": 2, "duration": 6, "price": 14},
    {"name": "Contract3", "start": 6, "duration": 2, "price": 8},
    {"name": "Contract4", "start": 10, "duration": 9, "price": 7}],
[
    {"name": "Contract1", "start": 0, "duration": 2, "price": 10},
    {"name": "Contract2", "start": 0, "duration": 4, "price": 20},
    {"name": "Contract3", "start": 2, "duration": 5, "price": 8},
    {"name": "Contract4", "start": 0, "duration": 6, "price": 7}],
[
    {"name": "Contract1", "start": 0, "duration": 2, "price": 20},
    {"name": "Contract2", "start": 6, "duration": 2, "price": 20},
    {"name": "Contract3", "start": 6, "duration": 2, "price": 80},
    {"name": "Contract4", "start": 4, "duration": 2, "price": 50}]
]

OUTPUTS = [
    {'income': 18, 'path': ['Contract1', 'Contract3']},
    {'income': 500, 'path': ['Contract4']},
    {'income': 600, 'path': ['Contract1', 'Contract4']},
    {'income': 14, 'path': ['Contract2']},
    {'income': 25, 'path': ['Contract1', 'Contract3', 'Contract4']},
    {'income': 20, 'path': ['Contract2']},
    {'income': 150, 'path': ['Contract1', 'Contract4', 'Contract3']}
]

def test_case_0(client):
    response = client.post("/spaceship/optimize", json=INPUTS[0])
    assert response.json == OUTPUTS[0]

def test_case_1(client):
    response = client.post("/spaceship/optimize", json=INPUTS[1])
    assert response.json == OUTPUTS[1]

def test_case_2(client):
    response = client.post("/spaceship/optimize", json=INPUTS[2])
    assert response.json == OUTPUTS[2]

def test_case_3(client):
    response = client.post("/spaceship/optimize", json=INPUTS[3])
    assert response.json == OUTPUTS[3]

def test_case_4(client):
    response = client.post("/spaceship/optimize", json=INPUTS[4])
    assert response.json == OUTPUTS[4]

def test_case_5(client):
    response = client.post("/spaceship/optimize", json=INPUTS[5])
    assert response.json == OUTPUTS[5]

def test_case_6(client):
    response = client.post("/spaceship/optimize", json=INPUTS[6])
    assert response.json == OUTPUTS[6]