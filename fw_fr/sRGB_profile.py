import os
from PIL import Image

def process_images(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.png'):
                input_file = os.path.join(root, filename)
                temp_file = os.path.join(root, 'temp_' + filename)
                
                try:
                    # Open the image file
                    with Image.open(input_file) as img:
                        # Save the image without metadata
                        img.save(temp_file, format='png', icc_profile=None)
                    
                    # Replace the original file with the processed file
                    os.remove(input_file)
                    os.rename(temp_file, input_file)
                    
                    print(f"Processed: {input_file}")
                except PermissionError as e:
                    print(f"Permission error with {input_file}: {e}")
                except Exception as e:
                    print(f"Unexpected error with {input_file}: {e}")

# Specify the top-level directory to start processing
directory = 'files'
process_images(directory)
