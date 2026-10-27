from PIL import Image
import os

# Directory containing your images
input_dir = 'files/background/missionu/1'

# Output directory for cropped images
output_dir = 'files/background/missionu/2'

# Target dimensions after cropping
target_width = 4032
target_height = 2269

# Crop dimensions
crop_top = 378
crop_bottom = 377

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Function to crop and save an individual image
def crop_and_save_image(input_path, output_path):
    image = Image.open(input_path)
    width, height = image.size

    # Calculate crop dimensions
    left = 0
    upper = crop_top
    right = width
    lower = height - crop_bottom

    # Crop the image
    cropped_image = image.crop((left, upper, right, lower))

    # Resize the image to the target dimensions
    resized_image = cropped_image.resize((target_width, target_height), Image.LANCZOS)

    # Save the image as JPG
    resized_image.save(output_path, 'JPEG', quality=95)

# Iterate through each image in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.JPG') or filename.endswith('.jpg'):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename.lower())  # Ensure lowercase extension
        crop_and_save_image(input_path, output_path)
        print(f'Cropped and saved: {filename}')

print('All images cropped and saved.')
