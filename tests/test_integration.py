from src.service import register_name

def test_register_name():
    data = []
    result = register_name(data, "Luis")

    assert result == ["Luis"]