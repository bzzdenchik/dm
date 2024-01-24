def is_kelly_commutative(kelly_table):
    n = len(kelly_table)
    for i in range(n):
        for j in range(n):
            if kelly_table[i][j] != kelly_table[j][i]:
                return False
    return True

def is_kelly_associative(kelly_table):
    n = len(kelly_table)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if int(kelly_table[int(kelly_table[i][j])][k])!= int(kelly_table[i][int(kelly_table[j][k])]):
                    return False
    return True

def is_kelly_reversible(kelly_table, neutral_element):
    n = len(kelly_table)
    for i in range(n):
        for j in range(n):
            if kelly_table[i][j] == neutral_element:
                if kelly_table[j][i] == neutral_element:
                    break
        else:
            return False
    return True

def find_neutral_element(kelly_table, elements):
    n = len(kelly_table)
    for i in range(n):
        for j in range(n):
            if kelly_table[i][j] != elements[j]:
                break
        else:
            return elements[i]
    return False

def find_subgroups(kelly_table,elements):
    n = len(kelly_table)
    subgroups = []
    for i in range(1, 2**n):
        subset_index = []
        for j in range(n):
            if (i >> j) & 1:
                subset_index.append(j)
        closed = True
        subset = [elements[l] for l in subset_index]
        for a in subset_index:
            for b in subset_index:
                if kelly_table[a][b] not in subset:
                    closed = False
                    break
            if not closed:
                break
        if closed and subset not in subgroups:
            subset_kelly = [[kelly_table[y][u] for u in subset_index] for y in subset_index]
            neutral_element  = find_neutral_element(subset_kelly,subset)
            if neutral_element != False:
                if is_kelly_reversible(subset_kelly,neutral_element):
                    subgroups.append(subset)
    return subgroups

def find_normal_subgroups(kelly_table, elements):
    n = len(kelly_table)
    normal_subgroups = []
    subgroups = find_subgroups(kelly_table,elements)
    for subgroup in subgroups:
        k = len(subgroup)
        for i in range(n):
            left_class = []
            right_class = []
            for j in range(k):
                left_class.append(kelly_table[i][j])
                right_class.append(kelly_table[j][i])
            if set(left_class) == set(right_class):
                if subgroup not in normal_subgroups:
                    normal_subgroups.append(subgroup)
    if len(normal_subgroups)>0:
        return normal_subgroups
    else:
        return False

associative = False
reversible = False
n = int(input("Введите размер таблицы Кэли: "))

kelly_table = []
print("Введите таблицу Кэли:")
for i in range(n):
    element = list(input().split())
    kelly_table.append(element)
kelly_table_1 = []
for i in range(1,n):
    row = []
    for j in range(1,n):
        row.append(kelly_table[i][j])
    kelly_table_1.append(row)

if is_kelly_commutative(kelly_table_1):
    print("Коммутативна")
else:
    print("Не коммутативна")

if is_kelly_associative(kelly_table_1):
    print("Ассоциативна")
    associative = True
else:
    print("Не ассоциативна")

first_string = kelly_table[0]
first_string.pop(0)
neutral_element = find_neutral_element(kelly_table_1, first_string)
if neutral_element != False:
    print("Нейтральный элемент: " + str(neutral_element))
    if is_kelly_reversible(kelly_table_1, neutral_element):
        print("Обратима")
        reversible = True
    else:
        print("Не обратима")
else:
    print("Нейтральный элемент не найден")
    print("Не обратима")
normal_subgroups = find_normal_subgroups(kelly_table_1,first_string)
if  normal_subgroups != False and reversible and associative:
    print("Нормальные подгруппы:")
    for i in normal_subgroups:
        print(*i)
else:
    print("Нормальные подгруппы не обнаружены")



