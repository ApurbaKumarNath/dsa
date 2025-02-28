def selection_sort_id_mark(id_arr, mark_arr):
    swap_count = 0
    for i in range(len(mark_arr) - 1):
        max_mark_idx = i
        for j in range(i + 1, len(mark_arr)):
            if mark_arr[j] > mark_arr[max_mark_idx]:
                max_mark_idx = j

            if mark_arr[j] == mark_arr[max_mark_idx] and id_arr[j] < id_arr[max_mark_idx]: # condition for same marks but different IDs (lower ID comes first)
                max_mark_idx = j

        if i != max_mark_idx:
            mark_arr[i], mark_arr[max_mark_idx] = mark_arr[max_mark_idx], mark_arr[i]
            id_arr[i], id_arr[max_mark_idx] = id_arr[max_mark_idx], id_arr[i]
            swap_count += 1


    print('Minimum swaps:', swap_count)
    for i in range(len(id_arr)):
        print(f'ID: {id_arr[i]} Mark: {mark_arr[i]}')

N = int(input())
id_arr = input().split()
mark_arr = input().split()
if len(id_arr) == N:
    for i in range(N):
        id_arr[i] = int(id_arr[i])

    for i in range(N):
        mark_arr[i] = int(mark_arr[i])

    selection_sort_id_mark(id_arr, mark_arr)
