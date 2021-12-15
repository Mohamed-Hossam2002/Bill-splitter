from random import choice

num_users = int(input('Enter the number of friends joining (including you):\n\n'))
if num_users < 1:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), each on a new line:')
    dict_users = {input(): 0 for _ in range(num_users)}
    print()
    total_bill = int(input('Enter the total bill value:\n'))
    print()
    dict_users = {name: round(total_bill / num_users, 2) for name in dict_users}
    answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n').capitalize()
    lucky_one = choice(list(dict_users))
    print(f'\n{lucky_one} is the lucky one!\n' if answer == 'Yes' else '\nNo one is going to be lucky\n')
    lucky_one_dict_users = {name: (round(total_bill / (num_users - 1), 2) if name != lucky_one else 0) for name in dict_users}
    print(lucky_one_dict_users if answer == 'Yes' else dict_users)