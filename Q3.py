


def remove_duplicate(Input):
    buf_set=set(Input)
    output=[]
    for value in Input:
        if(value in buf_set):
            output.append(value)
            buf_set.remove(value)

    return output

if __name__ == '__main__':
    input=[12,24,35,24,88,120,155,88,120,155]
    print(remove_duplicate(input))
            
