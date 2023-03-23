def parse_markdown(text):
    is_in_mathbox = False
    result = ""
    i = 0
    while i < len(text):
        if text[i:i+2] == "$$":
            is_in_mathbox = not is_in_mathbox
            result += text[i:i+2]
            i += 2
        elif is_in_mathbox and text[i] == "*":
            result += "\\ast"
            i += 1
        else:
            result += text[i]
            i += 1
    return result

text = "Here's some text with $$f(x^*) = x^*$$ and *italics*."
parsed_text = parse_markdown(text)
print(parsed_text)
