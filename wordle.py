def disp(sol_list):
    for i in range(len(sol_list)):
        print(str(i+1) + ': ' + sol_list[i].replace('\n', ''))

def check(guess, sol):
    result = ''
    for i in range(5):
        if guess[i] == sol[i]:
            result += '2'
            continue
        elif guess[i] in sol:
            if guess[i] in guess[:i]:
                if guess[i] in sol.replace(guess[i], '', guess[:i].count(guess[i])):
                    result += '1'
                else:
                    result += '0'
            elif guess[i] in guess[i+1:]:
                for j in range(i+1, 5):
                    if guess[j] == guess[i] == sol[j]:
                        if guess[i] in sol.replace(guess[i], '', guess[i+1:].count(guess[i])):
                            result += '1'
                        else:
                            result += '0'
                        break
                else:
                    result += '1'
            else:
                result += '1'
        else:
            result += '0'
    return result

# Narrow Down: return a new list of possible solutions given the clue for the most recent guess and the previous list of possible solutions
def narrow(guess, clue, possible_sols):
    result = []
    for word in possible_sols:
        if check(guess, word) == clue:
            result.append(word)
    return result


# How many groups would making the given guess divide the list of remaining possibilities into?
def num_groups(guess, poss_rem):
    clues = []
    groups = 0
    for sol in poss_rem:
        check_guess = check(guess, sol)
        if check_guess not in clues:
            groups += 1
            clues.append(check_guess)
    return groups
    
# Given the remaining possibilities, what word would split the list into the most groups, optionally restrict to possible solutions
def best_guess(poss_rem, options):
    groups_max = 0
    for guess in options:
        groups = num_groups(guess, poss_rem)
        if groups > groups_max:
            groups_max = groups
            best = guess
    return (best, groups_max)


# while True: 
#     rec_guess = input(f'Enter your {turn_adjs[turn_count-1]} guess: ')
#     rec_clue = input('Enter clue: ')
#     turn_count += 1
#     solutions = narrow(rec_guess, rec_clue, solutions)
#     if len(solutions) == 1:
#         is_are = ('is', 'solution', 'it', '')
#     else:
#         is_are = ('are', 'solutions', 'them', 's')
#     skip = input(f'There {is_are[0]} {len(solutions)} remaining possible {is_are[1]}. Would you like to see {is_are[2]}? (Y/N) ')
#     if skip.upper() == 'Y':
#         for i in range(len(solutions)):
#             print(i+1, ': ', solutions[i], sep='')
#     rcmd_a = best_guess(solutions, solutions)
#     rcmd_b = best_guess(solutions, valid_list)
#     print(f"Your best possible solution guess is '{rcmd_a[0]}' (yielding {rcmd_a[1]} group{is_are[3]}).")
#     if rcmd_b[1] > rcmd_a[1]:
#         print(f"Your best overall guess is '{rcmd_b[0]}' (yielding {rcmd_b[1]} group{is_are[3]}).")
#     cont = input('Have you found the solution? (Y/N): ')
#     if cont.upper() == 'Y':
#         break
#     else:
#         continue
# print(f"Congrats! You solved today's Wordle in {turn_count} guesses! :)")