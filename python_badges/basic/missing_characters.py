import string
import re

s = "7985interdisciplinary12"

numbers = [i for i in range(0,10)]
letters = string.ascii_lowercase

found_letters = re.findall(r"[a-z]", s)
found_numbers = list(map(int, re.findall(r"[0-9]", s)))

remaining_letters = list(set(letters) - set(found_letters))
remaining_numbers = list(set(numbers) - set(found_numbers))

sorted_letters = ''.join(sorted(remaining_letters))
sorted_numbers = ''.join(str(n) for n in (sorted(remaining_numbers)))

final_str = sorted_numbers + sorted_letters
