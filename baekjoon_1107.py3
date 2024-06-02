N = int(input())

M = int(input())

removed_button = [1 for _ in range(10)]
if M != 0:
    removed = list(map(int, input().split(' ')))
    for i in range(M):
        removed_button[removed[i]] = 0
def is_possible(channel):
    # 786 -> '786'
    channel = str(channel)
    for c in channel:
        if removed_button[int(c)] == 0:
            return False
    return True
    # '7' -> 7
    # '8' -> 8
    # '6' -> 6
answer = abs(N - 100)
for channel in range(0, 1000000):
    if is_possible(channel):
        # 786 -> '786' -> 3
        num = len(str(channel))
        num += abs(N - channel)
        answer = min(answer, num)
print(answer)