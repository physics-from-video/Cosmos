Set up environment
```bash
module load 2023
module load Anaconda3/2023.07-2
cd models/Cosmos
conda env create -f cosmos_env.yml
source activate cosmos_env
uv pip install -r requirements.txt
```

Donwload weights

```bash
PYTHONPATH=$(pwd) python cosmos1/scripts/download_diffusion.py --model_sizes 7B --model_types Video2World --checkpoint_dir /scratch-shared/${USER}/weights/
```

Inference
```bash
PYTHONPATH=$(pwd) python cosmos1/models/diffusion/inference/video2world.py \
  --checkpoint_dir /scratch-shared/${USER}/weights/ \
  --diffusion_transformer_dir Cosmos-1.0-Diffusion-7B-Video2World \
  --num_input_frames 1 \
  --video_save_name "/home/${USER}/VGMs/generated_videos/Cosmos/plain/falling_ball" \
  --input_image_or_video_path /home/${USER}/VGMs/prompts/reference_images/falling_ball.png \
  --prompt Orange ping-pong ball falling down and making impact with the table surface below.
```

Had to download:

```bash
uv pip install pynvml attrs
```

Then got:

```bash
subprocess.CalledProcessError: Command 'ldconfig -p | grep 'libnvrtc'' returned non-zero exit status 1.
```