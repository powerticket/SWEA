import sys
sys.stdin = open('sample_input.txt', 'r')  #파일로 인풋받기

def dfs(s, g):   # n : 현재 정점
    result = 0
    stack = [0] * V    # 스택
    visited = [0] * (V+1)   # 방문배열
    top = -1

    top += 1
    stack[top] = s  # 시작정점을 스택에 넣기
    visited[s] = 1  # 시작정점을 방문했다고 표시

    # 순회
    while (top >= 0):   # 스택이 비어있지 않는 동안 반복
        s = stack[top]   # 스택에서 하나 꺼내오기
        top -= 1
        for i in range(1, V+1):
            # n에 인접하고 아직 방문하지 않은 정점 i라면
            if adj[s][i] == 1 and visited[i] == 0:
                if i == g:
                    result = 1
                    break
                top += 1
                stack[top] = i
                visited[i] = 1  # 방문여부 체크
    return result

T=int(input())
for t in range(1,T+1):
    V,E = map(int,input().split())
    #간선정보
    edges = [list(map(int, input().split())) for _ in range(E)]
    S,G = map(int,input().split())
    # 인접행렬을 생성
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    # for row in adj:  # 확인
    #     print(row)
    visited = [0]*(V+1)
    for i in range(E):
        s, e = edges[i][0], edges[i][1]
        adj[s][e] = 1
        # adj[G][S] = 1  #무방향 그래프

    grph = dfs(S,G)
    print("#{} {}".format(t,grph))