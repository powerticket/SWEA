T = int(input())
for t in range(1, T + 1):    
    N = int(input())
    print(f'#{t} ', end = '')    
    count = 0
    L = list(map(str,input().split()))
    for word in L:
        alllower = 0
        check_end = 0
        if(word[0].isupper() == True):            
            for j in word:
                if(j == '.' or j == '?' or j == '!'):
                    check_end += 1                
                elif(j.isupper() or not j.isalpha()):                
                    alllower += 1                
            if(alllower == 1):
                count += 1
            if(check_end == 1):
                print(count, end = ' ')
                check_end = 0
                count = 0
    print()