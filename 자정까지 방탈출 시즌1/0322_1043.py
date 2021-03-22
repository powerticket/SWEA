import sys
sys.stdin = open('0322_1043.txt', 'r')

# 03/22
# 1043 거짓말

N, M = map(int, input().split())
know_truth = list(map(int, input().split()))
party = [list(map(int, input().split())) for _ in range(M)]
truth = [0] * (N+1)
fake_party = [1] * M
for man in know_truth[1:]:
    truth[man] = 1
# 진실을 아는 사람이 없으면 모든 파티의 수를 출력
if not know_truth[0]:
    print(M)
else:
    i = 0
    while i < M:
        # 해당 파티가 거짓 파티이면
        if fake_party[i]:
            # 해당 인원 중 진실을 아는 인원이 있는지 검사
            for man in party[i][1:]:
                # 있을 경우 해당 파티의 모든 인원이 진실을 알게 됨
                if truth[man]:
                    for man in party[i][1:]:
                        truth[man] = 1
                    # 해당 파티는 진실 파티가 됨
                    fake_party[i] = 0
                    # 처음부터 다시 확인
                    i = 0
                    break
            else:
                i += 1
            continue
        i += 1
    print(sum(fake_party))
