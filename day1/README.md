 ## Running python code

 1. By using the interactive mode
 2. By running `python first.py`
 3. Or making the file an executable and running it, for that you should change the file permission
    - powershell : ``icacls `"./first.py`" /grant `"Senal`":`(X`)``
    - then run it like `./test.py`

## Identifiers

- Underscores, letters and numbers only
- Cannot start with a number
- Case sensitive
- Conventions:
    - Class
    - variable
    - _test : private
    - __test : strongly private
    - test__ : language-defined special name

## Reserved words

- There are set of reserved words which cannot be used for identifiers (and, assert, break, exec, etc...)

## Lines ans Indentation

- No braces just indentations

## Multi-line statements

- Use line continuation character to continue the statement on the next line. Because python treats all new lines are as separate statements
- `x = t + \`
- ` u + \`
- ` v`
- Or else contain inside [], {}, ()

## Quatations

- Python accepts ('), (")
- And also tripple (''') or (""")
- Triple quotes are used for multiline strings

## Comments

- Comments are using (#), one line comments

## Using blank lines

- a line with white spaces or only a comment is a blank line and python ignore it

## Waiting for the user

- `raw_input("\n\nPress the enter key to exit")`
- Used to keep the console window open

## Multiple statements on one line

- `import sys; x = 'foo'; sys.stdout.write(x + '\n')`

## Suites

- An indented code block is called a suite
- Complex statements starts with a key word and end with a colon (:)