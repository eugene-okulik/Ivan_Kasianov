text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"

new_text = text.split()
text_result = []

for i in new_text:
    if "." in i or "," in i:
        new_word = i.replace(",", "ing,").replace(".", "ing.")
    else:
        new_word = str(i) + "ing"
    text_result.append(new_word)
print(" ".join(text_result))
