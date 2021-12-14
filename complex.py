class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def __str__(self):
        return '(%s, %si)' % (self.real, self.img)

    def __add__(self,oth):
        re = self.real
        im = self.img
        re_add = oth.real
        im_add = oth.img
        return Complex((re_add + re), (im + im_add))

    def __sub__(self,oth):
        re = self.real
        img = self.img
        re_sub = oth.real
        im_sub = oth.img
        return Complex((re - re_sub), (img - im_sub))

    def __mul__(self,oth):
        re = self.real
        img = self.img
        re_mul = oth.real
        im_mul = oth.img
        return Complex((re * re_mul - img * im_mul), (img * re_mul + re * im_mul))


class Calculator:

    def __init__(self, num1 = None, num2 = None, operation = None):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation

    def __call__(self):
        if self.operation == '+':
            return self.num1 + self.num2
        elif self.operation == '-':
            return self.num1 - self.num2
        elif self.operation == '*':
            return self.num1 * self.num2


    def partition(self, operation):
        factors = operation.split(' ')
        factor_1 = self.parser(factors[0])
        factor_2 = self.parser(factors[2])
        factors = factors[1]
        return Calculator(factor_1, factor_2, factors)

    @staticmethod
    def parser(number):
        if '+' in number:
            sign_formula = number.split('+')
            complex_numb = Complex(float(sign_formula[0]), float(sign_formula[1][:-1]))
        elif '*' in number:
            sign_formula = number.split('*')
            complex_numb = Complex(float(sign_formula[0]), float(sign_formula[1][:-1]))
        elif '-' in number:
            tmp = False
            if number[0] == '-':
                tmp = True
            sign_formula = number.split('-')
            if not tmp:
                num = float(sign_formula[0])
            else:
                num = (-float(sign_formula[0]))
            complex_numb = Complex(num, -float(sign_formula[1][:-1]))

        return complex_numb

def zad_1_complex():
    y = Complex(5,1)
    z = Complex(4,2)
    x = y+z
    print(f" =:{x}")

def zad_2_calculator():
    print("Insert A+Bi + C+Di ")
    input_data = input()
    calc = Calculator().partition(input_data)
    print(f"Result {calc()}")


if __name__ == "__main__":
    #zad_1_complex()
    zad_2_calculator()

