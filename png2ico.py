from PIL import Image

file = Image.open('B3d.png')
new =file.resize((48,48))
new.save('favicon.ico')
