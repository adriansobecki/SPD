import time


def merge(left, right):
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left].d <= right[index_right].d:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def merge_sort(list):
    if len(list) < 2:
        return list

    midpoint = len(list) // 2

    return merge(
        left = merge_sort(list[:midpoint]),
        right = merge_sort(list[midpoint:]))


def greedy(tasks):
    start = time.time()
    pi = merge_sort(tasks)
    czas = time.time() - start

    return pi, czas