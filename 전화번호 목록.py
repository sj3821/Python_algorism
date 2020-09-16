# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    for i in range(len(phone_book)): # phone_book의 길이수만큼 반복
        for j in range(len(phone_book)): #phone_book의 길이수만큼 반복
            if i!=j: # i와 j가 다를 경우
                if phone_book[i] in phone_book[j][:len(phone_book[i])]: 
                    # phone_book[i] 값이 phone_book[j]의 문자열 첫번째글자부터 phone_book[i]글자수만큼 자른만큼의 영역에 존재하는지 확인(접두어인지 확인)
                    # ['12','012'] 일때 in으로 하면 접두사가 아닌데도 false가 되기 때문에 꼭 첫번째 글자부터 체크를 해야함.
                    # 접두어인게 하나라도 존재하는 경우 False를 반환하면 배열의 뒤에 있는 인덱스에 들어있는 값들은 더 볼 필요가 없음 그러므로 for문만을 끝내는 break보다는 함수 자체를 종료해야함.==> sys.exit(1) 로 함수 종료
                    return False
                    sys.exit(1)
    return True
