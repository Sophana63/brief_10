import pytest
from flask import g, session
from flaskr.db import get_db



def test_add_gear(client, app):
    assert client.get('/gears/create').status_code == 302
    response = client.post(
        '/gears/create', data={'name': 'gearTest', 'desc': 'asdqsdqsd', 'arg': 1}
    )
    assert response.headers["Location"] == "/auth/login"

    with app.app_context():
        assert get_db().execute(
            "SELECT * FROM gear WHERE name = 'gearTest'",
        ).fetchone() is not None


@pytest.mark.parametrize(('name', 'desc', 'arg', 'message'), (
    ('', '', '', b' name is required.'),
    ('gearTest', '', '',  b' description is required.'),
    ('gearTest', 'test', '', b' argument is required.'),
    ('gearTest', 'test', '1', b' ok.'),
))
def test_register_validate_input(client, name, desc, arg, message):
    response = client.post(
        '/gears/create',
        data={'name': name, 'desc': desc, 'arg': arg}
    )
    assert message in response.data