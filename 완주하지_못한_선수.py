def solution(participant, completion):
    #문제의 포인트 : 완주하지못한 사람 "단 한명", 동명이인의 가능성 
        
    participant.sort() # 참가자 정렬
    completion.sort() # 완주자 정렬
    # 이렇게 배열하면 참가자가 완주한 경우 participant의 인덱스와 completion인덱스가 같은 value를 가진다.
    
    for index in range(len(completion)): # 완주자 배열의 길이만큼 반복하면서 index 생성
        if completion[index] != participant[index]:  
            # completion[index]가 participant[index]와 일치하지 않거나,
            # 앞의 동명이인은 일치하여 넘어가도, 뒤에 있는 동명이인의 사람은 동일인덱스번호의 참가자,완주자가 일치하지 않음
            # 그러므로 participant[index]를 리턴한다
            return participant[index] 
        
    # 위의 if는 completion의 크기만큼 반복하기 때문에 participant의 마지막값이 완주하지 못한 사람을 거를 수가 없다.
    # 이 문제는 완주하지 못한 사람이 "한 명" 반드시 존재하기 때문에, 위의 if문에서 걸러지지 않은 사람이 완주하지 못한 사람이다.
    # 동명이인이면서 완주를 하지 못했으나 이름상 제일 뒤에 있는 사람인 경우도 체크하여야 한다.
    # ex) 정렬된 후 배열이 participant['a', 'b', 'b', 'z', 'z'] / completion['a', 'b', 'b', 'z'] 인 경우
    # 그러므로 participant의 맨마지막값을 리턴한다.
    return participant[-1]
