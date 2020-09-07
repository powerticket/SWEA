def solution(N, stages):
    rate=[]
    answer = []

    for i in range(1,N+1) :    #스테이지 1~N
        P_stage=0
        W_stage=0
        for j in range(len(stages)) :
            if i==stages[j] :
                P_stage+=1     #현재 스테이지
            if stages[j]>=i :
                W_stage+=1    #현재+통과한 스테이지
        if W_stage == 0 :
            rate.append([i,0])   #한명도 도달하지 못한 스테이지
        else :
            rate.append((i,P_stage/W_stage))
            #[스테이지,실패율]
    rate.sort(key=lambda rate:rate[1],reverse=True)
    for i in rate :
        answer.append(i[0])
    return answer