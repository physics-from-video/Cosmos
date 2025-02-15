import os
import shutil
import argparse

def organize_videos(base_directory):
    # Create output directory
    output_dir = os.path.join(base_directory, 'Cosmos-1.0-Diffusion-7B-Video2World')
    os.makedirs(output_dir, exist_ok=True)
    
    # Create a dictionary to track files per relative path
    files_per_path = {}
    
    # First pass: count files per relative path
    for root, dirs, files in os.walk(base_directory):
        for file in files:
            if file.endswith('.mp4'):
                seed = extract_seed(os.path.join(root, file))
                if seed:
                    relative_path = os.path.relpath(root, base_directory).split(os.sep)[0]
                    files_per_path[relative_path] = files_per_path.get(relative_path, 0) + 1

    # Second pass: organize files
    video_counter = 1
    for root, dirs, files in os.walk(base_directory):
        # Handle video files
        for file in files:
            if file.endswith('.mp4'):
                seed = extract_seed(os.path.join(root, file))
                if seed:
                    relative_path = os.path.relpath(root, base_directory).split(os.sep)[0]
                    
                    # Only add count to filename if there are multiple files in this path
                    if files_per_path[relative_path] > 1:
                        new_file_name = f"{base_directory}_seed_{seed}_count_{video_counter}.mp4"
                    else:
                        new_file_name = f"{base_directory}_seed_{seed}.mp4"
                    
                    # Copy video file
                    shutil.copy(os.path.join(root, file), os.path.join(output_dir, new_file_name))
                    video_counter += 1

        # Handle txt files separately
        for file in files:
            if file.endswith('.txt'):
                seed = extract_seed(os.path.join(root, file))
                if seed:
                    relative_path = os.path.relpath(root, base_directory).split(os.sep)[0]
                    
                    # Use the same naming convention as videos
                    if files_per_path[relative_path] > 1:
                        new_txt_name = f"{base_directory}_seed_{seed}_count_{video_counter}.txt"
                    else:
                        new_txt_name = f"{base_directory}_seed_{seed}.txt"
                    
                    # Copy txt file
                    shutil.copy(os.path.join(root, file), os.path.join(output_dir, new_txt_name))
                    video_counter += 1

def extract_seed(file_path):
    # Extract the seed from the file path
    parts = file_path.replace('\\', '/').split('/')
    
    # Try to find seed in directory names first
    for part in parts:
        if part.startswith('seed_'):
            return part.split('_')[1]
    
    # Look for line_idx in the filename
    for part in parts:
        if 'line_idx_' in part:
            # Extract the number after line_idx_
            try:
                return part.split('line_idx_')[1].split('_')[0]
            except IndexError:
                continue
    
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Organize video files based on their seeds.')
    parser.add_argument('--base_directory', type=str, default='holonomic_pendulum_regular_wo_ps_frames_1', help='Base directory containing the video files')
    
    args = parser.parse_args()
    organize_videos(args.base_directory)