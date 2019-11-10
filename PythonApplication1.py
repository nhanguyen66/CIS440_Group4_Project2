import cgi, cgitb
from spellchecker import SpellChecker

form = cgi.FieldStorage()

message = form.getvalue('message')

message = "schol asignment due evry snday"

split_message = message.split()

spell = SpellChecker()

new_message = spell.unknown(split_message)

for word in new_message:
  print(spell.correction(word))
