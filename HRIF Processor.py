import sys
from PIL import Image
import time
from colorama import init, Fore, Style

init()

def print_error(message):
    print(Fore.RED + message + Style.RESET_ALL)



color_palette= {
    'Black': '#000000',
    'Dark Navy': '#000055',
    'Navy Blue': '#0000aa',
    'Blue': '#0000ff',
    'Dark Green': '#005500',
    'Dark Teal': '#005555',
    'Deep Teal': '#0055aa',
    'Teal': '#0055ff',
    'Dark Green': '#00aa00',
    'Green': '#00aa55',
    'Cyan': '#00aaaa',
    'Light Cyan': '#00aaff',
    'Green': '#00ff00',
    'Lime Green': '#00ff55',
    'Spring Green': '#00ffaa',
    'Cyan': '#00ffff',
    'Dark Red': '#550000',
    'Purple': '#550055',
    'Purple': '#5500aa',
    'Medium Purple': '#5500ff',
    'Dark Olive': '#555500',
    'Dark Grey': '#555555',
    'Grey': '#5555aa',
    'Light Grey': '#5555ff',
    'Olive': '#55aa00',
    'Olive Drab': '#55aa55',
    'Light Slate Grey': '#55aaaa',
    'Silver': '#55aaff',
    'Lime': '#55ff00',
    'Pale Green': '#55ff55',
    'Pale Turquoise': '#55ffaa',
    'Light Sky Blue': '#55ffff',
    'Dark Maroon': '#aa0000',
    'Maroon': '#aa0055',
    'Purple': '#aa00aa',
    'Medium Purple': '#aa00ff',
    'Brown': '#aa5500',
    'Rosy Brown': '#aa5555',
    'Light Purple': '#aa55aa',
    'Medium Purple': '#aa55ff',
    'Olive': '#aaaa00',
    'Khaki': '#aaaa55',
    'Grey': '#aaaaaa',
    'Light Violet': '#aaaaff',
    'yellow lime': '#aaff00',
    'Light Lime': '#aaff55',
    'Light Aqua': '#aaffaa',
    'White Cyan': '#aaffff',
    'White': '#ffffff',
    'Red': '#ff0000',
    'Light Pink': '#ff0055',
    'Pink': '#ff00aa',
    'Magenta': '#ff00ff',
    'Orange': '#ff5500',
    'Salmon': '#ff5555',
    'Light Coral': '#ff55aa',
    'Light Pink': '#ff55ff',
    'Yellow': '#ffaa00',
    'Light Yellow': '#ffaa55',
    'Light Peach': '#ffaaaa',
    'Light Pink': '#ffaaff',
    'Yellow': '#ffff00',
    'Light Yellow': '#ffff55',
    'Pale Yellow': '#ffffaa',
    'White': '#ffffff',
    '':''
}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python process_script.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    with open(filename, 'r') as f:
        contents = f.read()
        
raw_list = contents.split(',')

height = int(raw_list[0])
width = int(raw_list[1])

rgb_list =[]

def decode():
    index = 2
    while index < len(raw_list):
        try:
            rgb_list.append(color_palette[raw_list[index]])
        except KeyError:
            print_error('Error in pixel '+str(index-1))
            print_error(str(raw_list[index])+' is not a valid color')
            
        index = index + 1
print('Processing...')
decode()

image = Image.new('RGB', (width, height))
pixels = image.load()
for y in range(height):
        for x in range(width):
            try:
                rgb = tuple(int(rgb_list[x + y * width][i:i+2], 16) for i in (1, 3, 5))
            except (ValueError, IndexError):
                print_error('Eroor in pixel X='+str(x)+', Y='+str(y))
                print_error('No pixel data. Missing pixel will be filled in with a black pixel')
                print('')
                rgb = (0,0,0)
            pixels[x, y] = rgb
image.show()
