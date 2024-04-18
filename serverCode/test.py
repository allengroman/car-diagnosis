from chatbot import *

answer = getParts("bumpy drive", "Acura TSX 2007", "Suspension issues")
l = partsList(answer)

for i in l:
    print(i)