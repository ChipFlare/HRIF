from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog

file_path = ''

color_palette = {
    '#000000': 'Black',
    '#000055': 'Dark Navy',
    '#0000aa': 'Navy Blue',
    '#0000ff': 'Blue',
    '#005500': 'Dark Green',
    '#005555': 'Dark Teal',
    '#0055aa': 'Deep Teal',
    '#0055ff': 'Teal',
    '#00aa00': 'Dark Green',
    '#00aa55': 'Green',
    '#00aaaa': 'Cyan',
    '#00aaff': 'Light Cyan',
    '#00ff00': 'Green',
    '#00ff55': 'Lime Green',
    '#00ffaa': 'Spring Green',
    '#00ffff': 'Cyan',
    '#550000': 'Dark Red',
    '#550055': 'Purple',
    '#5500aa': 'Purple',
    '#5500ff': 'Medium Purple',
    '#555500': 'Dark Olive',
    '#555555': 'Dark Grey',
    '#5555aa': 'Grey',
    '#5555ff': 'Light Grey',
    '#55aa00': 'Olive',
    '#55aa55': 'Olive Drab',
    '#55aaaa': 'Light Slate Grey',
    '#55aaff': 'Silver',
    '#55ff00': 'Lime',
    '#55ff55': 'Pale Green',
    '#55ffaa': 'Pale Turquoise',
    '#55ffff': 'Light Sky Blue',
    '#aa0000': 'Dark Maroon',
    '#aa0055': 'Maroon',
    '#aa00aa': 'Purple',
    '#aa00ff': 'Medium Purple',
    '#aa5500': 'Brown',
    '#aa5555': 'Rosy Brown',
    '#aa55aa': 'Light Purple',
    '#aa55ff': 'Medium Purple',
    '#aaaa00': 'Olive',
    '#aaaa55': 'Khaki',
    '#aaaaaa': 'Grey',
    '#aaaaff': 'Light Violet',
    '#aaff00': 'yellow lime',
    '#aaff55': 'Light Lime',
    '#aaffaa': 'Light Aqua',
    '#aaffff': 'White Cyan',
    '#ffffff': 'White',
    '#ff0000': 'Red',
    '#ff0055': 'Light Pink',
    '#ff00aa': 'Pink',
    '#ff00ff': 'Magenta',
    '#ff5500': 'Orange',
    '#ff5555': 'Salmon',
    '#ff55aa': 'Light Coral',
    '#ff55ff': 'Light Pink',
    '#ffaa00': 'Yellow',
    '#ffaa55': 'Light Yellow',
    '#ffaaaa': 'Light Peach',
    '#ffaaff': 'Light Pink',
    '#ffff00': 'Yellow',
    '#ffff55': 'Light Yellow',
    '#ffffaa': 'Pale Yellow',
    '#ffffff': 'White'
}

def image_to_2bit_rgb(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    img_array = np.array(img)
    rgb_list = []
    for row in img_array:
        for pixel in row:
            r, g, b = pixel[0], pixel[1], pixel[2]
            r2bit = int(r/255*3)*85
            g2bit = int(g/255*3)*85
            b2bit = int(b/255*3)*85
            rgb_list.append(color_palette['#%02x%02x%02x'%(r2bit, g2bit, b2bit)])
    return rgb_list

def choose_image_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Choose an image file",
                                           filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    if file_path:
        return file_path
    else:
        return None

def save():
    global rgb_list
    file_path= filedialog.asksaveasfilename(title="Save File", filetypes=[('Human Readable Image Format','.hrif')], defaultextension=".hrif")
    with open(file_path, 'w') as file:
        index = 0
        while index < len(rgb_list):
            file.write(str(rgb_list[index])+',')
            index = index + 1


image_path = choose_image_file()
img = Image.open(str(image_path))
width, height = img.size 
if image_path:
    print('Processing...')
    print('')
    print('Image Details:')
    print('width = '+str(width))
    print('height = '+str(height))
    rgb_list = image_to_2bit_rgb(image_path)
    rgb_list.insert(0, height)
    rgb_list.insert(1, width)
    print('')
    print('file contents: '+str(rgb_list[:10])+'...')
    save()
    print("saved")
else:
    print("No image file selected.")
