def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes


def train_insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j][0] <= arr[j - 1][0]:

            if arr[j][0] < arr[j - 1][0] or time_to_minutes(arr[j][-1]) > time_to_minutes(arr[j - 1][-1]):
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

    for i in arr:
        print(' '.join(i))


N = int(input())
train_info = []
for i in range(N):
    train_info.append(input().split())

train_insertion_sort(train_info)