input_path = "model_data/Human_Dataset_v2_YOLO/test_filtered/_annotations_f.txt"
output_path = "model_data/Human_Dataset_v2_YOLO/test_filtered/_annotations_f_r.txt"

with open(input_path, "r") as f_in, open(output_path, "w") as f_out:
    for line in f_in:
        parts = line.strip().split()
        image_path = parts[0]
        boxes = parts[1:]

        fixed_boxes = []
        for box in boxes:
            coords = box.split(",")[:-1]  # everything except class_id
            fixed_box = ",".join(coords + ["0"])  # reindex class to 0
            fixed_boxes.append(fixed_box)

        f_out.write(f"{image_path} {' '.join(fixed_boxes)}\n")
