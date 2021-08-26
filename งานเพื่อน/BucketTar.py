def bucketSort(array: list):
    # Create empty buckets
    bucket = [[] for i in range(len(array))]
    maxVal, minVal = array[0], array[0]
    for m in range(len(array)):
        if array[m] < minVal:
            minVal = array[m]
        if array[m] > maxVal:
            maxVal = array[m]

    rangeVar = (maxVal-minVal)/len(array)

    # Insert elements into their respective buckets
    for ele in array:
        for j in range(len(array)):
            upper = minVal + ((j-1)*rangeVar)
            lower = minVal + ((j*rangeVar))
            if ele > minVal + ((len(array)-1)*rangeVar):
                bucket[len(array)-1].append(ele)
                break
            elif upper <= ele < lower:
                bucket[j].append(ele)
                break

    # Sort the elements of each bucket
    bucket = [j for i in bucket for j in sorted(i)]
    return bucket


array = [0, 3, 5, 1, 2, 19, 14, 10, 14]
print("Sorted Array in descending order is")
print(bucketSort(array))

talk = False
if not(talk):
    print('---------')
else:
    talk = True