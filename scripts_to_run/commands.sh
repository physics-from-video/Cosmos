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
    --job-name=falling_ball_prompt_upsampler_text \
    prompt_upsampling.job \
    --input "Orange ping-pong ball falling down and making impact with the table surface below. Fixed camera view, no camera movement."





sbatch \
    --job-name=falling_ball_prompt_upsampler_text \
    prompt_upsampling.job \
    --input "Orange ping-pong ball falling down and making impact with the table surface below. Fixed camera view, no camera movement."

sbatch \
    --job-name=falling_ball_prompt_upsampler_1 \
    prompt_upsampling_video.job \
    --image_or_video_path "./frames_for_generation/falling_ball_09_10_2024/video_0_fps30/videos/frame_160_9.mp4"





#Text only prompt upsamplers

#falling ball
sbatch \
    --job-name=falling_ball_prompt_upsampler_text \
    prompt_upsampling.job \
    --input "Orange ping-pong ball falling down and making impact with the table surface below. Fixed camera view, no camera movement."

#holonomic pendulum
sbatch \
    --job-name=holonomic_pendulum_prompt_upsampler_text \
    prompt_upsampling.job \
    --input "A single pendullum moving retrogressive back and fourth. At the bottom of a pendullum there is a ball attached to it. The pendullum is holonomic. Fixed camera view, no camera movement."

#non-holonomic pendulum
sbatch \
    --job-name=non_holonomic_pendulum_prompt_upsampler_text \
    prompt_upsampling.job \
    --input "A single pendulum swings smoothly back and forth. The pendulum consists of a thin, dark string, and at the bottom of the string, there is a small  orange ball. The motion of the pendulum is realistic, with slowing at the peaks of its arc and accelerating through the center, simulating gravity's effect.  As the pendulum is non-holonomic, its swing is not perfectly planar, and there might be small, natural deviations in its path as it moves. Fixed camera view, no camera movement."

#double pendulum
sbatch \
    --job-name=double_pendulum_prompt_upsampler_text \
    prompt_upsampling.job \
    --input "Double pendullum, consisting of a purple and an orange segment. Each segment moves independently. Fixed camera view, no camera movement."

#projectile
sbatch \
    --job-name=projectile_prompt_upsampler_text \
    prompt_upsampling.job \
    --input "A single, small 3D-printed ball, dark gray in color, is launched from a plastic, small-scale ramp with a slight upward angle. The ball follows a natural, smooth, arcing trajectory upward and then downward, continuing along that arc until it exits the right side of the video frame. The video should accurately simulate the ball's motion under standard earth gravity, showing a clear parabolic arc. The video should emphasize a smooth and realistic physics-based movement of the ball without any sudden changes in speed. The ball should not bounce or collide with any objects in the scene. Fixed camera view, no camera movement."

