def solution(num_list):
    answer = 0
    odd = 0
    even = 0

    print(len(num_list))

    for i in range(1, len(num_list), 2):
        even += num_list[i]
    
    for i in range(0, len(num_list), 2):
        odd += num_list[i]

    print(f'odd : {odd}')
    print(f'even : {even}')
    
    return odd if odd > even else even