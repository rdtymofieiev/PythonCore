def solution(number):
    numbers = list(range(1,number))
    mult_3 = [i for i in numbers if i%3==0]
    mult_5 = [i for i in numbers if i%5==0]
    final_list = list(set(mult_3) | set(mult_5))
    return sum(final_list)