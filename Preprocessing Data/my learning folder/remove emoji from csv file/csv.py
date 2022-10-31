import re
import emoji

def strip_emoji(text):
    print(emoji.emoji_count(text))
    new_text = re.sub(emoji.get_emoji_regexp(), r"", text)
    return new_text
    
with open("infile.txt", "r") as infile:
    old_text = None
    old_text = infile.read()
no_emoji = None
no_emoji = strip_emoji(old_text)

with open("outfile.txt", "w") as outfile:
    outfile.write(no_emoji)