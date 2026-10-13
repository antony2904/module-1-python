#Write a Python program that checks whether a given string is a palindrome  or not.
def is_palindrome(text: str) -> bool:

  cleaned = "".join(char.lower() for char in text if char.isalnum())


  return cleaned == cleaned[::-1]


test_strings = [
    "radar",
    "A man running in footpath ",
    "race a car",
    "Malayalam",
]

for s in test_strings:
  result = "is" if is_palindrome(s) else "is NOT"
  print(f'"{s}" -> {result} a palindrome.')