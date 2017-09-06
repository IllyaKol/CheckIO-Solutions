def left_join(phrases):
    new_string = ""
    for i in phrases:
        new_string += i + ','
    new_string = new_string.replace("right", "left")
    new_string = new_string[:-1]
    print(new_string)
    return new_string
    
left_join(("left", "right", "left", "stop"))

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
#     assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
#     assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
#     assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"