
class A:
    def foo(self):
        coeff_calorie_1 = 1
        coeff_calorie_2 = 1

        clr = self.action / self.duration + coeff_calorie_1

        return clr * coeff_calorie_2 * self.weight
