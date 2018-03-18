class Polynomial:
    def __init__(self, coeffs):
        assert len(coeffs) != 0, "Empty polynomial"

        self.coeffs = coeffs
        while self.coeffs[0] == 0 and len(self.coeffs) > 1:
            del self.coeffs[0]

    def __add__(self, other):
        my_len = len(self)
        other_len = len(other)

        if my_len > other_len:
            coeffs1 = self.coeffs
            coeffs2 = [0] * (my_len - other_len) + other.coeffs
        else:
            coeffs1 = [0] * (other_len - my_len) + self.coeffs
            coeffs2 = other.coeffs

        out_coeffs = [c1 + c2 for c1, c2 in zip(coeffs1, coeffs2)]

        return Polynomial(out_coeffs)

    def __sub__(self, other):
        my_len = len(self)
        other_len = len(other)

        if my_len > other_len:
            coeffs1 = self.coeffs
            coeffs2 = [0] * (my_len - other_len) + other.coeffs
        else:
            coeffs1 = [0] * (other_len - my_len) + self.coeffs
            coeffs2 = other.coeffs

        out_coeffs = [c1 - c2 for c1, c2 in zip(coeffs1, coeffs2)]

        return Polynomial(out_coeffs)

    def __mul__(self, other):
        out_coeffs = [0] * (len(self) + len(other))

        for idx1, c1 in enumerate(reversed(self.coeffs)):
            for idx2, c2 in enumerate(reversed(other.coeffs)):
                out_coeffs[idx1 + idx2] += c1 * c2

        out_coeffs = list(reversed(out_coeffs))

        return Polynomial(out_coeffs)

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        equal = [c1 == c2 for c1, c2 in zip(self.coeffs, other.coeffs)]

        return all(equal)

    def __ne__(self, other):
        return not(self == other)

    def __len__(self):
        return len(self.coeffs)

    def __str__(self):
        return str(self.coeffs)
