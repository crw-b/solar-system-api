def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []
    
def test_get_all_planets(client, two_planets):
    response = client.get('/planets')

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [{"id":1,
        "name": "Earth",
        "description": "home",
        "moons": "Luna",
        "life":"True"},
        {"id":2,
        "name": "Mars",
        "description": "1st Colony",
        "moons": "None",
        "life":"True"}]

def test_get_planet_by_id(client, two_planets):
    response = client.get("planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id":1,
        "name": "Earth",
        "description": "home",
        "moons": "Luna",
        "life":"True"
    }

def test_get_planet_by_invalid_id(client):
    response = client.get("planets/a")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"details":"Invalid id a"}

def test_create_one_planet(client):

    response = client.post("/planets", json={
        "name": "Pluto",
        "description": "A real planet!",
        "moons": "None",
        "life":"False"
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {
        "id":1,
        "name": "Pluto",
        "description": "A real planet!",
        "moons": "None",
        "life":"False"
    }

def test_create_planet_with_a_missing_key(client):

    response = client.post("/planets", json={
        "description": "A big blue planet!",
        "moons": "Luna",
        "life":"True"
    })

    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"details":"Missing key: 'name'"}


def test_delete_planet(client, two_planets):

    response = client.delete("/planets/1")
    response_body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert response_body == '*** You have successfully destroyed Earth ! ***'


def test_get_planet_id_not_found(client):

    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {'details': 'No planet with id 1 found'}



def test_update_planet_description(client, two_planets):

    response = client.patch("/planets/1", json={
        "description": "A big blue planet!",
    })

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id" : 1,
        "name": "Earth",
        "description": "A big blue planet!",
        "moons": "Luna",
        "life":"True"
    }

def test_update_planet_name(client, two_planets):

    response = client.patch("/planets/1", json={
        "name": "Earth 2.0",
    })

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id" : 1,
        "name": "Earth 2.0",
        "description": "home",
        "moons": "Luna",
        "life":"True"
    }

def test_update_planet_life(client, two_planets):

    response = client.patch("/planets/1", json={
        "life":"Not anymore",
    })

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id" : 1,
        "name": "Earth",
        "description": "home",
        "moons":"Luna",
        "life":"Not anymore"
    }

def test_update_planet_moons(client, two_planets):

    response = client.patch("/planets/1", json={
        "moons":"Not anymore",
    })

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id" : 1,
        "name": "Earth",
        "description": "home",
        "moons":"Not anymore",
        "life":"True"
    }

def test_update_planet_with_a_put(client, two_planets):

    response = client.put("/planets/1", json={
        "name": "Earth",
        "description": "A big blue planet!",
        "moons": "Luna",
        "life":"True"
    })

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id" : 1,
        "name": "Earth",
        "description": "A big blue planet!",
        "moons": "Luna",
        "life":"True"
    }

def test_update_planet_with_a_put_missing_key(client, two_planets):

    response = client.put("/planets/1", json={
        "description": "A big blue planet!",
        "moons": "Luna",
        "life":"True"
    })

    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"details":"Missing key: 'name'"}