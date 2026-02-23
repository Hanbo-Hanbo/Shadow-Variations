import os
import random
import shutil

# Root directory containing the original 'bird', 'dog', and 'snake' folders
source_root = "shadow" 
# Target directory for the partitioned dataset
destination_root = "Dataset_Final"

# Allocation ratios for the dataset partition
train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1

categories = ['bird', 'dog', 'snake']

for label in categories:
    # Construct target physical directory structure
    os.makedirs(os.path.join(destination_root, 'train', label), exist_ok=True)
    os.makedirs(os.path.join(destination_root, 'val', label), exist_ok=True)
    os.makedirs(os.path.join(destination_root, 'test', label), exist_ok=True)
    
    # Define source path and verify existence
    current_source_path = os.path.join(source_root, label)
    if not os.path.exists(current_source_path):
        print(f"Warning: Source directory not found at {current_source_path}. Skipping...")
        continue
    
    # Retrieve and shuffle file list to ensure randomized distribution
    all_images = [f for f in os.listdir(current_source_path) if os.path.isfile(os.path.join(current_source_path, f))]
    random.shuffle(all_images)
    
    # Calculate split indices based on defined ratios
    total_files = len(all_images)
    train_idx = int(total_files * train_ratio)
    val_idx = train_idx + int(total_files * val_ratio)
    
    # Map files to their respective subsets
    train_subset = all_images[:train_idx]
    val_subset = all_images[train_idx:val_idx]
    test_subset = all_images[val_idx:]
    
    # Execute physical file transfers
    for filename in train_subset:
        shutil.copy(os.path.join(current_source_path, filename), os.path.join(destination_root, 'train', label, filename))
    for filename in val_subset:
        shutil.copy(os.path.join(current_source_path, filename), os.path.join(destination_root, 'val', label, filename))
    for filename in test_subset:
        shutil.copy(os.path.join(current_source_path, filename), os.path.join(destination_root, 'test', label, filename))

print("Execution Successful: Dataset has been partitioned into Train, Val, and Test sets.")