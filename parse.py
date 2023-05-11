from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import re
import uuid
import os
from io import BytesIO
from PIL import Image


def convert_and_resize_image(image, output_path, size):
    image.putalpha(0)
    image = image.convert('RGB')  # Convert image to RGB format
    image = image.resize(size)  
    image.save(output_path, 'JPEG')  # Save the image as JPEG format

def process_page(url):

    output_str = ""

    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        for img_tag in soup.find_all('img'):
            if 'src' in img_tag.attrs:
                    image_url = img_tag['src']

                    if not "https://" in image_url:
                        image_url = urljoin(url, image_url)  # Handle relative URLs
                    

                    image_response = requests.get(image_url)
                    if image_response.status_code == 200:
                        #print(image_url)

                        image_name = os.path.basename(image_url)
                        #image_uuid = image_name
                        image_uuid = str(uuid.uuid4())

                        try:
                            if not image_url.endswith(".svg"):   
                                image = Image.open(BytesIO(image_response.content))
                                #output_path_jpg = os.path.splitext(output_path)[0] + '.jpg'
                                output_path_jpg = f"./data/images/{image_uuid}.jpg"
                                convert_and_resize_image(image, output_path_jpg, (224, 224))
                                #print('Image downloaded and converted:', output_path_jpg)
                                output_str += f"{output_path_jpg}\n"
                        except:
                            pass
                    else:

                        print('Failed to download image:', image_url)
        
        output_str += "IMAGES_DONE\n"

        text_str = ""
        for text_tag in soup.find_all('p'):
            text_str += f" {text_tag.get_text()}"
        text_str = text_str.replace("\n", " ")

        output_str += text_str


        
        page_uuid = str(uuid.uuid4())

        path = f"./data/pages/{page_uuid}.txt"

        with open(path, "w") as f:
            f.write(output_str)
        print(f"saved web page data: {path}")

    else:
        print('Failed to fetch the web page:', response.status_code)