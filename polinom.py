class Polynomial:
    def __init__(self, coeffs):
        if (type(coeffs) == float or
            type(coeffs) == int):
            coeffs = [coeffs]
        elif(type(coeffs) == list):
            pass
        elif(coeffs.__class__.__name__ == "Polynomial"):
            coeffs = coeffs.coeffs
        else:
            raise Exception("Unsupported type {}".format(type(coeffs)))

        assert len(coeffs) != 0, "Empty polynomial"

        self.coeffs = coeffs
        while self.coeffs[0] == 0 and len(self.coeffs) > 1:
            del self.coeffs[0]

    def __add__(self, other):
        other = Polynomial(other)
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

    def __radd__(self, other):
        other = Polynomial(other)
        return self + other

    def __sub__(self, other):
        my_len = len(self)
        other = Polynomial(other)
        other_len = len(other)

        if my_len > other_len:
            coeffs1 = self.coeffs
            coeffs2 = [0] * (my_len - other_len) + other.coeffs
        else:
            coeffs1 = [0] * (other_len - my_len) + self.coeffs
            coeffs2 = other.coeffs

        out_coeffs = [c1 - c2 for c1, c2 in zip(coeffs1, coeffs2)]

        return Polynomial(out_coeffs)

    def __rsub__(self, other):
        other = Polynomial(other)
        return -1 * self + other

    def __mul__(self, other):
        other = Polynomial(other)
        out_coeffs = [0] * (len(self) + len(other))

        for idx1, c1 in enumerate(reversed(self.coeffs)):
            for idx2, c2 in enumerate(reversed(other.coeffs)):
                out_coeffs[idx1 + idx2] += c1 * c2

        out_coeffs = list(reversed(out_coeffs))

        return Polynomial(out_coeffs)

    def __rmul__(self, other):
        other = Polynomial(other)
        return self * other

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
        max_d = len(self.coeffs) - 1
        out = ""
        for i, c in enumerate(self.coeffs[:-2]):
            out += str(self.coeffs[i]) + "x^" + str(max_d - i)
            if self.coeffs[i + 1] > 0:
                out += "+"

        if max_d > 0:
            out += str(self.coeffs[-2]) + "x"
            if self.coeffs[-1] > 0:
                out += "+"

        out += str(self.coeffs[-1])

        return out