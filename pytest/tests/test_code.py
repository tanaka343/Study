import pytest
from src import code

def test_sum_numbers():
    result1,result2=code.sum_numbers(1,2)
    
    assert result1==3
    assert result2==1

def get_json_data_mock(id):
    return{'name':'サプー'}

def test_get_user_names(monkeypatch):
    monkeypatch.setattr(
        code,'get_json_data',get_json_data_mock
    )
    result= code.get_user_names(['001','009'])

    assert list(result.keys())==['001','009']
    assert list(result.values())==['サプー','サプー']

def test_user_name_validation():
    with pytest.raises(ValueError) as e:
        code.user_name_validation(None)
    assert str(e.value) == '名前未設定'
