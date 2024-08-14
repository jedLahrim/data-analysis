print("hello".capitalize())  # Output: 'Hello'
print("Hello".casefold())  # Output: 'hello'
print("hello".center(10, '-'))  # Output: '--hello---'
print("hello world".count('o'))  # Output: 2
print("hello".encode())  # Output: b'hello'
print("hello".endswith('o'))  # Output: True
print("hello\tworld".expandtabs(4))  # Output: 'hello   world'
print("hello".find('e'))  # Output: 1
print("Hello, {}".format("world"))  # Output: 'Hello, world'
print("{name} is {age} years old".format_map({'name': 'Alice', 'age': 25}))  # Output: 'Alice is 25 years old'
print("hello".index('e'))  # Output: 1
print("hello123".isalnum())  # Output: True
print("hello".isalpha())  # Output: True
print("hello".isascii())  # Output: True
print("123".isdecimal())  # Output: True
print("123".isdigit())  # Output: True
print("hello".isidentifier())  # Output: True
print("hello".islower())  # Output: True
print("123".isnumeric())  # Output: True
print("hello".isprintable())  # Output: True
print("   ".isspace())  # Output: True
print("Hello World".istitle())  # Output: True
print("HELLO".isupper())  # Output: True
print(",".join(["a", "b", "c"]))  # Output: 'a,b,c'
print("hello".ljust(10, '-'))  # Output: 'hello-----'
print("HELLO".lower())  # Output: 'hello'
print("  hello  ".lstrip())  # Output: 'hello  '
table = str.maketrans("abc", "123")
print("abc".translate(table))  # Output: '123'
print("hello world".partition(' '))  # Output: ('hello', ' ', 'world')
print("hello world".replace("world", "there"))  # Output: 'hello there'
print("hello".rfind('l'))  # Output: 3
print("hello".rindex('l'))  # Output: 3
print("hello".rjust(10, '-'))  # Output: '-----hello'
print("hello world".rpartition(' '))  # Output: ('hello', ' ', 'world')
print("a,b,c".rsplit(','))  # Output: ['a', 'b', 'c']
print("  hello  ".rstrip())  # Output: '  hello'
print("a,b,c".split(','))  # Output: ['a', 'b', 'c']
print("hello\nworld".splitlines())  # Output: ['hello', 'world']
print("hello".startswith('h'))  # Output: True
print("  hello  ".strip())  # Output: 'hello'
print("Hello World".swapcase())  # Output: 'hELLO wORLD'
print("hello world".title())  # Output: 'Hello World'
table = str.maketrans("abc", "123")
print("abc".translate(table))  # Output: '123'
print("hello".upper())  # Output: 'HELLO'
print("42".zfill(5))  # Output: '00042'
# print("HelloWorld".removeprefix("Hello"))  # Output: 'World'
# print('HelloWorld'.removesuffix("World"))  # Output: 'Hello'
