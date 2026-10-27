from PIL import Image
import os

def convert_png_to_jpg(input_directory, output_directory, quality=85):
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Iterate over all files in the specified input directory
    for filename in os.listdir(input_directory):
        # Check if the file is a .png
        if filename.lower().endswith('.png'):
            # Define the full path of the .png file
            png_path = os.path.join(input_directory, filename)
            
            # Open the .png image
            with Image.open(png_path) as img:
                # Define the output filename (change the extension to .jpg)
                jpg_filename = os.path.splitext(filename)[0] + '.jpg'
                jpg_path = os.path.join(output_directory, jpg_filename)
                
                # Convert and save the image as .jpg
                img.convert('RGB').save(jpg_path, 'JPEG', quality=quality)
                print(f'Converted {filename} to {jpg_filename} with quality={quality}')

# Specify the input directory containing .png files
input_directory = 'files/background/missionu/1'
# Specify the output directory for .jpg files
output_directory = 'files/background/missionu/2'
# Specify the desired quality (0 to 100)
quality = 85

# Call the function to perform the conversion
convert_png_to_jpg(input_directory, output_directory, quality)
