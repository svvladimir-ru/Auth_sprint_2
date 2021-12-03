import http


def test_rate_limit(
    client,
    mocked_rate_limit,
):
    response = client.get(
        path="/api/internal/v1/users/info",
    )

    for i in range(6):
        response = client.get(
            path="/api/internal/v1/users/info",
        )

    assert response != 200 # сломался тест
