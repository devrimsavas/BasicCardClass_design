from tkinter import *
import random
CARD_WIDTH=80
CARD_HEIGHT=130
symbols={'HEARTS': ['♥','red'],'DIAMONDS': ['♦','red'],'CLUBS': ['♣','black'],'SPADES': ['♠','black'] }

class Card:
    def  __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.flag=0

    
        

    def card_face(self,canvas,x,y,**kwargs):
        global btext
        self.x=x
        self.y=y
        self.rect=canvas.create_rectangle(x,y,x+CARD_WIDTH,y+CARD_HEIGHT,fill='white',width=2,**kwargs)
        btext=""
        for i in range(6):
            btext+='▓'*6+'\n'

        self.text=canvas.create_text(self.x+40 , self.y+74 , text=btext,font=('Arial', 12, 'bold'), fill='red')        
        canvas.tag_bind(self.rect, '<Button-1>',self.show_card)
        canvas.tag_bind(self.text, '<Button-1>',self.show_card)

    def show_card(self,event):
        
        global btext
        ctext=f"""




          ▓▓▓▓▓▓
          ▓▓▓▓▓▓
          ▓▓▓▓▓▓
          ▓▓▓▓▓▓
          ▓▓▓▓▓▓
          ▓▓▓▓▓▓
"""       
        
        
        
        self.flag=1-self.flag
        cardvalue=f"""\n\n\n{' ':4}{self.rank:2}
{' ':7}{symbols[self.suit][0]:^00}
{' ':8}{self.rank:2}
"""
        

        if self.flag==1:
            canvas.itemconfig(self.rect,fill='white')
            #canvas.itemconfig(self.text,text="")
            canvas.delete(self.text)
            self.text=canvas.create_text(self.x+20,self.y+26,text=cardvalue,font=('Arial',26,'bold'),fill=symbols[self.suit][1])
        if self.flag==0:
            canvas.itemconfig(self.rect,fill='white')
            canvas.itemconfig(self.text,text=ctext,font=('Arial',12,'bold'),fill='red')
        
                                     
class Deck:
    def  __init__(self):
        self.cards=[]
        for suit in ('HEARTS', 'DIAMONDS', 'CLUBS', 'SPADES'):
            for rank in ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'):
                self.cards.append(Card(suit,rank))
    def shuffle(self):
        random.shuffle(self.cards)
    def draw(self):
        try:
            return self.cards.pop()
        except IndexError:
            raise IndexError('The Deck is Empty')


root=Tk()
root.geometry('1200x900')
root.resizable(False,False)

canvas=Canvas(root,bg='green',width=1180,height=800)
canvas.place(x=10,y=10)
my_deck=Deck()
my_deck.shuffle()
xs,ys=0,10

def kart():
    global xs,ys
    my_card=my_deck.draw()
    my_card.card_face(canvas,xs+7,ys)
    xs=((xs+90)%1170)
    if xs==0:
        ys+=140


button=Button(root,text='DRAW CARD',command=kart)
button.place(x=600,y=850)
root.mainloop()









        
        
     
        
        
