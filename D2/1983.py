# 1983. 조교의 성적 매기기

T = int(input())

for test_case in range(1, T+1):
    # 0번에는 학생의 수, 1번에는 성적을 알고싶은 학생의 번호
    student_count = list(map(int, input().split()))
    student_dict = dict()
    achieve = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

    score_set = student_count[0]/10

    for i in range(1, student_count[0]+1):
        score = list(map(int, input().split()))
        student_dict[i] = score[0] * 0.35 + score[1] * 0.45 + score[2] * 0.2
    
    sorted_dict= sorted(student_dict, key=student_dict.get, reverse=True)

    for j in range(1, student_count[0]+1):
        if(sorted_dict[j] == student_count[1]):
            achieve_index = int(j // score_set)
            print("#"+ str(test_case) + " " + str(achieve[achieve_index]))
            break