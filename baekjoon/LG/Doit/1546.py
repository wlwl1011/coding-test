N = int(input())
score = list(map(int, input().split()))
max_score = max(score)
new_score = [0 for i in range(N)]
for i in range(N):
    new_score[i] = score[i]/max_score*100

print(round(sum(new_score)/N,2))