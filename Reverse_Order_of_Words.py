#Reverse order of words in given sentence

sentence = "Reverse order of words in given sentence"
print(sentence)
new_sentence = ""
start = 0
for i in range(0,len(sentence)):
    if(sentence[i].isspace()):
        new_sentence = sentence[start:i] + " " + new_sentence
        start = i + 1
        
new_sentence = sentence[start:] + " " + new_sentence
        
print(new_sentence)