import pytest

def test_fill_data_base(client) -> None:
    response = client.get('factories/fill_data_base')
    pytest.assume(response.status.startswith('200'))
    