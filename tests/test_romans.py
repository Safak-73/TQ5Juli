
from romans import to_roman

def test_to_roman():
    assert to_roman(1) == 'I'
    assert to_roman(2) == 'II'
    assert to_roman(3) == 'III'
    assert to_roman(4) == 'IIII'
    assert to_roman(5) == 'V'
