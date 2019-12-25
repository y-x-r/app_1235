import pytest,yaml,os,sys

sys.path.append(os.getcwd())
from Base.getData import GetData

def get_sum_data():
    sum_list=[]
    data=GetData().get_yml_data("sum.yml")
    for i in data.values():
        sum_list.append(tuple(i.values()))
    return sum_list
# print(get_sum_data())

class TestSum:
    @pytest.mark.parametrize("a,b,c",get_sum_data())
    def test_sum(self,a,b,c):
        print(a,b,c)
        assert a+b==c