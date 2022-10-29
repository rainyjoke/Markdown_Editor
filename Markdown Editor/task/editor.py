# write your code here
# stage 5/5

formatters = ["plain", "bold", "italic", "inline-code", "link", "header", "unordered-list"
              ,"ordered-list", "new-line", "!help"]
help = "Available formatters: plain bold italic header unordered-list ordered-list link inline-code new-line\n" \
              "Special commands: !help !done"

def plain(text):
    return text

def bold(text):
    return "**"+text+"**"

def italic(text):
    return "*"+text+"*"

def get_level_for_header():
    level = int(input("Level: "))
    while True:
        if 1 <= level <= 6:
            return level
        else:
            print("The level should be within the range of 1 to 6")
        level = int(input("Level: "))
    

def header():
    level = get_level_for_header()
    text = input("Text: ")
    return "#"*level+" "+text+new_line()

def link():
    label = input("Label: ")
    url = input("URL: ")
    label = "["+label+"]"
    url = "("+url+")"
    return label+url

def inline_code(text):
    return "`"+text+'`'

def new_line():
    return "\n"

def get_list_length():
    n = int(input("Number of rows: "))
    
    while True:
        if n>0:
            return n
        print("The number of rows should be greater than zero")
        n = int(input("Number of rows: "))

def get_list_items(n):
    items = [ input("Row #" + str(i+1) + ": ") for i in range(n)]
    return items

def list(type_list):

    n = get_list_length()
    items = get_list_items(n)
    syntax = ""

    if type_list == "ordered-list":
        for i in range(n):
            syntax += str(i+1) + ". " + items[i] + "\n"

    else:
        for i in range(n):
            syntax += "* " + items[i] + "\n"

    return syntax

def done(syntax):
    file = open("output.md", "w")
    file.write(syntax)
    file.close()

def formatting_text(formatter):

    syntax = ""
    if formatter == "plain":
        text = input("Text: ")
        syntax = plain(text)

    elif formatter == "bold":
        text = input("Text: ")
        # syntax = lambda text: ("**" + text + "**")
        syntax = bold(text)

    elif formatter == "italic":
        text = input("Text: ")
        # syntax = lambda text: ("*" + text + "*")
        syntax = italic(text)

    elif formatter == "inline-code":
        text = input("Text: ")
        syntax = inline_code(text)

    elif formatter == "header":
        syntax = header()

    elif formatter == "new-line":
        syntax = new_line()

    elif formatter == "link":
        syntax = link()

    elif formatter == "ordered-list" or formatter == "unordered-list":
        syntax = list(formatter)

    return syntax



# Main
markdown_syntax = ""   # To store each markdown syntaxes
while True:
    formatter = input("Choose a formatter: ")

    if formatter == "!done":
        done(markdown_syntax)
        break

    elif formatter == "!help":
        print(help)

    elif formatter in formatters:
        markdown_syntax += formatting_text(formatter)

    elif formatter not in formatters:
        print("Unknown formatting type or command")

    print(markdown_syntax)

