def processQueueOperations(ops):
    ops=ops.split(',')
    ops=list(ops)
    print(ops)
    Stack=[]
    for x in ops:
        if x != None:
            if x=='deq':
                if Stack:
                    Stack.pop(0)
                
            x=x.split()
            if 'enq' in x:
                x=int(x[1])
                Stack.append(x)  
        else:
            return []
    return Stack
print(processQueueOperations("deq,enq 1,enq -3,enq 5,deq,enq 10"))