import re

patterns = ["term1", "term2"]

text = "This is a string with term1, not the other"
split_term = "@"
email = "user@gmail.com"

# for pattern in patterns:
#     print("I'm searching for: " + pattern)
#
#     if re.search(pattern, text):
#         print("MATCH!")
#     else:
#         print("NO MATCH!")

print(re.split(split_term, email))  # email.split("@")
# print(match.start())

print(re.findall("match", "test phrase match in match middle"))


def multi_re_find(patterns, phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print("\n")


# test_phrase = "sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd"
# test_patterns = ["s[sd]+"]

# test_phrase = "This is a string! But it has punctuation. How can we remove it?"
# test_patterns = ["[^!.?]+"]
# test_patterns = ["[A-Z]+"]

test_phrase = "This is a string with numbers 12312 and a symbol #hashtag"
# d - digits
# D - non-digits
# s - whitespace
# S - non-whitespace
# w - alphanumeric characters
# W - non-alphanumeric characters
test_patterns = [r"\W+"]

multi_re_find(test_patterns, test_phrase)
