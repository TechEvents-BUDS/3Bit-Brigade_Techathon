from PIL import Image, ImageDraw, ImageFont
import time

# List of image file paths and their labels (healthy or diseased) with descriptions
image_files = [
    ("tomato disease.jpg", "Diseased Tomato", "This tomato plant is suffering from a common disease. You can improve its health by removing infected leaves, using fungicides, and ensuring proper watering practices."),
    ("healthy tree.jpg", "Healthy Tree", "This tree is healthy. Ensure it continues receiving adequate sunlight, water, and regular pruning to maintain its good health.")
]

def add_label_to_image(image_path, label, description):
    """Open an image, add a label and description in a separate text box, and display it."""
    try:
        # Open the image from the file path
        img = Image.open(image_path)

        # Add a label to the image (if needed)
        draw = ImageDraw.Draw(img)
        
        # Font size for the label and description
        try:
            label_font = ImageFont.load_default()
            description_font = ImageFont.truetype("arial.ttf", size=20)  # Larger font for description
        except IOError:
            label_font = None
            description_font = ImageFont.load_default()
        
        # Position to place the label text
        label_position = (10, 10)  # Top-left corner for the label
        
        # Position to place the description text box
        description_box_position = (10, 50)  # Start of the box for the description
        box_width = img.width - 20  # Width of the text box
        box_height = 100  # Height of the text box

        # Draw the background box for the description
        draw.rectangle([description_box_position, (box_width, description_box_position[1] + box_height)], fill=(0, 0, 0, 128))

        # Add the label text (plant status)
        draw.text(label_position, label, font=label_font, fill="white")
        
        # Add the description text in the separate text box
        draw.text((description_box_position[0] + 10, description_box_position[1] + 10), description, font=description_font, fill="white")

        # Display the image with the label and description
        img.show()  # This will open the image with the label and description in a box
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")

def main():
    """Main function to display images with labels and descriptions in separate text boxes one by one."""
    for file_path, label, description in image_files:
        print(f"Displaying image from: {file_path} with label: {label}")
        add_label_to_image(file_path, label, description)
        
        # Wait for 5 seconds before displaying the next image
        time.sleep(5)

if __name__ == "__main__":
    main()
