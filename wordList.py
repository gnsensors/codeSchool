from itertools import permutations


f = open('/usr/share/dict/words', 'r')

tmp = f.readlines()

fullWordList=[]
for i in tmp:
  i.replace('\n', '')
  fullWordList.append(i.replace('\n', ''))

print(len(fullWordList))
  
letterList = ['e', 'i', 'u', 'g', 'n', 'n', 'p']

tmpComboList = list(permutations(letterList,  5))

comboList = []

for w in tmpComboList:
  x = ''
  comboList.append(x.join(w))

#print(comboList)

words = []
for x in comboList:
  if (x in fullWordList):
    words.append(x)
    
mylist = list(dict.fromkeys(words))
print(mylist)

# print("there are " + str(len(words))+ " combinations of letters")
# print(words)

# counter = 0
# while counter<len(words):
#   print(words[counter])
#   counter=counter+1
