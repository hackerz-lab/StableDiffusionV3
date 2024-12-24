#!/usr/bin/env python3

import os
from diffusers import StableDiffusionPipeline
import torch

# ASCII Art for the Tool
ascii_art = """
   _______ _______  
  /  ___  |  ___  \ 
 /  /  /  | |   |  |
 |  |  |  | |   |  |
 |  |__|  | |___|  |
 \_______/_______/
"""

def main():
    print(ascii_art)
    print("Welcome to the Stable Diffusion AI Tool!")
    print("Developed by Marttin Saji | Contact: martinsaji26@gmail.com")
    
    # Check if GPU is available
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"\nUsing device: {device.upper()}\n")
    
    # Load the Stable Diffusion pipeline
    print("Loading Stable Diffusion model. This may take a moment...")
    try:
        pipeline = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
        pipeline.to(device)
        print("Model loaded successfully!\n")
    except Exception as e:
        print(f"Error loading the model: {e}")
        return

    # Prompt input
    prompt = input("Enter your text prompt: ").strip()
    if not prompt:
        print("Error: Prompt cannot be empty!")
        return

    # Generate the image
    print("\nGenerating your image... Please wait.\n")
    try:
        image = pipeline(prompt).images[0]
        output_path = "output.png"
        image.save(output_path)
        print(f"Image generated successfully and saved as {output_path}")
    except Exception as e:
        print(f"Error generating the image: {e}")

if __name__ == "__main__":
    main()
