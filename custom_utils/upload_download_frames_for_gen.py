import argparse
import os

from huggingface_hub import HfApi, login, snapshot_download

def delete_repo(repo_id, token):
    # Initialize HF API with the token
    api = HfApi()
    login(token=token)

    # Delete the entire repository
    try:
        api.delete_repo(
            repo_id=repo_id,
            repo_type="dataset"
        )
        print(f"Successfully deleted repository {repo_id}.")
    except Exception as e:
        print(f"Error deleting repository: {e}")

def upload_frame_data(base_path, repo_id, token, commit_message):
    # Initialize HF API with the token
    api = HfApi()
    login(token=token)

    # Create the dataset repository if it doesn't exist
    try:
        api.create_repo(
            repo_id=repo_id, repo_type="dataset", private=True, exist_ok=True
        )
    except Exception as e:
        print(f"Repository initialization warning (can be ignored if repo exists): {e}")

    # Upload the entire folder at once
    try:
        api.upload_folder(
            repo_id=repo_id,
            repo_type="dataset",
            folder_path=base_path,
            commit_message=commit_message
        )
        print(f"Successfully uploaded folder {base_path}.")
    except Exception as e:
        print(f"Error uploading folder: {e}")

def download_frame_data(repo_id, token, output_dir):
    """
    Download the frames dataset from Hugging Face.
    
    Args:
        repo_id (str): Hugging Face repository ID (username/repo_name)
        token (str): Hugging Face API token
        output_dir (str): Local directory where the dataset will be downloaded
    """
    try:
        # Login with token
        login(token=token)

        # Download the complete repository to specified directory
        snapshot_download(
            repo_id=repo_id,
            repo_type="dataset",
            token=token,
            local_dir=output_dir,
        )
            
        print(f"Successfully downloaded frames to {output_dir}")
    except Exception as e:
        print(f"Error downloading frames: {e}")

def parse_args():
    parser = argparse.ArgumentParser(
        description="Upload or download frames to/from Hugging Face dataset repository."
    )
    
    parser.add_argument(
        "--mode",
        type=str,
        choices=['upload', 'download'],
        required=True,
        help="Whether to upload or download the dataset",
    )

    parser.add_argument(
        "--base_path",
        type=str,
        help="Path to the directory containing the frames.",
    )

    parser.add_argument(
        "--username",
        default="physics-from-video",
        type=str,
        help="Your Hugging Face username.",
    )

    parser.add_argument(
        "--repo_name",
        default="frames-for-generation",
        type=str,
        help="Name of your dataset repository.",
    )

    parser.add_argument(
        "--token",
        type=str,
        required=True,
        help="Hugging Face API token",
    )

    parser.add_argument(
        "--commit_message",
        type=str,
        default="Uploading frames",
        help="Commit message for the upload",
    )

    parser.add_argument(
        "--output_dir",
        type=str,
        help="Directory where to download the dataset (required for download mode)",
    )

    args = parser.parse_args()
    
    # Validate required arguments based on mode
    if args.mode.lower() == 'upload':
        if not args.base_path:
            parser.error("--base_path is required for upload mode")
    elif args.mode.lower() == 'download':
        if not args.output_dir:
            parser.error("--output_dir is required for download mode")
            
    return args

if __name__ == "__main__":
    args = parse_args()
    repo_id = f"{args.username}/{args.repo_name}"
    
    if args.mode.lower() == 'upload':
        upload_frame_data(
            base_path=args.base_path,
            repo_id=repo_id,
            token=args.token,
            commit_message=args.commit_message
        )
    elif args.mode.lower() == 'download':
        os.makedirs(args.output_dir, exist_ok=True)
        download_frame_data(
            repo_id=repo_id,
            token=args.token,
            output_dir=args.output_dir
        )
    else:
        raise ValueError(f"Invalid mode: {args.mode}")

# Example usage for upload:
# python custom_utils/upload_download_frames_for_gen.py --mode upload --base_path frames_for_generation/ --username physics-from-video --repo_name frames_for_generation --token $HF_TOKEN --commit_message "Uploading frames"
# Example usage for download:
# python custom_utils/upload_download_frames_for_gen.py --mode download --username physics-from-video --repo_name frames_for_generation --token $HF_TOKEN --output_dir /path/to/output