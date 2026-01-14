from classes.text_analyzer import TextAnalyzer
from classes.section_analyzers import NumberSectionAnalyzer, TextSectionAnalyzer


class InputAnalyzer:

    def __init__(self):
        self.txt = TextAnalyzer()

        self.analyzers = [
            NumberSectionAnalyzer(),
            TextSectionAnalyzer(),
        ]

    def _format_yes_no(self, value: bool, extra=None) -> str:
        base = "jah" if value else "ei"
        return base if extra is None else f"{base} ({extra})"

    def analyze(self, user_input: str) -> str:
        lines = []
        lines.append(f"Sisestus: {repr(user_input)}")
        lines.append("-" * 40)

        empty = self.txt.is_empty(user_input)
        lines.append(f"Tühi: {self._format_yes_no(empty)}")

        if empty:
            return "\n".join(lines)

        lines.append("")

        for analyzer in self.analyzers:
            if analyzer.can_handle(user_input):
                lines.extend(analyzer.analyze(user_input, self._format_yes_no))

        return "\n".join(lines)
