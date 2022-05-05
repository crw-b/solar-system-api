def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []
    
def test_get_all_planeets(client, two_planets):
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

def test_delete_planet(client, two_planets):

    response = client.delete("/planets/1")
    response_body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert response_body == '*** You have successfully destroyed Earth ! ***'


def test_get_planet_id_not_found(client):

    response = client.delete("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {'details': 'No planet with id 1 found'}
        
      