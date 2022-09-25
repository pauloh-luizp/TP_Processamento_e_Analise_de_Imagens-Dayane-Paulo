
from PIL import Image
  
# Create an image as input:
input_image = Image.new(mode="RGB", size=(400, 400),
                        color="blue")
  
# save the image as "input.png"
#(not mandatory)
input_image.save("input", format="png")
  
# Extracting pixel map:
pixel_map = input_image.load()
  
# Extracting the width and height
# of the image:
width, height = input_image.size


for i in range(width):
  for j in range(height):
    # getting the RGB pixel value.
    r, g, b = input_image.getpixel((i, j))
      
    # Apply formula of grayscale:
    grayscale = (0.299*r + 0.587*g + 0.114*b)

    # setting the pixel value.
    pixel_map[i, j] = (int(grayscale), int(grayscale), int(grayscale))

    print(pixel_map[i,j])