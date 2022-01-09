from PIL import Image
import json
import numpy as np

for num in range(8887):
    Foreground_index = np.random.choice(10, p=[0.05, 0.08, 0.11, 0.1, 0.12, 0.11, 0.1, 0.1, 0.15, 0.08])
    #Foreground_index = 0;
    Foreground_arr = ["Crypto", "Energy", "Fashion & Retail", "Finance & Investments", "Healthcare", "Manufacturing", "Media & Entertainment", "Real Estate", "Food & Beverage", "Technology"];
    Foreground = "./image/1. Foreground/{}.png"
    Foreground = (Foreground.format(Foreground_index+1))
    Leftarm_index = np.random.choice(9, p=[0.3, 0.15, 0.05, 0.03, 0.05, 0.15, 0.01, 0.06, 0.2])
    #Leftarm_index = 6
    Leftarm_arr = ["no item", "Beaded Bracelet", "Cartier Bracelet", "Diamond Watch", "Gold Bracelet", "Paracord Bracelet", "Whalex", "Rosary Bracelet", "Smartwatch"]
    Leftarm = "./image/2. Left Arm Acc/{}.png"
    Leftarm = (Leftarm.format(Leftarm_index))
    Handacc_index = np.random.choice(10, p=[0.25, 0.03, 0.01, 0.08, 0.08, 0.1, 0.1, 0.05, 0.15, 0.15])
    #Handacc_index = 2
    Handacc_arr = ["no item", "Diamond", "Trident", "Money", "Money Bag", "Paint Brush", "Pointer", "Poker Chip", "Smartphone", "Wallet"]
    Handacc = "./image/3. Hands Acc/{}.png"
    Handacc = (Handacc.format(Handacc_index))
    Neckacc_index = np.random.choice(10, p=[0.4, 0.12, 0.05, 0.1, 0, 0.04, 0.06, 0.12, 0.05, 0.06])
    #Neckacc_index = 5
    Neckacc_arr = ["no item", "Bow Tie", "Diamond-Necklace", "Cross necklace", "Gold", "Gold Medal", "Link Necklace", "Necktie", "Pearl necklaces", "Red Scarf"]
    Neckacc = "./image/4. Neck Acc/{}.png"
    Neckacc = (Neckacc.format(Neckacc_index))
    Headacc_index = np.random.choice(26, p=[0.3, 0.03, 0.04, 0.04, 0.03, 0.03, 0.04, 0.04, 0.01, 0.01, 0.04, 0.05, 0.03, 0.01, 0, 0.02, 0.03, 0.03, 0.03, 0.04, 0, 0.03, 0.04, 0, 0.05, 0.03])
    #Headacc_index = 8
    Headacc_arr = ["no Hat", "Army Hat", "Aviator Hat", "Beret", "Boater Hat", "Bowler Hat", "Bucket Hat", "Cowboy Hat", "Crown", "Devil Horns", "Fedora", "Fisherman's Hat", "Graduation Hat", "Halo", "Hard Hat", "Beats headphones", "Party Hat", "Pirate's Hat", "Red Cap", "Sailor's Hat", "Santa Hat", "Sombrero", "Top Hat", "Visor", "Whale Spout", "Witch Hat"]
    Headacc = "./image/5. Head Acc/{}.png"
    Headacc = (Headacc.format(Headacc_index))
    Eyesacc_index = np.random.choice(12, p=[0.2, 0.03, 0.1, 0.07, 0.07, 0.09, 0.07, 0.07, 0.09, 0.01, 0.09, 0.11])
    #Eyesacc_index = 9
    Eyeacc_arr = ["no item", "3D Glasses", "Aviator Glasses", "Eye Patch", "Hollywood Glasses", "Oval Glass", "Sting Rays", "Round Sunglass", "Sports Sunglass", "Thug Life Glass", "Wayfarer glasses", "Prescription Glasses"]
    Eyesacc = "./image/6. Eyes Acc/{}.png"
    Eyesacc = (Eyesacc.format(Eyesacc_index))
    Eyes_index = np.random.choice(6, p=[0.15, 0.1, 0.2, 0.25, 0.15, 0.15])
    #Eyes_index = 1
    Eyes_arr = ["Angry", "Cross Eyed", "Happy", "Standard", "Stoned", "Bug Eyed"]
    Eyes = "./image/7. Eyes/{}.png"
    Eyes = (Eyes.format(Eyes_index+1))
    Mouth_index = np.random.choice(16, p=[0.14, 0.06, 0.02, 0.08, 0.06, 0.06, 0.03, 0.03, 0.01, 0.06, 0.08, 0.14, 0.05, 0.07, 0.06, 0.05])
    #Mouth_index = 8
    Mouth_arr = ["Big Smile", "Coin Bite", "Biting Diamond", "Biting Fish", "Bubble Gum", "Cigar", "Diamond teeth", "Gold Teeth", "One Gold Tooth", "Lollipop", "Biting Red Fish", "Smile", "Tobacco", "Tongue", "Vape", "Weed"]
    Mouth = "./image/8. Mouth/{}.png"
    Mouth = (Mouth.format(Mouth_index+1))
    Body_index = np.random.choice(20, p=[0.03, 0.04, 0.09, 0.08, 0.06, 0.02,  0.01, 0.08, 0.06, 0.04, 0.04, 0.06, 0.06, 0.06, 0.04, 0.06, 0.04, 0.04, 0.06, 0.03])
    #Body_index = 6
    Body_arr = ["Alien Green", "Black", "Black Camo", "Blue", "Brown", "Diamond", "Gold", "Gray", "Green", "Lava", "Ocean Sand", "Orange", "Pink", "Purple", "Rainbow", "Red", "Reptile", "Seaweed", "Yellow", "Zombie"]
    Body = "./image/9. Body/{}.png"
    Body = (Body.format(Body_index+1))
    Industry_arr = ["Crypto", "Energy", "Fashion & Retail", "Finance & Investments", "Healthcare", "Manufacturing", "Media & Entertainment", "Real Estate", "Restaurant", "Technology"]
    Industry = "./image/10. Industry/{}.png"
    Industry = (Industry.format(Foreground_index+1))

    Foreground_img = Image.open(Foreground)
    Leftarm_img = Image.open(Leftarm)
    Handacc_img = Image.open(Handacc)
    Neckacc_img = Image.open(Neckacc)
    Headacc_img = Image.open(Headacc)
    Eyesacc_img = Image.open(Eyesacc)
    Eyes_img = Image.open(Eyes)
    Mouth_img = Image.open(Mouth)
    Body_img = Image.open(Body)
    Industry_img = Image.open(Industry)

    Industry_img.paste(Body_img, (0, 0), mask=Body_img)
    Industry_img.paste(Mouth_img, (0, 0), mask=Mouth_img)
    Industry_img.paste(Eyes_img, (0, 0), mask=Eyes_img)
    Industry_img.paste(Eyesacc_img, (0, 0), mask=Eyesacc_img)
    Industry_img.paste(Headacc_img, (0, 0), mask=Headacc_img)
    Industry_img.paste(Neckacc_img, (0, 0), mask=Neckacc_img)
    Industry_img.paste(Handacc_img, (0, 0), mask=Handacc_img)
    Industry_img.paste(Leftarm_img, (0, 0), mask=Leftarm_img)
    Industry_img.paste(Foreground_img, (0, 0), mask=Foreground_img)
    image = "./result/{}.png"
    image = image.format(num+1)
    Industry_img.save(image)
    URI = "https://whales.mypinata.cloud/ipfs/QmVkRQqYsuEBxweSPzXiD4WuVNniPpEY5jiEQwpD1ogU4a/{}.png"
    URI = (URI.format(num+1))
    dictionary = {
        "attributes": [
          {
            "trait_type": "Foreground",
            "value": Foreground_arr[Foreground_index]
          },
          {
            "trait_type": "Left Fin Accessory",
            "value": Leftarm_arr[Leftarm_index]
          },
          {
            "trait_type": "Right Fin Accessory",
            "value": Handacc_arr[Handacc_index]
          },
          {
            "trait_type": "Neck Accessory",
            "value": Neckacc_arr[Neckacc_index]
          },
          {
            "trait_type": "Head Accessory",
            "value": Headacc_arr[Headacc_index]
          },
          {
            "trait_type": "Eyes Accessory",
            "value": Eyeacc_arr[Eyesacc_index]
          },
          {
            "trait_type": "Eyes",
            "value": Eyes_arr[Eyes_index]
          },
          {
            "trait_type": "Mouth",
            "value": Mouth_arr[Mouth_index]
          },
          {
            "trait_type": "Body",
            "value": Body_arr[Body_index]
          },
          {
            "trait_type": "Industry",
            "value": Industry_arr[Foreground_index]
          },
        ],
        "description": "Wealthy Whale Club NFT Collection",
        "image": URI,
        "name": "Wealthy Whale Club"
    }

    # Serializing json
    json_object = json.dumps(dictionary)

    # Writing to sample.json
    file = "./Json/{}.json"
    file = (file.format(num+1))
    with open(file, "w") as outfile:
        outfile.write(json_object)

        print(file)