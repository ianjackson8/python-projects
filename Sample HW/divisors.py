'''
=== Divisors ===
- User inputs a number and returns the divisors of the number

Problem from IENG 331 - HW1
'''

def main():
    '''
    main function
    uses the modulo operator to find if the number is evenly divisible
    '''
    userInput = input("Enter an integer: ")

    # validate input 
    try:
        num = int(userInput)
    except ValueError:
        # cannot convert str->num
        print("ERR: Invalid input")
        return

    # iterate all integers up to input
    for i in range(1,num+1):
        # base case/ending number
        if i == num:
            print(i)
        elif (num % i) == 0:
            print(i, end=', ')
        
if __name__ == "__main__":
    main()