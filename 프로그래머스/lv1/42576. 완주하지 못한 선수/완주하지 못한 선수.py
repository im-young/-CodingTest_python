'''
빈 딕셔너리 만들기 - 참가자
빈 딕셔너리 만들기 - 완주자

입력 받은값 -> 참가자 dic에 넣기
입력 받은 값 -> 완주자에 넣기

두 dic 비교해서 남는 값 -> answer 에 담기

'''
def solution(participant, completion):
    part = {}
    comp ={}
    for i in participant:
      part[i] = part.get(i,0)+1
    for i in completion:
      part[i] = part.get(i,0)-1
    
    for e in part.items():
        if e[1]==1:
            answer = e[0]
    return answer
    
