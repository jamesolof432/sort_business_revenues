
values = [3621945, 1847260, 4992718, 2134568, 3308271, 942372, 4783901, 1367284, 2901047, 4991245,
3748230, 2386789, 4826301, 1756890, 2561947, 4129035, 1315628, 4824907, 4998721, 3875620,
4605721, 1823465, 3258792, 4571423, 2743890, 4012257, 2845960, 4998570, 3991785, 1345678]

original = values.copy()

result = values.copy()

total = sum(values)

threshold = 0

def sortingAll():
    global values
    global result
    global total
    global threshold
    while threshold <= (.6 * total):
        max_index = values.index(max(values))
        threshold += values[max_index]
        for i in range(len(result)):
            if result[i] == values[max_index]:
                result[i] = "60%"
                break
        values.pop(max_index)
    while threshold <= (.8 * total):
        max_index = values.index(max(values))
        threshold += values[max_index]
        for i in range(len(result)):
            if result[i] == values[max_index]:
                result[i] = "20%"
                break
        values.pop(max_index)
    while threshold < (total):
        max_index = values.index(max(values))
        threshold += values[max_index]
        for i in range(len(result)):
            if result[i] == values[max_index]:
                result[i] = "0%"
                break
        values.pop(max_index)
    return

def topSixty():
    global values
    global result
    global total
    global threshold
    while threshold <= (.6 * total):
        max_index = values.index(max(values))
        threshold += values[max_index]
        for i in range(len(result)):
            if result[i] == values[max_index]:
                result[i] = "60%"
                break
        values.pop(max_index)
    return 

def middle():
    global values
    global result
    global total
    global threshold
    while threshold <= (.8 * total):
        max_index = values.index(max(values))
        threshold += values[max_index]
        for i in range(len(result)):
            if result[i] == values[max_index]:
                result[i] = "20%"
                break
        values.pop(max_index)
    return

def bottomTwenty():
    global values
    global result
    global total
    global threshold
    while threshold < (total):
        max_index = values.index(max(values))
        threshold += values[max_index]
        for i in range(len(result)):
            if result[i] == values[max_index]:
                result[i] = "0%"
                break
        values.pop(max_index)
    return result


    return




def main():
    
    global values
    global result
    global original

    sortingAll()
    
    i=0
    
    while i < len(original):
        print(f"{original[i]} --> {result[i]}")
        i = i+1


if __name__ == "__main__":
    main()      