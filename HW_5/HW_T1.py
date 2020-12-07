
first_num = (int(input('Please input first integer ')))
last_num = (int(input('Please input last integer ')))

integers = list(range(first_num,last_num+1))
float_num = []

for i in integers:
    i = float(i)
    float_num.append(i)

print(float_num, end=' ')