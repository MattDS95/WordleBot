import wordle as wd, tkinter as tk

root = tk.Tk()

def main():
    while True:
        guess_input(turn_count)
        break

def guess_input(turn):
    tk.Label(root, text=f'Enter your {turn_adjs[turn-1]} guess: ').grid(row=2*turn, column=0)
    guess = tk.Entry(root)
    guess.grid(row=2*turn, column=1)
    clue = tk.Entry(root)
    clue.grid(row=2*turn, column=2)
    tk.Button(root, text='Go', command=lambda guess=guess, clue=clue: process_input(guess.get(), clue.get())).grid(row=2*turn, column=3)

def process_input(guess, clue):
    global solutions
    solutions = wd.narrow(guess, clue, solutions)
    message = tk.Label(root, text='There are ')

sol_list = []
for word in open('sol_list.txt', 'rt').readlines():
    sol_list.append(word.replace('\n', ''))

valid_list = []
for word in open('valid_list.txt', 'rt').readlines():
    valid_list.append(word.replace('\n', ''))

solutions = sol_list
turn_count = 1
turn_adjs = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']

tk.Label(root, text='Wordle Assistant').grid(row=0, column=1)
tk.Button(root, text='Click here to begin', command=main).grid(row=1, column=0)

root.mainloop()