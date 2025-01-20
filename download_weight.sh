#!/bin/bash
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Error: Missing required arguments"
    echo "Usage: $0 <huggingface_token> <weights_dir>"
    exit 1
fi

HF_TOKEN="$1"
WEIGHTS_DIR="$2"

huggingface-cli login --token "$HF_TOKEN"

# Set PYTHONPATH to the project root directory
export PYTHONPATH="${PWD}:${PYTHONPATH}"

python cosmos1/scripts/download_diffusion.py \
--model_sizes 7B 14B \
--model_types Text2World Video2World \
--checkpoint_dir ${WEIGHTS_DIR}