from random import *
from tkinter import *
game = Tk()
game.geometry('250x250')
game.title('WORDS')
def game_start():
    global random_word
    list_word = ["яблоко", "банан", "жизнь", "ложка", "холодильник","клубника","робот","игра","планета","человек","еда","метал","сталь","химия","школа","кошка"]
    star = []
    word=[]
    for i in list_word:
        random_word =choice(list_word)
    for g in random_word:
        word.append(g)
        star.append('*')
    star[0] = word[0]
    star[-1] = word[-1]
    return star
win = 0
lose = 0
def wording():
    global win
    global lose
    wordd =  word_entry.get().lower()
    if wordd == random_word:
        none_label['text'] = 'ВЫ УГАДАЛИ '
        none_label['foreground'] = '#0a0'
        word_label['text'] = game_start()
        win += 1
        win_label['text'] = f'Побед:{win}'
    elif wordd != random_word:
        none_label['text'] = 'ВЫ НЕ УГАДАЛИ '
        none_label['foreground'] = '#f00'
        word_label['text'] = game_start()
        lose += 1
        lose_label['text'] = f'Поражений:{lose}'



none_label = Label(text='',font=50)
none_label.pack()
word_label = Label(text= game_start(),font=50,)
word_label.pack()
word_entry = Entry()
word_entry.pack()
word_button = Button(text='Принять',command= wording)
word_button.pack()
win_label = Label(text=f'Побед: 0',font=50)
win_label.pack()
lose_label = Label(text=f'Поражений: 0',font=50)
lose_label.pack()
game.mainloop()






