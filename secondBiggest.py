def find_second_largest(arr, arr_size):
    arr.sort()
    second_largest_elem = 0
    for i in range(arr_size-2, -1, -1):
        if arr[i] != arr[arr_size-1]:
            second_largest_elem = arr[i]
            break
    return second_largest_elem

if __name__ == '__main__':
    a = [12, 35, 1, 10, 34, 1]
    n = len(a)
    answer = find_second_largest(a, n)
    print("The second largest element in the array is: ", answer)
