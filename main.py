from googletrans import Translator
translator = Translator()
output = translator.translate("Szia",dest="en")
print(output.text)