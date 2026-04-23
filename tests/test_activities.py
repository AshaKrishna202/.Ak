def test_get_activities_returns_all_activities(client):
    response = client.get("/activities")

    assert response.status_code == 200

    payload = response.json()

    assert isinstance(payload, dict)
    assert len(payload) == 9
    assert "Chess Club" in payload
    assert payload["Chess Club"] == {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"],
    }


def test_get_activities_returns_expected_fields(client):
    response = client.get("/activities")

    payload = response.json()
    activity = payload["Drama Club"]

    assert set(activity) == {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }
    assert activity["participants"] == ["marcus@mergington.edu", "isabella@mergington.edu"]