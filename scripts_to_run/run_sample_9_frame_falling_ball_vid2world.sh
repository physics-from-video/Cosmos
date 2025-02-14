#!/bin/bash

ACTUAL_SEED=42  # Set a specific seed value
SEED_LIST=($(shuf --input-range=1-10000 --random-source=<(openssl enc -aes-256-ctr -pass pass:"$ACTUAL_SEED" -nosalt </dev/zero 2>/dev/null) -n 1)) # Generate 100 random seeds


NUM_INPUT_FRAMES=9


for SEED in "${SEED_LIST[@]}"; do
    echo "Running with seed: ${SEED}"
    sbatch --job-name=enhanced_falling_ball_single_frame_vid2world_${SEED} sample_single_frame_vid2world.job \
        --diffusion_transformer_dir Cosmos-1.0-Diffusion-7B-Video2World \
        --batch_input_path cosmos1/models/diffusion/assets/v1p0/morpheus/batch_inputs/enhanced_falling_ball_regular_wo_ps.jsonl \
        --video_save_folder enhanced_falling_ball_regular_wo_ps_frames_${NUM_INPUT_FRAMES}/Cosmos-1.0-Diffusion-7B-Video2World/seed_${SEED} \
        --disable_prompt_upsampler \
        --num_input_frames ${NUM_INPUT_FRAMES} \
        --seed ${SEED}
done