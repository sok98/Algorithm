# 스택1 -> push
# 스택2 -> pop

mainStack = [1, 2, 3, 4, 5]
tempStack = []
num = 0

def enqueueIt(num):
	mainStack.append(num)
	print(mainStack)

# pop 할 경우 가장 나중에 들어온 원소부터 tempStack에 추가하여 역순 stack을 만든 후 가장 끝 요소를 pop 후 다시 맨 나중 요소부터 mainStack에 넣음
def dequeIt():
    result = -1
    
    while mainStack:
	    tempStack.append(mainStack.pop())
    tempStack.pop()
    while tempStack:
	    mainStack.append(tempStack.pop())
	

print(mainStack)
enqueueIt(6)
enqueueIt(7)
dequeIt()
print(mainStack)