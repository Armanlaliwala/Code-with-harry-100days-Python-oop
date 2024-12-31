import  re

pattern = r"[A-Z]+yclones"
text = "Cyclones are powerful storms characterized by strong winds and heavy rainfall. A Dyclones can cause significant damage to infrastructure and pose serious threats to life. Understanding the formation and behavior of Jyclones is crucial for disaster preparedness and response. Effective Hyclones management strategies can mitigate the adverse impacts of these natural disasters."

match= re.finditer(pattern, text) #this will give all occurance of the word starting with capital (A-Z)+yclones
for match in match:
    print(match)
    print(match.span())#this will give all occurance of the word starting with capital (A-Z)+yclones it will give the span(index number)
    print(text[match.span()[0]:match.span()[1]]) #we can do slicing in the and get the word