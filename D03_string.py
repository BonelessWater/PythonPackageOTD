import string 

print(string.ascii_letters)  # All ASCII letters (lowercase + uppercase)
print(string.ascii_lowercase)  # All lowercase ASCII letters
print(string.ascii_uppercase)  # All uppercase ASCII letters

print(string.digits)  # All decimal digits
print(string.hexdigits)  # All hexadecimal digits (0-9, a-f, A-F)
print(string.octdigits)  # All octal digits (0-7)
print(string.capwords("hello world"))  # Capitalize the first letter of each word in a string
print(string.Formatter().format("Hello, {}!", "world"))  # Format a string with placeholders