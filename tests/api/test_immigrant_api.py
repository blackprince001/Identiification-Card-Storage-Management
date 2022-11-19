from api.immigrant import create_immigrant, get_immigrant


def test_create_immigrant(db, immigrant):
    db_immigrant = create_immigrant(db=db, new_immigrant=immigrant)

    assert db_immigrant.firstnames == "Black"
    assert db_immigrant.surnames == "Prince"
    assert db_immigrant.nationality == "Pirate"


def test_get_immigrant(db, immigrant):
    db_immigrant = create_immigrant(db=db, new_immigrant=immigrant)

    res = get_immigrant(db=db, immigrant_id=db_immigrant.id)

    assert res.age == 99
    assert res.sex == "F"
