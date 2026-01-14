class NumberAnalyzer:
    def parse(self, value: str):
        value = value.strip()
        if value == "":
            return None
        try:
            return float(value)
        except ValueError:
            return None

    def is_integer(self, n: float) -> bool:
        return n.is_integer()

    def is_even(self, n: float) -> bool:
        return n.is_integer() and int(n) % 2 == 0

    def is_positive(self, n: float) -> bool:
        return n > 0

    def divisible_by_three(self, n: float) -> bool:
        return n.is_integer() and int(n) % 3 == 0

    def is_round_number(self, n: float) -> bool:
        return n.is_integer() and abs(int(n)) % 10 in (0, 5)
