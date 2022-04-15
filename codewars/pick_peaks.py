def pick_peaks(arr):
    """Find all local maxima in the arr.

    An element A[i] is defined as a local maxima if 
        A[i-1] < A[i] and A[i] > A[i+1] where i = 1...n-2. 
        In case of boundary elements, the number has to be 
        just smaller than its adjacent number.

    Args:
        arr: List of integer.

    Returns:
        A dictionary of positions and values 
            of local maximas.
    """
    
    pos = []
    peaks = []
    arr_len = len(arr) - 1 
    for i in range(1, arr_len):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
           pos.append(i)
        elif  (arr[i] > arr[i-1]):
              # check for plateaus.
              j = i + 1
              while(arr[i] == arr[j]) and (j < arr_len): j = j + 1 
              if (arr[i] > arr[j]):    
                pos.append(i)


    return {'pos':pos, 'peaks':[[arr[i] for i in pos]]}
    
if __name__=='__main__':
    print(pick_peaks([0, 1, 2, 5, 1, 0]))
    print(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]))
    print(pick_peaks([1, 2, 2, 2, 1]))
    print(pick_peaks([1, 2, 2, 2, 2]))
    print(pick_peaks([1, 2, 2, 2, 3]))
    print(pick_peaks([1, 2, 2, 2, 1, 2, 2, 2, 2]))
    print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]))
    print(pick_peaks([2,1,3,2,2,2,2,1]))
    print(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]))
