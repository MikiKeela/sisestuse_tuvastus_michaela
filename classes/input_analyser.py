from classes.number_analyzer import NumberAnalyzer
from classes.text_analyzer import TextAnalyzer


class InputAnalyzer:

    def __init__(self):
        self.num = NumberAnalyzer()
        self.txt = TextAnalyzer()

    def _yes_no(self, value: bool) -> str:
        return "jah" if value else "ei"

    def analyze(self, user_input: str) -> str:
        results = []
        results.append(f"Sisestus: {repr(user_input)}")
        results.append("-" * 40)

        number = self.num.is_number(user_input.strip())

        results.append("NUMBRID:")
        if number is None:
            results.append("Paarisarv: ei")
            results.append("Positiivne: ei")
            results.append("Täisarv: ei")
            results.append("Jagub kolmega: ei")
            results.append("Ümmargune number: ei")
        else:
            results.append(f"Paarisarv: {self._yes_no(self.num.is_even(number))}")
            results.append(f"Positiivne: {self._yes_no(self.num.is_positive(number))}")
            results.append(f"Täisarv: {self._yes_no(self.num.is_integer(number))}")
            results.append(f"Jagub kolmega: {self._yes_no(self.num.divisible_by_three(number))}")
            results.append(f"Ümmargune number: {self._yes_no(self.num.is_round_number(number))}")

        results.append("")
        results.append("TEKST:")

        results.append(f"Tühi: {self._yes_no(self.txt.is_empty(user_input))}")
        results.append(f"Algab suure tähega: {self._yes_no(self.txt.starts_with_uppercase(user_input))}")
        results.append(f"Sisaldab numbrit: {self._yes_no(self.txt.contains_digit(user_input))}")
        results.append(f"Mitu sõna: {self._yes_no(self.txt.has_multiple_words(user_input))}")
        results.append(f"Palindroom: {self._yes_no(self.txt.is_palindrome(user_input))}")

        return "\n".join(results)
