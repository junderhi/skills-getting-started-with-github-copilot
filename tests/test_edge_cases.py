from src.app import activities


def test_signup_with_empty_email_is_currently_accepted(client):
    response = client.post("/activities/Chess%20Club/signup", params={"email": ""})

    assert response.status_code == 200
    assert response.json()["message"] == "Signed up  for Chess Club"
    assert "" in activities["Chess Club"]["participants"]


def test_signup_and_unregister_mutate_participants_exactly_once(client):
    email = "statecheck@mergington.edu"
    starting_count = len(activities["Chess Club"]["participants"])

    signup_response = client.post("/activities/Chess%20Club/signup", params={"email": email})
    assert signup_response.status_code == 200
    assert activities["Chess Club"]["participants"].count(email) == 1

    unregister_response = client.post("/activities/Chess%20Club/unregister", params={"email": email})
    assert unregister_response.status_code == 200
    assert email not in activities["Chess Club"]["participants"]
    assert len(activities["Chess Club"]["participants"]) == starting_count
