import pytest
from flask import g, session
from flaskr.db import get_db


def test_add_gear(gear, app):
    assert gear.get('/gears/create').status_code == 200
    response = gear.post(
        '/gears/create', data={'name': 'gearTest', 'desc': 'asdqsdqsd'}
    )
    assert response.headers["Location"] == "/auth/login"

    with app.app_context():
        assert get_db().execute(
            "SELECT * FROM gear WHERE name = 'gearTest'",
        ).fetchone() is not None


@pytest.mark.parametrize(('name', 'desc', 'message'), (
    ('', '', b' name is required.'),
    ('gearTest', '', b' desc is required.'),
    ('test', 'test', b' ok.'),
))
def test_register_validate_input(gear, name, desc, message):
    response = gear.post(
        '/gears/create',
        data={'name': name, 'desc': desc}
    )
    assert message in response.data