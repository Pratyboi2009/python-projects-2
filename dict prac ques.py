"""
Rain falls down on the town. 
The rain falls fast, and the rain falls hard. 
Cold rain, grey rain, constant rain. 
People watch the rain, feeling the rain, smelling the rain. 
When the rain stops, the town misses the rain. 
The rain is life, and the rain is everything.

"""
#wap Given a string, create a dictionary showing the frequency of each word.
str = "Rain falls down on the town. The rain falls fast, and the rain falls hard. Cold rain, grey rain, constant rain. People watch the rain, feeling the rain, smelling the rain. When the rain stops, the town misses the rain. The rain is life, and the rain is everything."
c = str.lower()

def delpunc(x):        #or we can remove punctuation manually
    for i in ".,":
                x = x.replace(i,"")
    return x
case = delpunc(c)
words = case.split()
freq = {}

for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word] = 1

print(freq)