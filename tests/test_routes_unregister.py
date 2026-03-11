from src.app import activities


def test_unregister_succeeds_for_registered_student(client):
    email = activities["Chess Club"]["participants"][0]

    response = client.post("/activities/Chess%20Club/unregister", params={"email": email})

    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from Chess Club"
    assert email not in activities["Chess Club"]["participants"]


def test_unregister_fails_when_student_not_registered(client):
    response = client.post("/activities/Chess%20Club/unregister", params={"email": "missing@mergington.edu"})

    assert response.status_code == 400
    assert response.json()["detail"] == "Student is not signed up for this activity"


def test_unregister_fails_for_unknown_activity(client):
    response = client.post(
        "/activities/Unknown%20Club/unregister", params={"email": "student@mergington.edu"}
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
