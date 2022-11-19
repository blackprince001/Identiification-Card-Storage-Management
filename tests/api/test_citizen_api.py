from api.citizen import create_citizen, get_citizen


def test_create_citizen(db, citizen):
    db_citizen = create_citizen(db=db, new_citizen=citizen)

    assert db_citizen.firstnames == "Prince"
    assert db_citizen.surnames == "Appiah"
    assert db_citizen.card_number


def test_get_citizen(db, citizen):
    db_citizen = create_citizen(db=db, new_citizen=citizen)

    res = get_citizen(db=db, citizen_id=1)

    assert res.age == 99
    assert res.place_of_birth == "Amakom Kumasi"
