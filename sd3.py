import requests
import os
import sys
from time import sleep

API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
API_TOKEN = "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"

def generate_image(prompt, output_dir="output"):
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    payload = {"inputs": prompt}

    # Make API request
    print("[*] Generating image... This may take a moment.")
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        print("[+] Image generated successfully!")
        save_image(response.content, prompt, output_dir)
    else:
        print(f"[!] Failed to generate image: {response.status_code} - {response.text}")

def save_image(image_content, prompt, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_name = f"{prompt.replace(' ', '_')[:50]}.png"
    file_path = os.path.join(output_dir, file_name)
    
    with open(file_path, "wb") as img_file:
        img_file.write(image_content)
    
    print(f"[+] Image saved to {file_path}")

def main():
    print_ascii_art()
    print("=== Advanced Ai Text To Image Generation ===")
    print("[INFO] Powered by Stable Diffusion AI")
    print("Developed by: Marttin Saji")
    print("Contact: martinsaji26@gmail.com | UAE Phone: +971")

    while True:
        prompt = input("\nEnter a text prompt (or type 'exit' to quit): ").strip()
        if prompt.lower() == 'exit':
            print("[*] Exiting the program.")
            break
        
        generate_image(prompt)

def print_ascii_art():
    ascii_art = r"""
      
░██████╗████████╗░█████╗░██████╗░██╗░░░░░███████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
╚█████╗░░░░██║░░░███████║██████╦╝██║░░░░░█████╗░░
░╚═══██╗░░░██║░░░██╔══██║██╔══██╗██║░░░░░██╔══╝░░
██████╔╝░░░██║░░░██║░░██║██████╦╝███████╗███████╗
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝

██████╗░██╗███████╗███████╗██╗░░░██╗░██████╗██╗░█████╗░███╗░░██╗
██╔══██╗██║██╔════╝██╔════╝██║░░░██║██╔════╝██║██╔══██╗████╗░██║
██║░░██║██║█████╗░░█████╗░░██║░░░██║╚█████╗░██║██║░░██║██╔██╗██║
██║░░██║██║██╔══╝░░██╔══╝░░██║░░░██║░╚═══██╗██║██║░░██║██║╚████║
██████╔╝██║██║░░░░░██║░░░░░╚██████╔╝██████╔╝██║╚█████╔╝██║░╚███║
╚═════╝░╚═╝╚═╝░░░░░╚═╝░░░░░░╚═════╝░╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝

██╗░░░██╗██████╗░
██║░░░██║╚════██╗
╚██╗░██╔╝░█████╔╝
░╚████╔╝░░╚═══██╗
░░╚██╔╝░░██████╔╝
░░░╚═╝░░░╚═════╝░
    """
    print(ascii_art)

if __name__ == "__main__":
    if "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" in API_TOKEN:
        print("[!] Please replace 'API' with a valid Hugging Face API token.")
        sys.exit(1)
    
    try:
        main()
    except KeyboardInterrupt:
        print("\n[*] Exiting the program.")
