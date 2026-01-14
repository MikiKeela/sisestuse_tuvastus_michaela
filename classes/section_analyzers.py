from classes.number_analyzer import NumberAnalyzer
from classes.text_analyzer import TextAnalyzer


class NumberSectionAnalyzer:

    def __init__(self):
        self.num = NumberAnalyzer()

        self.rules = [
            ("Paarisarv", self.num.is_even),
            ("Positiivne", self.num.is_positive),
            ("Täisarv", self.num.is_integer),
            ("Jagub kolmega", self.num.divisible_by_three),
            ("Ümmargune number", self.num.is_round_number),
        ]

    def can_handle(self, user_input: str) -> bool:
        return self.num.parse(user_input) is not None

    def analyze(self, user_input: str, format_yes_no) -> list[str]:
        number = self.num.parse(user_input)
        lines = ["NUMBRID:"]
        for label, func in self.rules:
            ok = bool(func(number))
            lines.append(f"{label}: {format_yes_no(ok)}")
        return lines


class TextSectionAnalyzer:

    def __init__(self):
        self.num = NumberAnalyzer()
        self.txt = TextAnalyzer()

    def can_handle(self, user_input: str) -> bool:
        return self.num.parse(user_input) is None

    def analyze(self, user_input: str, format_yes_no) -> list[str]:
        wc = self.txt.word_count(user_input)

        lines = ["TEKST:"]
        lines.append(f"Algab suure tähega: {format_yes_no(self.txt.starts_with_uppercase(user_input))}")
        lines.append(f"Sisaldab numbrit: {format_yes_no(self.txt.contains_digit(user_input))}")
        lines.append(f"Mitu sõna: {format_yes_no(wc > 1, wc)}")
        lines.append(f"Palindroom: {format_yes_no(self.txt.is_palindrome(user_input))}")
        return lines
