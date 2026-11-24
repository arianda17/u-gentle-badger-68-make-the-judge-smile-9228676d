ENTRY = "The line was out the door, but the barista saw my kid crying and handed him a warm cookie, his coffee foam shaped like a dinosaur — for free."

assert "\n" not in ENTRY and 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry must be one line of 1-200 non-whitespace chars"

print(ENTRY)