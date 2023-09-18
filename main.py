import commands as com
from functions import dialogue, first_coms, second_coms, third_coms, fourth_coms, fifth_coms, sixth_coms


i = 0
print(com.GREETING)
answer = dialogue(0)
while answer.lower() != 'exit':
    if answer.lower() == 'next' and i < 5:
        i += 1
        answer = dialogue(i)
        continue
    elif answer.isdigit() and '0' < answer < '5':
        if i == 0:
            first_coms(answer)
        if i == 1:
            second_coms(answer)
        if i == 2:
            third_coms(answer)
        if i == 3:
            fourth_coms(answer)
        if i == 4:
            fifth_coms(answer)
        if i == 5:
            sixth_coms(answer)
    else:
        print(com.ERROR)
        break
    proceed = input(com.CONTINUE)
    if proceed.lower() == 'yes':
        i = 0
        answer = dialogue(i)
    elif proceed.lower() == 'exit':
        break
    else:
        print(com.ERROR)
