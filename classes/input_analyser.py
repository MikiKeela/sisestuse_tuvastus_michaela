class InputAnalyzer:
    def analyze(self, user_input: str) -> str:
        results = []
#kontroll analüüs
        # näita mida sisestati
        results.append(f"Sisestati: {repr(user_input)}")
        results.append("-" * 40)

        stripped = user_input.strip()

        #numbri analüüs
        results.append("Numbri kontroll:")
        number = self._get_number(stripped)

        if number is None:
            results.append("Paaris või paaritu: ei ole number")
            results.append("Positiivne või negatiivne: ei ole number")
            results.append("Täisarv või murdarv: ei ole number")
            results.append("Jagub kolmega või ei jagu: ei ole number")
            results.append("Ümmargune number või mitte: ei ole number")
        else:
            if number.is_integer():
                results.append("Täisarv või murdarv: täisarv")
                int_number = int(number)

                if int_number % 2 == 0:
                    results.append("Paaris või paaritu: paaris")
                else:
                    results.append("Paaris või paaritu: paaritu")
                if int_number % 3 == 0:
                    results.append("Jagub kolmega või ei jagu: jagub kolmega")
                else:
                    results.append("Jagub kolmega või ei jagu: ei jagu kolmega")
                if abs(int_number) % 10 in (0, 5):
                    results.append("Ümmargune number või mitte: ümmargune")
                else:
                    results.append("Ümmargune number või mitte: ei ole ümmargune")
            else:
                results.append("Täisarv või murdarv: murdarv")
                results.append("Paaris või paaritu: ei ole paaris")
                results.append("Jagub kolmega või ei jagu: ei jagu kolmega")
                results.append("Ümmargune number või mitte: ei ole ümmargune")
            if number > 0:
                results.append("Positiivne või negatiivne: positiivne")
            elif number < 0:
                results.append("Positiivne või negatiivne: negatiivne")
            else:
                results.append("Positiivne või negatiivne: null")


        #Teksti analüüs
        results.append("")
        results.append("Teksti kontroll:")

        if stripped == "":
            results.append("Tühi või mitte: tühi")
        else:
            results.append("Tühi või mitte: ei ole tühi")

        if user_input and user_input[0].isalpha() and user_input[0].isupper():
            results.append("Algab suure tähega või mitte: algab suure tähega")
        else:
            results.append("Algab suure tähega või mitte: ei alga suure tähega")

        if any(char.isdigit() for char in user_input):
            results.append("Sisaldab numbrit või mitte: sisaldab numbrit")
        else:
            results.append("Sisaldab numbrit või mitte: ei sisalda numbrit")

        words = stripped.split()
        if len(words) == 0:
            results.append("Üks või mitu sõna: 0 sõna")
        elif len(words) == 1:
            results.append("Üks või mitu sõna: üks sõna")
        else:
            results.append(f"Üks või mitu sõna: mitu sõna ({len(words)})")

        normalized = "".join(char.lower() for char in user_input if char.isalnum())
        if normalized and normalized == normalized[::-1]:
            results.append("Palindroom või mitte: palindroom")
        else:
            results.append("Palindroom või mitte: ei ole palindroom")

        return "\n".join(results)

    def _get_number(self, value: str):
        try:
            return float(value)
        except ValueError:
            return None

