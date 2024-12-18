import tensorflow as tf
import numpy as np
from PIL import Image
import pygame

# Load a pre-trained MobileNetV2 model with ImageNet weights
model = tf.keras.applications.MobileNetV2(weights="imagenet")

def load_and_preprocess_image(image_path, target_size=(224, 224)):
    """Load and preprocess the image using PIL."""
    img = Image.open(image_path)
    img = img.resize(target_size)  # Resize to 224x224 for MobileNetV2
    img_array = np.array(img) / 255.0  # Normalize the image
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

def classify_image(img_array):
    """Classify the image and return the label."""
    preds = model.predict(img_array)
    decoded_preds = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)[0][0][1]
    return decoded_preds

def display_with_pygame(image_path, label):
    """Display the image and outputs in a simple layout using Pygame."""
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Tree Health Classification")

    # Load the image and convert it to a Pygame surface
    img = Image.open(image_path).convert("RGB")
    img_width, img_height = img.size
    img_surface = pygame.surfarray.make_surface(np.array(img))

    # Scale the image to fit within the display area
    scale_factor = min((screen_width - 50) / img_width, (screen_height - 200) / img_height)
    new_width, new_height = int(img_width * scale_factor), int(img_height * scale_factor)
    img_surface = pygame.transform.scale(img_surface, (new_width, new_height))

    # Fonts for headings and description
    font_title = pygame.font.SysFont("arial", 32)
    font_text = pygame.font.SysFont("arial", 24)

    # Prepare the description
    description = (
        "This tree is healthy. Ensure adequate sunlight, water, and pruning."
        if label == "Healthy"
        else "This tree is diseased. Remove infected leaves and use fungicides."
    )

    # Main event loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with a white background
        screen.fill((255, 255, 255))

        # Draw the title
        title_surface = font_title.render("Tree Health Classification", True, (0, 0, 0))
        screen.blit(title_surface, ((screen_width - title_surface.get_width()) // 2, 20))

        # Draw the image
        image_x = (screen_width - new_width) // 2
        screen.blit(img_surface, (image_x, 80))

        # Draw the classification result
        result_surface = font_text.render(f"Classification: {label}", True, (0, 0, 0))
        screen.blit(result_surface, (20, new_height + 100))

        # Draw the description
        description_surface = font_text.render(f"Description: {description}", True, (0, 0, 0))
        screen.blit(description_surface, (20, new_height + 140))

        # Update the display
        pygame.display.flip()

    pygame.quit()

def main():
    """Main function to classify and display the tree image."""
    image_path = "defg.jpeg"  # Replace with your image file path

    print(f"Classifying image: {image_path}")

    # Preprocess the image
    img_array = load_and_preprocess_image(image_path)

    # Classify the image
    label = classify_image(img_array)

    # You can refine the decision logic for whether it's healthy or diseased
    # For this example, we map the label to a more general "Healthy" or "Diseased"
    healthy_keywords = ["tree", "oak", "palm", "maple"]
    diseased_keywords = ["wilt", "fungus", "blight", "diseased"]

    # Check if the label contains any keywords for healthy or diseased trees
    label = "Healthy" if any(keyword in label.lower() for keyword in healthy_keywords) else "Diseased"
    
    print(f"Label: {label}")

    # Display the result with Pygame
    display_with_pygame(image_path, label)

if __name__ == "__main__":
    main()
