import os
import shutil

# === CONFIGURATION ===
TARGET_CLASS_ID = 3  # <-- change this to your desired class ID
INPUT_ANNOTATION_FILE = "model_data/Human_Dataset_v2_YOLO/train/_annotations_.txt"
CLASSES_FILE = "model_data/Human_Dataset_v2_YOLO/train/_classes.txt"
OUTPUT_ANNOTATION_FILE = "model_data/Human_Dataset_v2_YOLO/train_filtered/_annotations_f.txt"
OUTPUT_IMAGE_DIR = "model_data/Human_Dataset_v2_YOLO/train_filtered"

# === Create output directory if it doesn't exist ===
os.makedirs(OUTPUT_IMAGE_DIR, exist_ok=True)

# === Read class names (optional step to extract class name) ===
with open(CLASSES_FILE, "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Extract the class name for the selected class ID
try:
    target_class_name = classes[TARGET_CLASS_ID]
except IndexError:
    raise ValueError(f"Class ID {TARGET_CLASS_ID} not found in {CLASSES_FILE}!")

# === Write filtered classes file (optional) ===
with open("model_data/Human_Dataset_v2_YOLO/train_filtered/_classes.txt", "w") as f:
    f.write(f"{target_class_name}\n")

print(f"Filtering dataset to only include class: {target_class_name} (ID {TARGET_CLASS_ID})")

# === Filter dataset ===
filtered_count = 0
skipped_count = 0

with open(INPUT_ANNOTATION_FILE, "r") as f_in, open(OUTPUT_ANNOTATION_FILE, "w") as f_out:
    for line in f_in:
        parts = line.strip().split()
        if len(parts) < 2:
            skipped_count += 1
            continue  # no boxes

        image_path = parts[0]
        boxes = parts[1:]

        # Filter boxes to only the target class
        filtered_boxes = []
        for box in boxes:
            *coords, class_id = box.split(",")
            if int(class_id) == TARGET_CLASS_ID:
                filtered_boxes.append(",".join(coords + [class_id]))

        if filtered_boxes:
            # Copy image to filtered folder
            image_name = os.path.basename(image_path)
            dst_image_path = os.path.join(OUTPUT_IMAGE_DIR, image_name)

            try:
                shutil.copy2(image_path, dst_image_path)
            except FileNotFoundError:
                print(f"⚠️ Image not found: {image_path} (skipping)")
                continue

            # Write to filtered annotation file
            f_out.write(f"{dst_image_path} {' '.join(filtered_boxes)}\n")
            filtered_count += 1
        else:
            skipped_count += 1

print(f"\n✅ Filtering complete.")
print(f" - Kept:    {filtered_count} images with at least one class {TARGET_CLASS_ID} box")
print(f" - Skipped: {skipped_count} images with no valid boxes")
