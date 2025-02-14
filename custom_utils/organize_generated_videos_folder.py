import os
import shutil

def organize_videos(base_directory):
    # Iterate through all files in the base directory
    for root, dirs, files in os.walk(base_directory):
        # Initialize folder_num
        folder_num = None
        
        # Handle the DynamiCrafter directory structure first
        if 'samples_separate' in root:
            # Extract the folder number from the parent directory name
            # e.g., "4/dynamicrafter_512_seed4/samples_separate" should get "4"
            path_parts = root.split(os.sep)
            folder_num = path_parts[-3]  # Get the number directory (two levels up from samples_separate)
        else:
            # Handle the original structure
            current_folder = os.path.basename(root)
            if current_folder.isdigit():
                folder_num = current_folder
        
        # Only process files if we have a valid folder number
        if folder_num is not None:
            for file in files:
                if file.endswith('.mp4'):
                    # Extract the system name from the folder path
                    system_name = root.split(os.sep)[-2]  # Gets 'holonomic_pendulum' from the path
                    new_file_name = f"{system_name}_{folder_num}.mp4"
                    # Move the video file to the base directory with the new name
                    shutil.copy(os.path.join(root, file), os.path.join(base_directory, new_file_name))
                
                elif file == 'config.json':
                    # Create the new config filename using the folder number
                    new_config_name = f"config_{folder_num}.json"
                    # Copy the config file to the base directory with the new name
                    shutil.copy(os.path.join(root, file), os.path.join(base_directory, new_config_name))

# Call the function with the base directory
organize_videos('projectile_DunamiCrafter')