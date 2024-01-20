def mergeTwoLists(self, list1, list2):
    mergedList = []
    
    for i in range(len(list1)):
        mergedList.append(list1[i])
        mergedList.append(list2[i])

    mergedList.sort()

    return mergedList

print(mergeTwoLists("self", [1,2,4], [1,3,4]))
