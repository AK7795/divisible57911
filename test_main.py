import main
import pytest

@pytest.mark.parametrize("n1,out1",[(5,True),(7,False),(10,True),(9,False)])
def test_divby5_1(n1,out1):
    out1 = main.divby5(n1)
    assert out1 == out1

@pytest.mark.parametrize("n2,out2",[(7,True),(8,False),(14,True),(20,False)])
def test_divby7_1(n2,out2):
    out1 = main.divby7(n2)
    assert out1 == out2


@pytest.mark.parametrize("n3,out3",[(9,True),(8,False),(18,True),(20,False)])
def test_divby9_1(n3,out3):
    out1 = main.divby9(n3)
    assert out1 == out3


@pytest.mark.parametrize("n4,out4",[(11,True),(8,False),(33,True),(20,False)])
def test_divby11_1(n4,out4):
    out1 = main.divby11(n4)
    assert out1 == out4



