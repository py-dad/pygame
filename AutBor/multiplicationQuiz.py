import pyinputplus as pyip
import random, time


numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0,20)
    num2 = random.randint(0,20)
    wrd = '(You got this!)'

    prompt = '#%s: %s x %s %s = ' % (questionNumber, num1, num2, wrd)


    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                  blockRegexes=[('.*', 'Incorrect!')],
                  timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    
    else:
        print('Correct!')
        correctAnswers += 1

    time.sleep(1) # brief pause to let user see the result
    
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))