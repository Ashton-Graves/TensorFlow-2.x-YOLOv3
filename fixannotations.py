input_path = "model_data/Human_Dataset_v2_YOLO/train/_annotations.txt"
output_path = "model_data/Human_Dataset_v2_YOLO/train/_annotations_.txt"
image_dir = "model_data/Human_Dataset_v2_YOLO/train"

with open(input_path, 'r') as f_in, open(output_path, 'w') as f_out:
    for line in f_in:
        parts = line.strip().split()
        image_name = parts[0]
        annotations = " ".join(parts[1:])
        fixed_line = f"{image_dir}/{image_name} {annotations}\n"
        f_out.write(fixed_line)
