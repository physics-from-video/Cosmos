import argparse
from pathlib import Path
from huggingface_hub import snapshot_download

def parse_args():
    parser = argparse.ArgumentParser(description="Download NVIDIA Cosmos-1.0 Video2World 7B Diffusion model")
    parser.add_argument(
        "--checkpoint_dir", 
        type=str, 
        default="checkpoints", 
        help="Directory to save the downloaded checkpoint."
    )
    return parser.parse_args()

def main(args):
    ORG_NAME = "nvidia"
    MODEL_NAME = "Cosmos-1.0-Diffusion-7B-Video2World"
    
    # Create local checkpoints folder
    checkpoints_dir = Path(args.checkpoint_dir)
    checkpoints_dir.mkdir(parents=True, exist_ok=True)

    # Set up download location
    repo_id = f"{ORG_NAME}/{MODEL_NAME}"
    local_dir = checkpoints_dir.joinpath(MODEL_NAME)
    local_dir.mkdir(parents=True, exist_ok=True)

    # Download the model
    print(f"Downloading {repo_id} to {local_dir}...")
    snapshot_download(
        repo_id=repo_id,
        local_dir=str(local_dir),
        local_dir_use_symlinks=False,
        allow_patterns=["README.md", "model.pt", "config.json", "*.jit"]
    )

if __name__ == "__main__":
    args = parse_args()
    main(args) 