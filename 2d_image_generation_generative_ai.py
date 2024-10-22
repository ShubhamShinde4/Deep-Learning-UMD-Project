import openai
import requests

# Put your OpenAI API key here
# openai.api_key = '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'


# Function to generate and save an image based on text description
def generate_image_from_text_openai(text_description, output_path):
    # Your OpenAI API key (ensure to keep it secure and not expose in shared code)
    openai.api_key = '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'

    try:
        # Create an image using the OpenAI API
        response = openai.Image.create(
            prompt=text_description,
            n=1,
            size="1024x1024"
        )

        # Extract the URL of the generated image from the response
        image_url = response['data'][0]['url']

        # Download the imageGive
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            with open(output_path, 'wb') as f:
                f.write(image_response.content)
            print(f"Image saved to {output_path}")
        else:
            print("Failed to download the image.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Main script execution
if __name__ == "__main__":
    # Prompt the user for their image description
    text_description = input("What's on your mind? Describe the image you want: ")
    output_path = "generated_image.png"

    # Call the function to generate and save the image
    generate_image_from_text_openai(text_description, output_path)

