def convert(c):
    if (c == 'A'): return 'C'
    if (c == 'C'): return 'G'
    if (c == 'G'): return 'T'
    if (c == 'T'): return 'A'

print("Start")

opt = "ACGT"
s = ""
s_last = ""
len_str = 13

for i in range(len_str):
    s += opt[0]

for i in range(len_str):
    s_last += opt[-1]

pos = 0
counter = 1
while (s != s_last):
    counter += 1
    # Следующая строка выводит результаты
    # print(s)
    change_next = True
    for i in range(len_str):
        if (change_next):
            if (s[i] == opt[-1]):
                s = s[:i] + convert(s[i]) + s[i+1:]
                change_next = True
            else:
                s = s[:i] + convert(s[i]) + s[i+1:]
                break

# Следующая строка выводит результаты
# print(s)
print("Number of generated k-mers: {}".format(counter))
print("Finish!")
