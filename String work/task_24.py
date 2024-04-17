sentence=input("Sentence is ")
is_literal = False
result=""
for char in sentence:
    if char == '"':
        is_literal = not is_literal
    if not is_literal:
        result+=char
print(result.replace('"',""))