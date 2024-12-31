import  re

pattern = "was"
text = "i was in the school after i was in the clg after i was in the office after i was in the haome "
match= re.search(pattern, text) #this will give you first occrunce
print(match)