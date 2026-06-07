import os.path
import io
import requests
from PIL import Image
class Character:
    def __init__(self, name, status, species, gender, origin,image,number_episodes):
        self.name = name
        self.status = status
        self.species = species
        self.gender = gender
        self.origin = origin
        self.origin=origin
        self.image_url=image
        self.number_episodes=number_episodes
        self.image_name=self.name.replace(" "," ")+".png"
        self.image_path='./images/'+self.image_name
        self.download_image()
    def show_character(self):
        print(self.name,self.gender,self.species)
    def download_image(self):
        if not os.path.exists(self.image_path):
            response=requests.get(self.image_url)
            img_data=response.content

            image=Image.open(io.BytesIO(img_data))
            #resize
            image = image.resize((200, 200), Image.Resampling.LANCZOS)
            image.save(self.image_path)
            print(self.name+"Is downloaded")
    def get_image(self):
        return Image.open(self.image_path)
