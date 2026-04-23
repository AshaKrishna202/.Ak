def test_signup_registers_a_new_participant(client):
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": "newstudent@mergington.edu"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Signed up newstudent@mergington.edu for Chess Club"
    }

    activities_response = client.get("/activities")
    participants = activities_response.json()["Chess Club"]["participants"]

    assert "newstudent@mergington.edu" in participants


def test_signup_rejects_unknown_activity(client):
    response = client.post(
        "/activities/Robotics Club/signup",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_signup_rejects_duplicate_participant(client):
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": "michael@mergington.edu"},
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Student already signed up for this activity"
    }


def test_unregister_removes_participant(client):
    response = client.delete(
        "/activities/Drama Club/participants",
        params={"email": "marcus@mergington.edu"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Removed marcus@mergington.edu from Drama Club"
    }

    activities_response = client.get("/activities")
    participants = activities_response.json()["Drama Club"]["participants"]

    assert "marcus@mergington.edu" not in participants


def test_unregister_rejects_unknown_activity(client):
    response = client.delete(
        "/activities/Robotics Club/participants",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_rejects_missing_participant(client):
    response = client.delete(
        "/activities/Drama Club/participants",
        params={"email": "notfound@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Participant not found for this activity"
    }