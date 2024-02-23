test_case = int(input())
for _ in range(test_case):
    n = list(map(int, input().split()))
    array = list(map(int,input().split()))
    array.sort()
    if n[1]> len(array)//2:
        diff = abs( sum(array[len(array)-n[1]: ]) - sum(array[0 : len(array) - n[1] ]))
    else:
        diff = abs(sum( array[n[1] : ]) - sum( array [0 : n[1]]))
    print(diff)    