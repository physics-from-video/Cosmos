# Cosmos Installation in an HPC Environment

This guide provides instructions for installing and running Cosmos in a High-Performance Computing (HPC) environment using Apptainer (formerly Singularity).

## Prerequisites

- Access to an HPC system with GPU support (preferably an H100)
- [Apptainer](https://apptainer.org/) installed on the HPC system
- [Hugging Face](https://huggingface.co/) account for model weights access

## Installation Steps

1. Clone the repository:
```bash
git clone git@github.com:NVIDIA/Cosmos.git
cd Cosmos
```

2. Build the Apptainer image:
```bash
sbatch build_image_apptainer.job
```
This will create a `cosmos.sif` file containing the containerized environment.

## Downloading Model Weights

1. Generate a [Hugging Face access token](https://huggingface.co/settings/tokens)
   - Set the token permission to 'Read' (default is 'Fine-grained')
   - Keep your token secure
   - Accept the usage of the https://huggingface.co/mistralai/Pixtral-12B-2409 on the Hugging Face website

2. Configure the download script:
   - Open `download_weight.job`
   - Replace `your_token_here` with your Hugging Face access token:
     ```bash
     HF_TOKEN="your_token_here"
     ```

3. Start the download:
```bash
sbatch download_weight.job
```

The script will download the model weights to `/scratch-shared/${USER}/cosmos-weights` and create a symbolic link in your working directory.

### Expected Directory Structure

After downloading, your weights directory should look like this:
```
checkpoints/
├── Cosmos-1.0-Diffusion-7B-Text2World
│   ├── model.pt
│   └── config.json
├── Cosmos-1.0-Diffusion-14B-Text2World
│   ├── model.pt
│   └── config.json
├── Cosmos-1.0-Diffusion-7B-Video2World
│   ├── model.pt
│   └── config.json
├── Cosmos-1.0-Diffusion-14B-Video2World
│   ├── model.pt
│   └── config.json
├── Cosmos-1.0-Tokenizer-CV8x8x8
│   ├── decoder.jit
│   ├── encoder.jit
│   └── mean_std.pt
├── Cosmos-1.0-Prompt-Upsampler-12B-Text2World
│   ├── model.pt
│   └── config.json
├── Pixtral-12B
│   ├── model.pt
│   ├── config.json
└── Cosmos-1.0-Guardrail
    ├── aegis/
    ├── blocklist/
    ├── face_blur_filter/
    └── video_content_safety_filter/
```

## Running Demos

### Text2World Generation (Currently this is the model we have tested, there are other models available, have a look at ```cosmos1/models/diffusion/README.md```)

The Text2World model generates world representations from text descriptions. Currently, the demo supports:

- Single and batch generation using the 7B parameter model
- GPU-accelerated inference
- Automatic prompt upsampling

To run the demo:
```bash
sbatch run_demo.job
```

The demo will:
- Use an H100 GPU for computation
- Process inputs from `cosmos1/models/diffusion/assets/v1p0/batch_inputs/text2world.jsonl`
- Save generated outputs to `outputs/Cosmos-1.0-Diffusion-7B-Text2World/`

<div align="center"><b>🚧 Coming Soon 🚧</b></div>

> **Note**: Additional features and improvements are coming soon! Stay tuned for updates.


