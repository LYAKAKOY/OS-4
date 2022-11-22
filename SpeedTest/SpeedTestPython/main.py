import time

_sum = 0
b = 3
c = 3
start_time = time.time()
for i in range(1, 100000001):
    _sum += b*2 + c - i
end_time = time.time()
print(f'Сумма: {_sum}')
print(f'Время работы: {end_time - start_time}s')