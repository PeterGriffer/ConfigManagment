class Parser:
    def parse(self, input_string):
        parts = []
        current = []
        in_quotes = False
        quote_char = None

        for char in input_string.strip():
            if char in ["\'", "\""]:
                if not in_quotes:
                    in_quotes = True
                    quote_char = char
                elif char == quote_char:
                    in_quotes = False
                    quote_char = None
                else:
                    current.append(char)
            elif char == ' ' and not in_quotes:
                if current:
                    parts.append(''.join(current))
                    current = []
            else:
                current.append(char)

        if current:
            parts.append(''.join(current))

        if not parts:
            return None, []
        return parts[0], parts[1:]