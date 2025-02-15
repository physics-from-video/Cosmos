# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "opencv-python-headless",
# ]
# ///


import cv2
import os
import argparse

def create_video_from_frames(
    start_frame,
    num_frames,
    fps,
    frames_path,
    ):
    # Get the first frame to determine dimensions
    first_frame = cv2.imread(os.path.join(frames_path, f"frame_{start_frame}.png"))
    if first_frame is None:
        raise ValueError(f"Could not read the first frame at {frames_path}/frame_{start_frame}.png")
    
    height, width = first_frame.shape[:2]
    
    # Initialize video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_dir = os.path.join(frames_path, "videos")
    os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist          
    output_path = os.path.join(output_dir, f"frame_{start_frame}_{num_frames}.mp4")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    # Write frames to video
    for frame_num in range(start_frame, start_frame + num_frames):
        frame_path = os.path.join(frames_path, f"frame_{frame_num}.png")
        frame = cv2.imread(frame_path)
        
        if frame is None:
            print(f"Warning: Could not read frame {frame_num}")
            continue
            
        out.write(frame)
    
    # Release the video writer
    out.release()
    print(f"Video saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create video from sequence of frames')
    parser.add_argument('--start_frame', type=int, default=160, help='Starting frame number')
    parser.add_argument('--num_frames', type=int, default=9, help='Number of frames to include')
    parser.add_argument('--fps', type=int, default=30, help='Frames per second for output video')
    parser.add_argument('--frames_path', type=str, 
                       default="/scratch-shared/azadaianchuk/frames_for_generation/falling_ball_09_10_2024/video_0_fps30",
                       help='Path to directory containing frames')
    
    args = parser.parse_args()
    
    create_video_from_frames(
        start_frame=args.start_frame,
        num_frames=args.num_frames,
        fps=args.fps,
        frames_path=args.frames_path,
    )