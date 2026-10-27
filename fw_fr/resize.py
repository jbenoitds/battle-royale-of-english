from PIL import Image
import os

def resize_images(input_directory, output_directory, new_size):
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Loop through all files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(('.png', '.jpg', '.JPG', '.jpeg', '.bmp', '.gif')):
            # Open an image file
            with Image.open(os.path.join(input_directory, filename)) as img:
                # Resize image
                img = img.resize(new_size, Image.LANCZOS)
                # Save it to the output directory
                img.save(os.path.join(output_directory, filename))
                print(f'resized and saved: {filename}')
    
    print(f"All images have been resized and saved to {output_directory}")

# Example usage
input_dir = 'files/background/missionu/2'
output_dir = 'files/background/missionu/3'
size = (1066, 600)  # New size as a tuple (width, height)

resize_images(input_dir, output_dir, size)
