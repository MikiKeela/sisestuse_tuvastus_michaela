class NumberAnalyzer:

    def is_number(self, value: str):
        try:
            return float(value)
        except ValueError:
            return None

    def is_even(self, number: float) -> bool:
        return number.is_integer() and int(number) % 2 == 0

    def is_positive(self, number: float) -> bool:
        return number > 0

    def is_integer(self, number: float) -> bool:
        return number.is_integer()

    def divisible_by_three(self, number: float) -> bool:
        return number.is_integer() and int(number) % 3 == 0

    def is_round_number(self, number: float) -> bool:
        return number.is_integer() and abs(int(number)) % 10 in (0, 5)
