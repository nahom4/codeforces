m,n = map(int,input().split())

matrix = []
for _ in range(m):
    row = list(map(int,input().split()))
    row.append(0) # just to avoid index out of range error
    matrix.append(row)

for i in range(m):
    for j in range(n):
        matrix[i][j] = -1 if matrix[i][j] == 0 else 1 # modifying our matrix changing 0 to -1 

for row in matrix:
    #let's do prefix sum on each of the rows
    for i in range(1,n):
        row[i] += row[i - 1]

maxSize = 0
for leftColumn in range(n): # fix the left column
    for rightColumn in range(leftColumn,n): #for each left column fix right column
        block = [] #compressed one dimensional array

        '''
        1 1 1 1
        0 1 1 0
        0 0 0 0

        for the above test case if we fixed leftColumn at 1 and rightColumn 2  zero indexed
        
        we create a sub rectangle as follows 

            1 1
            1 1
            0 0

        when we compress the above sub rectangle

        we get 

             2
             2
             0
            
        A one dimensional array 

        block = [2,2,0] for this case
        '''

        for row in range(m):
            currVal = matrix[row][rightColumn] - matrix[row][leftColumn - 1] #The total sum of the elements between the right and the left column
            block.append(currVal)

        #lets check the block if it contains max size sub rectangle
        width = rightColumn - leftColumn + 1
        maxSize = max(maxSize,maxSizeGoodSubArray(block, width))


print(maxSize)


'''
    similar with sub array sum equals k problem but we need to keep track of the index of the 
    the prefixes as we add them to the dictionary to help us calculate the height of the block
'''
def maxSizeGoodSubArray(block,width):

    currMax = 0
    runningSum = 0
    prefixSumDict = dict()
    prefixSumDict[0] = -1

    for row in range(len(block)):
        runningSum += block[row]

        # if we have registered a prefix as big as the running sum we can remove the prefix
        # to bring our running sum down to zero which we are after
        if runningSum in prefixSumDict: 
            height = row - prefixSumDict[runningSum] 
            currMax = max(currMax,height * width)
        else:
            prefixSumDict[runningSum] = row
     
    return currMax
    





