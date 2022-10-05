import random
from PIL import Image
import os

thumb_size = (2800, 2800)

rootdir = os.getcwd()


def assign_traits(quantity, trait):
    for path, subdirs, files in os.walk(rootdir):
        dir = os.path.basename(path)
        if dir == trait:
            trait_list = []

            for number in range(1, quantity + 1):
                trait_list.append(Image.open(f'{trait}/{number}.png'))

            return trait_list
        else:
            continue


Backgrounds = assign_traits(2, 'BackGround')
Eyes = assign_traits(7, 'Eyes')
Bases = assign_traits(8, 'Base')
Accesss = assign_traits(6, 'Accesss')
Mouths = assign_traits(5, 'Mouth')
Snows = assign_traits(8, 'Snow')

for number in range(30):
    randomMouth = random.choice(Mouths)
    randomEyes = random.choice(Eyes)
    randomBase = random.choice(Bases)
    randomSnow = random.choice(Snows)
    randomAccesss = random.choice(Accesss)
    randomBackground = random.choice(Backgrounds)

    new_image = Image.alpha_composite(randomBackground, randomAccesss)
    new_image = Image.alpha_composite(new_image, randomSnow)
    new_image = Image.alpha_composite(new_image, randomBase)
    new_image = Image.alpha_composite(new_image, randomEyes)
    new_image = Image.alpha_composite(new_image, randomMouth)

    output = rootdir + "/OutPut/X-mas Dog" + str(number) + ".png"
    print(f"Generating {output}")
    new_image.save(output)