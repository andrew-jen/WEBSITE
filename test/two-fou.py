def processStackOperations(ops):
    ops=ops.split(',')
    ops=list(ops)
    print(ops)
    Stack=[]
    for x in ops:
        if x != None:
            if x=='pop':
                if Stack:
                    Stack.pop()
                
            x=x.split()
            if 'push' in x:
                x=int(x[1])
                Stack.append(x)  
        else:
            return []
    return Stack
print(processStackOperations("push 3,push -2,pop,pop,pop"))