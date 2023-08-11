from tkinter import *
import random

deck_symbols={'HEARTS': '♥',
                'DIAMONDS': '♦',
                'CLUBS': '♣',
                'SPADES': '♠'}
deck_colors={'HEARTS': 'red',
             'DIAMONDS':'red',
             'CLUBS':'black',
             'SPADES':'black'}

class Card:
   
    def  __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.canvas=None
        self.rect=None

    def card_face(self,x1,y1,**kwargs):  #80, 130,color,
        self.canvas=canvas
        self.rect=self.canvas.create_rectangle(x1,y1,x1+80,y1+130,fill='white',width=2,**kwargs)
        self.canvas.create_text(x1+40,y1+65,text=deck_symbols[self.suit],font=('Arial',32,'bold'),fill=deck_colors[self.suit])
        self.canvas.create_text(x1+20,y1+26,text=self.rank,font=('Arial',28,'bold','underline'),fill=deck_colors[self.suit])
        self.canvas.create_text(x1+60,y1+109,text=self.rank,font=('Arial',28,'bold','underline'),fill=deck_colors[self.suit],angle=180)

class Deck:
    def  __init__(self):
        self.cards=[]
        for suit in ('HEARTS', 'DIAMONDS', 'CLUBS', 'SPADES'):
            for rank in ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'):
                self.cards.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards)==0:
            return None
        else:
            return self.cards.pop()
        
        

root=Tk()
root.geometry('1200x900')


canvas=Canvas(root,bg='green',width=1180,height=800)
canvas.place(x=10,y=10)

#start=20,20-- 120,20

my_deck=Deck()
my_deck.shuffle()
xs,ys=00,10
def kart():
    global xs,ys
    
    
    my_card=my_deck.draw()
    my_card.card_face(xs+7,ys)
    xs=((xs+90)%1170)
    if xs==0:
        ys+=140
    
    
    print(xs)


button=Button(root,text='create',command=kart)
button.place(x=600,y=850)




root.mainloop()




