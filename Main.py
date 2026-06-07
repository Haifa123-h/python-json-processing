# importing modules

import requests
from tkinter import *
from PIL import Image,ImageTk
from Character import Character
from Scrollable import ScrollableFrame
url='https://rickandmortyapi.com/api/character/?page=1'
def load_data():
    response=requests.get(url)
    json_res=response.json()
    json_res_results=json_res['results']
    characters=[]
    for obj in json_res_results:
     name=obj['name']
     status=obj['status']
     species=obj['species']
     gender=obj['gender']
     origin=obj['origin']['name']
     image_url=obj['image']
     number_episodes=len(obj['episode'])
     character=Character(name,status,species,gender,origin,image_url,number_episodes)
     characters.append(character)
    return characters
characters=load_data()

#making the ui
root=Tk()
root.title('Rick and morty characters')
root.geometry('535x560')
root.update()
root.resizable(0,0)
scrollable=ScrollableFrame(root)

for char in characters:
    
    #main item frame of each of the characters
    list_item_frame=Frame(scrollable.scrollable_frame,borderwidth=4,relief=GROOVE)



    #left frame
    left_frame=Frame(list_item_frame)
    #load the image
    photo=ImageTk.PhotoImage(char.get_image())
    image_lbl=Label(left_frame,image=photo)
    image_lbl.imafe=photo
    image_lbl.pack(fill=BOTH , expand=True)
    left_frame.grid(row=0,column=0,padx=7.5,pady=15)
    #right frame
    right_frame=Frame(list_item_frame)


    right_frame.grid(row=0,column=1,sticky='we')

    #name label
    Label(right_frame,text="Name: "+char.name,font=("calibri",12),padx=7.5).pack(anchor=W,expand=True)
    Label(right_frame,text="Species: "+char.species,font=("calibri",12),padx=7.5).pack(anchor=W,expand=True)
    Label(right_frame,text="Gender: "+char.gender,font=("calibri",12),padx=7.5).pack(anchor=W,expand=True)
    Label(
        right_frame,
        text="Origin: " +char.origin,
        font=("calibri", 12),
        padx=7
    ).pack(anchor=W, fill="x", expand=True)

    Label(right_frame,text="Status: "+char.status,font=("calibri",12),padx=7.5).pack(anchor=W,expand=True)

    Label(
        right_frame,
        text=str(char.number_episodes)+" episodes",
        font=("calibri", 12),
        padx=7.5
    ).pack(anchor=W, expand=True)

    list_item_frame.pack(fill=X,padx=7.5)



scrollable.pack(fill=BOTH,expand=True)

root.mainloop()