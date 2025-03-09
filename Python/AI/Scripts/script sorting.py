import os
import shutil
general = 'C:\\Users\\zvezd\\3DObjects\\PersonalProjects\\Python\\AI\\Emotion\\Images'
categories = {
    "0": "anger",
    "1": "disgust",
    "2": "fear",
    "3": "neutral",
    "4": "sadness",
    "5": "smile",
    "6": "surprise"
}
for category in categories.values():
    category_path = os.path.join(general, category)
    os.makedirs(category_path, exist_ok=True)
for file in os.listdir(general):
    file_path = os.path.join(general, file)
    if os.path.isfile(file_path) and "_" in file:
        parts = file.split("_")
        if len(parts) > 1:
            emotion_number = parts[1].split(".")[0]
            if emotion_number in categories:
                category = categories[emotion_number]
                destination = os.path.join(general, category, file)
                shutil.move(file_path, destination)