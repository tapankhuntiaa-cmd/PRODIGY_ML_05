from PIL import Image
import numpy as np
import os

food_folder = "food_images"

calories = {
    "pizza": 285,
    "burger": 295,
    "apple": 95
}

print("Food Recognition and Calorie Estimation")
print("-" * 40)

for image_name in os.listdir(food_folder):
    image_path = os.path.join(food_folder, image_name)

    img = Image.open(image_path)
    img = img.resize((100, 100))

    food_name = image_name.split(".")[0].lower()

    print(f"Food Detected: {food_name.capitalize()}")

    if food_name in calories:
        print(f"Estimated Calories: {calories[food_name]} kcal")
    else:
        print("Calories: Unknown")

    print("-" * 40)