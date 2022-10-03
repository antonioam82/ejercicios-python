#EXAMPLE OF DATA SORTING USING INSERTION SORT ALGORITHM.

def insertion_sort(data):
    l = len(data)
    if l > 1:
        for i in range(1,l):
            for j in range(i, 0, -1):
                if data[j] < data[j-1]:
                    data[j], data[j-1] = data[j-1], data[j]
                    print(data)
                else:
                    print(data)
                    break
        return data
    else:
        return data

data = [56,234,123,6,23,1231,1]
i_sort = insertion_sort(data)
print("DATA SORTED: {}".format(i_sort))
