sbatch \
    --job-name=falling_ball_regular_video_vid2world_1 \
    vid2world.job \
    --diffusion_transformer_dir "Cosmos-1.0-Diffusion-7B-Video2World" \
    --batch_input_path "cosmos1/models/diffusion/morpheus/falling_ball_prompt_enhanced_with_upsampler_conditioning_video.jsonl" \
    --video_save_folder "outputs/enhanced_with_upsampler_43" \
    --disable_prompt_upsampler \
    --num_input_frames 9 \
    --seed 43


# Examples of prompt upsampling runs to generate a prompt for the video.

sbatch \
    --job-name=falling_ball_prompt_upsampler_1 \
    prompt_upsampling.job \
    --input "A video of a ball falling down. No camera movement or motion at all. Fixed camera pose."


sbatch \
    --job-name=falling_ball_prompt_upsampler_1 \
    prompt_upsampling_video.job \
    --image_or_video_path "./frames_for_generation/falling_ball_09_10_2024/video_0_fps30/videos/frame_160_9.mp4"