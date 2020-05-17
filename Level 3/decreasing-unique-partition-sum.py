def print_partition(arr):
    brr = [a for a in arr if a is not 0]
    print brr,sum(brr)

def adjust(arr,i):
    k = i+1
    while k < len(arr):
        arr[k] = 0
        k = k+1

# function to check if valid partition
def isValid(arr):
    brr = [a for a in arr if a is not 0]
    for a in brr:
        if brr.count(a) != 1:
            return False
    return True

def solution(n):
    # Your code here
    partition = [0]*n
    i =0
    partition[i] = n
    count = 0    
    # generate all partitions of n
    while True:        
        slack_val = 0
        # loop till first non-1 element found
        while i>=0 and partition[i] == 1:
            slack_val += 1
            i -= 1
        # all 1s in partition, terminate
        if i < 0:
            break
        # first non-1 element found
        partition[i] -= 1
        slack_val += 1
        # enforce decreasing order of partition since next step cannot be higher than previous
        while slack_val > partition[i]:
            partition[i+1] = partition[i]
            slack_val -= partition[i]
            i += 1
        # add new step
        partition[i+1] = slack_val
        i += 1
        # zero out remaining elements
        adjust(partition,i)
        if isValid(partition):
            count = count + 1
    return count
print solution(6)