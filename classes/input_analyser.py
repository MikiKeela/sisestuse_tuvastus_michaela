from classes.number_analyzer import NumberAnalyzer
from classes.text_analyzer import TextAnalyzer


class InputAnalyzer:
    def __init__(self):
        self.num = NumberAnalyzer()
        self.txt = TextAnalyzer()

    def _format_yes_no(self, value: bool, extra=None) -> str:
        base = "jah" if value else "ei"
        if extra is None:
            return base
        return f"{base} ({extra})"

    def analyze(self, user_input: str) -> str:
        results = []
        stripped = user_input.strip()

        results.append(f"Sisestus: {repr(user_input)}")
        results.append("-" * 40)

        # Tühi näitab nii numbri kui ka teksti puhul
        empty = self.txt.is_empty(user_input)
        results.append(f"Tühi: {self._format_yes_no(empty)}")

        # Kui on tühi, siis lõpetame siinkohal (muid kontrolle pole mõtet näidata)
        if empty:
            return "\n".join(results)

        results.append("")

        # number või tekst
        number = self.num.is_number(stripped)

        if number is not None:
            results.append("Number:")
            results.append(f"Paarisarv: {self._format_yes_no(self.num.is_even(number))}")
            results.append(f"Positiivne: {self._format_yes_no(self.num.is_positive(number))}")
            results.append(f"Täisarv: {self._format_yes_no(self.num.is_integer(number))}")
            results.append(f"Jagub kolmega: {self._format_yes_no(self.num.divisible_by_three(number))}")
            results.append(f"Ümmargune number: {self._format_yes_no(self.num.is_round_number(number))}")
        else:
            results.append("Tekst:")
            results.append(f"Algab suure tähega: {self._format_yes_no(self.txt.starts_with_uppercase(user_input))}")
            results.append(f"Sisaldab numbrit: {self._format_yes_no(self.txt.contains_digit(user_input))}")

            wc = self.txt.word_count(user_input)
            results.append(f"Mitu sõna: {self._format_yes_no(wc > 1, wc)}")

            results.append(f"Palindroom: {self._format_yes_no(self.txt.is_palindrome(user_input))}")

        return "\n".join(results)
