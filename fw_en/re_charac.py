from PIL import Image
import os

def resize_images_in_folder_and_subfolders(folder_path, new_height):
    # Walk through all subdirectories and files in the given folder
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith('.png'):
                # Construct the full file path
                file_path = os.path.join(root, filename)
                
                # Open the image file
                with Image.open(file_path) as img:
                    # Calculate new width while preserving the aspect ratio
                    aspect_ratio = img.width / img.height
                    new_width = int(new_height * aspect_ratio)
                    
                    # Resize the image
                    new_img = img.resize((new_width, new_height), Image.LANCZOS)
                    
                    # Save the image, overwriting the original file
                    new_img.save(file_path, format='PNG')
                    print(f'Resized and saved: {filename}')

# Example usage
folder_path = 'files/items'
new_height = 50
resize_images_in_folder_and_subfolders(folder_path, new_height)
