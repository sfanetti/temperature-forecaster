import importable as im

def exercise_1(l):
    def perimeter(side_length):
        return 4 * side_length
    return perimeter(l)


def exercise_1_solution(l):
    def perimeter(side_length): return side_length * 4
    return perimeter(l)


def exercise_2(alpha):
    my_lst = []
    for i in range(10):
        my_lst.append(alpha[i])
    return my_lst


def exercise_2_solution(alpha):
    return [alpha[i] for i in range(10)]


def exercise_3(names):
    my_dict = {}
    for i in names:
        my_dict[i] = i.upper()
    return my_dict


def exercise_3_solution(names):
    return {name: name.upper() for name in names}


def main():
    side_length = 5
    names = ["Alice", "bob", "charlie"]
    alpha = "abcdefghijklmnopqrstuvwxyz"

    print(exercise_1(side_length))
    print(exercise_1_solution(side_length))

    print(exercise_2(alpha))
    print(exercise_2_solution(alpha))

    print(exercise_3(names))
    print(exercise_3_solution(names))

    print([(lambda x: x % 2 == 0)(x) for x in [3, 6, 12, 35, 19, 24]])
    im.this_importable()

if __name__ == '__main__':
    main()
