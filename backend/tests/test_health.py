def test_health_check(client):
    """
    Verifies that the health check endpoint returns a 200 status 
    and the correct JSON payload.
    """
    response = client.get("/api/v1/health/")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
