import time

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

# Test arrays
arrays = {
    5:   list(range(1, 6)),
    10:  list(range(1, 11)),
    50:  list(range(1, 51)),
    100: list(range(1, 101))
}

print("— Insertion Sort —")
for n, arr in arrays.items():
    start_ns = time.perf_counter_ns()
    insertion_sort(arr)
    elapsed_ms = (time.perf_counter_ns() - start_ns) / 1e6
    print(f"For N = {n:<3} → Time = {elapsed_ms:.3f} ms")
