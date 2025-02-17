#!/usr/bin/env python3
import subprocess
import random
import argparse
import os


N_RUNS = 5

CONDITIONING = "video" # "video"
EXPERIMENT_NAME = "falling_ball" # "double_pendulum", "projectile", "non-holonomic_pendulum", "holonomic_pendulum"
TYPE = "enhanced_with_upsampler" # "enhanced", "enhanced_with_upsampler"


# Add argument parser
parser = argparse.ArgumentParser(description='Run video2world inference with COSMOS model')
parser.add_argument('--project_dir', 
                    default="/scratch-shared/azadaianchuk/videogen/cosmos", # Change to your project directory
                    help='Project directory containing cosmos.sif and cosmos-weights')

args = parser.parse_args()

JOB_CONTENT = f'''#!/bin/bash 
#SBATCH --partition=gpu_h100
#SBATCH --gpus=1
#SBATCH --gpus-per-node=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --time=00:10:00
#SBATCH --output=./logs/%j-%x.out

set -e 

export PYTHONPATH="${{PWD}}:${{PYTHONPATH}}"

PROJECT_DIR="{args.project_dir}"

IMAGE=${{PROJECT_DIR}}/cosmos.sif

WEIGHTS_DIR=${{PROJECT_DIR}}/cosmos-weights

IMAGES_PATH=/scratch-shared/${{USER}}/frames_for_generation

apptainer exec -B ${{WEIGHTS_DIR}}:${{WEIGHTS_DIR}} -B ${{IMAGES_PATH}}:${{IMAGES_PATH}} --nv ${{IMAGE}} \\
python cosmos1/models/diffusion/inference/video2world.py \\
    --checkpoint_dir ${{WEIGHTS_DIR}} \\
    "$@"
'''

# Create job file on the fly
with open('sample_single_frame_vid2world.job', 'w') as f:
    f.write(JOB_CONTENT)
os.chmod('sample_single_frame_vid2world.job', 0o755)  # Make it executable


random.seed(43)
SEED_LIST = random.sample(range(1, 10001), N_RUNS)  # 5 unique random seeds

if CONDITIONING == "image":
    num_input_frames = 1
elif CONDITIONING == "video":
    num_input_frames = 9

for seed in SEED_LIST:
    print(f"Running with seed: {seed}")
    subprocess.run([
        "sbatch",
        f"--job-name={EXPERIMENT_NAME}_{TYPE}_{CONDITIONING}_vid2world_{seed}",
        "sample_single_frame_vid2world.job",
        "--diffusion_transformer_dir", "Cosmos-1.0-Diffusion-7B-Video2World",
        "--batch_input_path", f"cosmos1/models/diffusion/morpheus/{EXPERIMENT_NAME}_prompt_{TYPE}_conditioning_{CONDITIONING}.jsonl",
        "--video_save_folder", f"outputs/{EXPERIMENT_NAME}_prompt_{TYPE}_conditioning_{CONDITIONING}_cropped/Cosmos-1.0-Diffusion-7B-Video2World/seed_{seed}",
        "--disable_prompt_upsampler", # TODO: figure our if we could actually use it somehow
        "--num_input_frames", str(num_input_frames),
        "--seed", str(seed)
    ]) 


    