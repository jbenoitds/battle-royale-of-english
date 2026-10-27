import os
from PIL import Image, ImageOps

# Get current working directory
parent_dir = 'Autre'

# List all files in the parent directory
all_files = os.listdir(parent_dir)

# Filter out only image files (adjust file extensions as needed)
image_files = [file for file in all_files if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Check if there are at least 10 image files
if len(image_files) < 10:
    print("Error: There are fewer than 10 image files in the directory.")
    exit()

# Select any 10 image files
image_files = image_files[:10]  # Take the first 10 files (you can change the selection logic as needed)

# Full paths to images
image_paths = [os.path.join(parent_dir, filename) for filename in image_files]

# Open all selected images and apply EXIF rotation correction
images = [ImageOps.exif_transpose(Image.open(filename)) for filename in image_paths]

# Get dimensions of the first image
if images:
    width, height = images[0].size

    # Calculate total height for the final image
    total_height = height * len(images)

    # Create a new blank image with the same width and total height
    combined_image = Image.new('RGB', (width, total_height))

    # Paste each image into the combined image
    y_offset = 0
    for img in images:
        combined_image.paste(img, (0, y_offset))
        y_offset += img.height
        print('One done')

    # Resize combined image by 10%
    new_width = int(width * 0.5)  # 10% reduction in width
    new_height = int(total_height * 0.5)  # 10% reduction in height
    resized_image = combined_image.resize((new_width, new_height))

    # Save the combined image as JPG
    combined_image.save(os.path.join(parent_dir, 'combined_image.jpg'), format='JPEG')

    # Save the resized image as JPG
    resized_image.save(os.path.join(parent_dir, 'resized_combined_image.jpg'), format='JPEG')

    print('All done')
else:
    print("Error: No images found in the directory.")
