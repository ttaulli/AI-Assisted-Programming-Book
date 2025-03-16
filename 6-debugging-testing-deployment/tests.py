


_ = lambda s: ''.join(chr((ord(c.lower()) - 97 + 13) % 26 + 97) if c.isalpha() else "*" if c.isspace() else c for c in s)
