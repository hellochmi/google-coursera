# python3


def max_pairwise_product(numbers):
    if len(numbers) <= 1:
        return 0
    
    numbers.sort()

    return numbers[len(numbers)-1] * numbers[len(numbers)-2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
