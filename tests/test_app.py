from app import app


def test_index_displays_monsters(monkeypatch):
    monsters = [{'id': 1, 'name': 'Vampiro', 'power': 'Volar'}]
    monkeypatch.setattr('app.Monster.get_all', lambda: monsters)

    response = app.test_client().get('/')

    assert response.status_code == 200
    assert 'Vampiro' in response.get_data(as_text=True)
    assert 'Volar' in response.get_data(as_text=True)
