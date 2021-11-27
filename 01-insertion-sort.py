# Given a list [8,5,3,2,9,6,0,1], the program should output [0,1,2,3,5,6,8,9] using insertion sort.
# Time complexity: best case: O(n) --> when array is in sorted order, worst case: O(n^2)
# space complexity: O(1) -- Done in place
def insertion_sort(array):
    for i in range(1,len(array)): # We start with an assumption that the first element is sorted and at the right place
        j =i
        while j > 0 and array[j] < array[j-1]: # 
            swap(j , j-1,array)  # swap number in the two indices
            j-=1
    return array


def swap(i, j, array):
    array[i],array[j] = array[j], array[i]


if __name__ == "__main__":
    array = [8,5,3,2,9,6,0,1]
    print(insertion_sort(array))