#test_calc.py
from calc import square

def main():
    test_square()


def test_square():
        assert square(2) == 4
        assert square(3) == 9
        assert square(4) == 16

if __name__ == "__main__":
    main()

# RUN: pytest unit_test.py (in terminal)