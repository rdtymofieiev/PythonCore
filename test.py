numbers = list(range(0,11))

even = [num_even for num_even in numbers if num_even % 2 == 0]
odd = [num_odd for num_odd in numbers if num_odd % 3 == 0]
div_except_23 = [num_other for num_other in numbers if not num_other % 2 == 0 and not num_other % 3 == 0]

print(div_except_23)