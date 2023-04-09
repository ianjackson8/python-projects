'''
=== Fibonacci ===
- User inputs a number and outputs the corresponding Fibonacci number

Problem from IENG 331 - HW1
'''

def main():
    # get user input
    userInput = input("Enter a number: ")

    # validate input
    try:
        num = int(userInput)
    except ValueError:
        print("ERR: Invalid Input")
        return
    
    fibNum = fib(num)
    print(f'{num}->{fibNum}')

def fib(num):
    '''
    Calculates the corresponding fibonacci number in the sequence
    Uses the Fast Doubling Method: O(log n)
    f_n = f_n + f_{n+1}
    Inputs: index of sequence
    Outputs: Fibonacci number at specified index
    '''
    if num == 0:
        return 0
    else:
        mat = [[1, 1], [1, 0]]
        res = powerMat(mat, num - 1)
        return res[0][0]

def multiplyMat(a, b):
    '''
    multiplies 2x2 matrices a and b
    returns 2x2 matrix
    '''
    return [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]

def powerMat(a, pow):
    """
    Raise a matrix to the power of n
    """
    if pow == 0:
        return [[1, 0], [0, 1]]
    elif pow % 2 == 0:
        half = powerMat(a, pow // 2)
        return multiplyMat(half, half)
    else:
        return multiplyMat(a, powerMat(a, pow - 1))


if __name__ == "__main__":
    main()