def binary_search(*, lst: list[int], x: int) -> list[int]:
    res = []
    start = 0;
    end = int(len(lst)) - 1
    mid = 0
    n = 0
    while start <= end:
        mid = int((end + start) / 2)
        n += 1
        print("============")
        print(f"lst[mid] is {lst[mid]}\nN is {n}")
        if x == lst[mid]:
            res.append(lst[mid])
            res.append(n)
            return res
        elif x > lst[mid]:
            start = mid + 1
        elif x < lst[mid]:
            end = mid - 1
    return None

def binary_search_recursive(*, lst: list[int], x: int, start: int, end: int, n: int) -> list[int]:
    mid = (end + start) // 2
    if lst[(end + start) // 2] != x and start <= end:
        if x > lst[mid]:
            return binary_search_recursive(lst=lst, x=x, start=(mid) + 1, end=end, n=n+1)
        elif x < lst[mid]:
            return binary_search_recursive(lst=lst, x=x, start=start, end=(mid) - 1, n=n+1)
    elif lst[mid] == x:
        if n == 0:
            n = 1
        res = res=[lst[mid], n]
        return res
    return None

lst = [x for x in range(100)]
finded_lst = binary_search_recursive(lst=lst, x=72, start=0, end=int(len(lst)), n=0)
finded_lst = binary_search(lst=lst, x=72)

print("============")
print (f"The x is {finded_lst[0]}")
print (f"Walk count is {finded_lst[1]}")