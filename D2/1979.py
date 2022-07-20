# 1979. 어디에 단어가 들어갈 수 있을까

def puzzle_check(list, size):
    split_list = ''.join(list).split("0")
    count = 0
    for i in split_list:
        if(len(i) == size):
            count += 1
    return count


T = int(input())

for test_case in range(1, T+1):
    puzzle_size = list(map(int, input().split()))
    puzzle = []
    true_count = 0

    #입력값 받기 + 가로 검증 
    for i in range(0, puzzle_size[0]):
        input_list = list(map(str, input().split()))
        true_count += puzzle_check(input_list, puzzle_size[1])
        puzzle.append(input_list)
        
    # 세로 검증
    for j in range(0, puzzle_size[0]):
        new_list = []
        for k in range(0, puzzle_size[0]):
            new_list.append(puzzle[k][j])
        true_count += puzzle_check(new_list, puzzle_size[1])
    
    print("#"+ str(test_case) + " " + str(true_count))
