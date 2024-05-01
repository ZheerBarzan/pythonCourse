def square(number):
    return number**2


def greet(first_name, last_name):
    print(f'Hello, {first_name} {last_name}!')


# positional arguments
greet("zheer", "Barzan")

# keyword arguments
greet(last_name="Barzan", first_name="Zheer")

print(square(5))
def emoji_converter(message):
    words = message.split(" ")
    emojis ={
        ":)": "😊",
        ":(": "😢"
    }
    output =""

    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input(">")

print(emoji_converter(message))


