
from math import pow, sqrt, floor, ceil

# part 1
item_1 = 234
item_2 = 81
result_sum = item_1 + item_2
print(result_sum)
result_subtr = item_1 - item_2
print(result_subtr)
result_multi = item_1 * item_2
print(result_multi)
result_exp = item_1**item_2
print(result_exp)
result_m_exp = pow(item_1, item_2)
print(result_m_exp)
result_s_root = item_1**0.5
print(result_s_root)
result_m_s_root = sqrt(item_1)
print(result_m_s_root)
result_mp_s_root = pow(item_1, 0.5)
print(result_mp_s_root)
item_1 = item_1 * 2 + 1
item_2 = item_2 * 2
result_division = item_1 / item_2
print(result_division)
result_m_floor = floor(result_division)
print(result_m_floor)
result_m_ceil = ceil(result_division)
print(result_m_ceil)
result_int = int(result_division)
print(result_int)
result_no_division_loss = item_1 // item_2
print(result_no_division_loss)
result_division_loss = item_1 % item_2
print(result_division_loss)

# part 2
item_3 = 123
item_3 += 10
print(item_3)
item_3 -= 5
print(item_3)
item_3 *= 3
print(item_3)
item_3 /= 2
print(item_3)
item_3 **= 2
print(item_3)
item_3 **= 0.5
print(item_3)
item_3 %= 2
print(item_3)

# part 3
b_item_t = True
b_item_f = False
b_item_result_sum = b_item_f + b_item_t
print(b_item_result_sum)
b_item_result_subtr = b_item_t - b_item_f
print(b_item_result_subtr)
b_item_result_multi = b_item_t * b_item_f
print(b_item_result_multi)
try:
    b_item_result_division = b_item_t / b_item_f
    print(b_item_result_division)
except:
    print("Не повезло не прокатило")
b_item_1_int = int(b_item_t)
print(b_item_1_int)
b_item_2_int = int(b_item_f)
print(b_item_2_int)
