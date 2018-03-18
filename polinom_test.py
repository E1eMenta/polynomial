from unittest import TestCase, main
from polinom import Polynomial

def equal_lists(list1, list2):
    return all([l1 == l2 for l1, l2 in zip(list1, list2)])

class SumTest(TestCase):
    def setup_method(self):
        self.p1 = Polynomial([1, -4, 6])
        self.p2 = Polynomial([2, 6])
        self.p3 = Polynomial([-1, 1])
        self.p4 = Polynomial([4, 2, 10, -1])
    def test_sum(self):
        self.setup_method()

        p12 = self.p1 + self.p2
        out12 = [1, -2, 12]
        p23 = self.p2 + self.p3
        out23 = [1, 7]
        p43 = self.p4 + self.p3
        out43 = [4, 2, 9, 0]
        p42 = self.p4 + self.p2
        out42 = [4, 2, 12, 5]

        assert equal_lists(p12.coeffs, out12)
        assert equal_lists(p23.coeffs, out23)
        assert equal_lists(p43.coeffs, out43)
        assert equal_lists(p42.coeffs, out42)

    def test_mul(self):
        self.setup_method()

        p12 = self.p1 * self.p2
        out12 = [2, -2, -12, 36]
        p23 = self.p2 * self.p3
        out23 = [-2, -4, 6]
        p43 = self.p4 * self.p3
        out43 = [-4, 2, -8, 11, -1]
        p42 = self.p4 * self.p2
        out42 = [8, 28, 32, 58, -6]

        assert equal_lists(p12.coeffs, out12)
        assert equal_lists(p23.coeffs, out23)
        assert equal_lists(p43.coeffs, out43)
        assert equal_lists(p42.coeffs, out42)

    def test_sub(self):
        self.setup_method()

        p12 = self.p1 - self.p2
        out12 = [1, -6, 0]
        p23 = self.p2 - self.p3
        out23 = [3, 5]
        p43 = self.p4 - self.p3
        out43 = [4, 2, 11, -2]
        p42 = self.p4 - self.p2
        out42 = [4, 2, 8, -7]

        assert equal_lists(p12.coeffs, out12)
        assert equal_lists(p23.coeffs, out23)
        assert equal_lists(p43.coeffs, out43)
        assert equal_lists(p42.coeffs, out42)

    def test_eq(self):
        self.setup_method()

        p12 = self.p1 - self.p2
        out12 = [1, -6, 0]
        p23 = self.p2 - self.p3
        out23 = [3, 5]
        p43 = self.p4 - self.p3
        out43 = [4, 2, 11, -2]
        p42 = self.p4 - self.p2
        out42 = [4, 2, 8, -7]

        assert p12 == Polynomial(out12)
        assert p23 == Polynomial(out23)
        assert p43 == Polynomial(out43)
        assert p42 == Polynomial(out42)

    def test_ne(self):
        self.setup_method()

        p12 = self.p1 - self.p2
        out12 = [1, -5, 0]
        p23 = self.p2 - self.p3
        out23 = [3, -5]
        p43 = self.p4 - self.p3
        out43 = [4, 25, 11, -2]
        p42 = self.p4 - self.p2
        out42 = [4, 2, 18, -7]

        assert p12 != Polynomial(out12)
        assert p23 != Polynomial(out23)
        assert p43 != Polynomial(out43)
        assert p42 != Polynomial(out42)


if __name__ == '__main__':
    main()