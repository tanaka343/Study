import pytest
from src import code

@pytest.mark.parametrize("input_data,expected",[
    ((1,2),3),
    ((2,3),5)
])

# def test_sum_numbers():
#     result1=code.sum_numbers(1,2)
    
#     assert result1==3

def test_sum_numbers2(input_data,expected):
    assert code.sum_numbers(*input_data) == expected


   





def get_json_data_mock(id):
    return{'name':'サプー'}

def test_get_user_names(monkeypatch):
    monkeypatch.setattr(
        code,'get_json_data',get_json_data_mock
    )
    result= code.get_user_names(['001','009'])

    assert list(result.keys())==['001','009']
    assert list(result.values())==['サプー','サプー']

# def test_user_name_validation():
#     with pytest.raises(ValueError) as e:
#         code.user_name_validation(None)
#     assert str(e.value) == '名前未設定'
