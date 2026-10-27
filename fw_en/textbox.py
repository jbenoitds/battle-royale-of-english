import os
from PIL import Image

# Directory containing the .jpg images
image_dir_in = 'files/background/missionu/3'
image_dir_out = 'files/background/missionu'
# Height of the white strip to add (in pixels)
white_strip_height = 125

# Process each image in the directory
for filename in os.listdir(image_dir_in):
    image_path = os.path.join(image_dir_in, filename)
    
    # Open the original image
    original_image = Image.open(image_path)
    
    # Get the dimensions of the original image
    width, height = original_image.size
    
    # Create a new image with additional space for the white strip
    new_height = height + white_strip_height
    new_image = Image.new('RGB', (width, new_height), color='white')
    
    # Paste the original image onto the new image
    new_image.paste(original_image, (0, 0))
    
    #### EXCEPTIONAL FOR THIS MISSION, PUT BACK PNG ####
    # Save the new image with the original name followed by ".jpg"
    new_filename = os.path.splitext(filename)[0] + ".jpg"
    new_image_path = os.path.join(image_dir_out, new_filename)
    new_image.save(new_image_path)
    print(f'textbox and saved: {filename}')

print("Processing complete.")
