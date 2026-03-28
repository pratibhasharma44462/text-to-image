import requests

API_TOKEN = "your_huggingface_token_here"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

API_URL = "https://router.huggingface.co/hf-inference/models/runwayml/stable-diffusion-v1-5"

def generate_image(prompt):
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

    if response.status_code == 200:
        with open("generated_image.png", "wb") as f:
            f.write(response.content)
        print("✅ Image generated successfully!")
    else:
        print("❌ Error:", response.text)

prompt = "A futuristic city with neon lights at night, ultra realistic"

generate_image(prompt)

