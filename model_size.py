import os

model_path = "model_data/mars-small128.pb"  # or .pb or .trt
size_bytes = os.path.getsize(model_path)
size_kb = size_bytes / 1024
size_mb = size_kb / 1024

print(f"Model size: {size_kb:.2f} KB ({size_mb:.2f} MB)")
