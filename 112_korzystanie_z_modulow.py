print('*** Lesson ***\n')

import math # import modułu math

pi = math.pi
print(pi)

# math floor zaokrągla do w dół do najbliższej liczby całkowitej
result1 = math.floor(3.7)
result2 = math.floor(math.pi)
print(result1,result2)

print('\n*** LAB ***')
print('\nTask 1\n')

import statistics

percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,
           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,
           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,
           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,
           8.740978348,6.174819567]

percent.sort()
print(percent)

low_m = statistics.median_low(percent)
high_m = statistics.median_high(percent)
med = statistics.median(percent)

print(med,low_m,high_m)