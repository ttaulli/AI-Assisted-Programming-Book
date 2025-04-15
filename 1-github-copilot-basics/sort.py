def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    sorted_numbers = bubble_sort(numbers)
    print("Sorted numbers:", sorted_numbers)