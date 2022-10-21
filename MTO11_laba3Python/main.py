from random import randint

def random_array(n,m,max_value=20):
    array = []
    for i in range(0,n):
        sub_array = []
        for j in range(m):
            number = randint(0,max_value)
            sub_array.append(number)
        array.append(sub_array)
    return array

def print_array(array):
    print()
    for i in array:
        for j in i:
            print("%d\t" % j, end='')
        print()

def counting(array):
    print()
    max_value = array[0][0]
    max_j = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            e = array[1][j]
            if e >= max_value:
                max_value = e
                max_j = j
    print("Максимум второй строки: %d" % (max_value))
    print("Координаты максимума: [2]["+str(max_j+1)+"]")
    return max_value, max_j

def main():
    array = random_array(4,5)
    print_array(array)
    max_value,max_j = counting(array)
    while True:
        print()
        print("1. Заполнить массив случайными числами;")
        print("2. Выполнить задание")
        print("3. Выход.")
        key = input("Введите комманду 1, 2 или 3: ")
        if key == '1':
            array = random_array(4, 5)
            print_array(array)
            max_value,max_j = counting(array)
        elif key == '2':
            print()
            sum = 0
            for i in range(len(array)):
                sum = array[0][1] + array[1][1] + array[2][1] + array[3][1]
                while True:
                    try:
                        array[1][max_j] = sum
                        break
                    except ValueError:
                        break
            print_array(array)
        elif key == "3":
            exit(0)


if __name__ == '__main__':
    main()
