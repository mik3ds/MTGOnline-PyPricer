
# coding: utf-8

# In[7]:


def pricecards(l):
    temp = []
    for i in l:
        name = "0"
        copies = "0"
        price = "0"
        components = i.split("(")
        if len(i) >= 5:
            components2 = components[1].split("x")
            name = components[0]
            if len(components2) == 2:
                copies = components2[0]
                tempprice = components2[1].split(")")
                price = tempprice[0]
            else:
                copies = "1"
                tempprice = components[1].split(")")
                price = tempprice[0]
        else:
            l.remove(i)
        if name != "0":
            copies = float(copies)
            price = float(price)
            temp.append([name,copies,price])
    return temp

def printnice(l):
    total = 0
    for i in l:
        total += i[1]*i[2]
        tempstring = str(i[1]*i[2]) + i[0] + " \\ Copies: " + str(int(i[1])) + " \\ Price: " + str(i[2])
        print(tempstring)
    print(total)
    
def sortcardlist(l):
    #The line below sorts the results by Total Amount you gain from selling all copies of the card (2 Force of Will (16 tix each, 32 tix total) will be listed higher than 1 x Jace, The Mindsculpter (24 tix total))
    l.sort(key = lambda x: x[2]*x[1], reverse=True)
    #The line below sorts the results by Total Amount you gain from selling one copy of the card
    #l.sort(key = lambda x: x[2], reverse=True)
    return l

#Add your text below with the timestamps and bot names removed

Edited_Text = """

"""


printnice(sortcardlist(pricecards(Edited_Text.split(":"))))

