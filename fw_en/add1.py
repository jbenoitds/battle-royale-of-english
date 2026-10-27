from PIL import Image
import os

def rotate_images_in_folder(folder_path):
    # Check if the provided folder path is valid
    if not os.path.isdir(folder_path):
        print(f"The folder path '{folder_path}' does not exist or is not a directory.")
        return

    # Iterate over all files in the directory
    for filename in os.listdir(folder_path):
        # Construct full file path
        old_file_path = os.path.join(folder_path, filename)
        
        # Skip directories
        if os.path.isdir(old_file_path):
            continue
        
        # Process only .png files
        if filename.lower().endswith('.png'):
            # Open the image
            with Image.open(old_file_path) as img:
                # Rotate the image by 180 degrees
                rotated_img = img.rotate(180, expand=True)
                
                # Save the rotated image with the same filename
                rotated_img.save(old_file_path)
                print(f"Rotated and saved '{filename}'")

# Usage
folder_path = 'files/new_enemies/turn'  # Replace with your folder path
rotate_images_in_folder(folder_path)
