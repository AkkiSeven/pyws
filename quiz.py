print('Hello, welcome to "Test your Knowledge Quiz"!!!')


ans = input('Are you ready to play (yes/no): ')
score = 0
total_q = 4

if ans.lower() == 'yes':
    ans = input('1. What is the best programming language?')
    if ans.lower() == 'python':
        score += 1
        print('Correct')
    else:
        print("Incorrect")

    ans = input('2. What is 2 + 8 + 9 -1 ?')
    if ans == '18':
        score += 1
        print('Correct')
    else:
        print("Incorrect")

    ans = input('3. Which is better a 1050ti or a 1060 (graphics card)?')
    if ans.lower() == '1060':
        score += 1
        print('Correct')
    else:
        print("Incorrect")

    ans = input('4. How many steps can a king move (chess)?')
    if ans.lower() == '1' or ans.lower() == '1 step':
        score += 1
        print('Correct')
    else:
        print("Incorrect")

    print('Thank you for playing, you got ', score, "questions correct.")
    mark = (score/total_q) * 100

    print("Mark: ", str(mark) + '%')
print("Goodbye")
