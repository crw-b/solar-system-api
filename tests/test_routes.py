def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []
    
def test_index_planets_with_empty_db_return_empty_list(client):
    response = client.get('/planets')

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_planet_by_id(client, two_planets):
    response = client.get("planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id":1,
        "name": "Earth",
        "description": "home",
        "moons": "Luna",
        "life":True
    }