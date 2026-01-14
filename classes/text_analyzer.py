class TextAnalyzer:

    def is_empty(self, text: str) -> bool:
        return text.strip() == ""

    def starts_with_uppercase(self, text: str) -> bool:
        return bool(text) and text[0].isalpha() and text[0].isupper()

    def contains_digit(self, text: str) -> bool:
        return any(char.isdigit() for char in text)

    def has_multiple_words(self, text: str) -> bool:
        return len(text.strip().split()) > 1

    def is_palindrome(self, text: str) -> bool:
        normalized = "".join(c.lower() for c in text if c.isalnum())
        return normalized != "" and normalized == normalized[::-1]
