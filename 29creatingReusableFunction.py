# xxx




def emoji_converter(message):
  words = message.split(" ")
  emojis = {
    ":)": "😀",
    ":(": "😞"
  }
  output = ""
  for word in words:
    output = output + emojis.get(word, word) + " "
  
  return output


message = input(">")
result = emoji_converter(message)
print(result)


# NOTE: DI KO PA NAILALAGAY SA ANKI ITONG FILE NA ITO