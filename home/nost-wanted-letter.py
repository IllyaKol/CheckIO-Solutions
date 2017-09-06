import re
def checkio(text):
    text = text.replace(' ', '').lower()
    text = re.sub(r'!|,|\.|-|\d', '', text)


    new_text = set(text)
    if len(new_text) != len(text):
        count = 0
        letter = []
        for i in text:
            if text.count(i) > count:
                letter = []
                count = text.count(i)
                letter.append(i)
            elif text.count(i) == count:
                count = text.count(i)
                letter.append(i)
        letter.sort()
        return letter[0]
    else:
        text = list(text)
        text.sort()
        return text[0]