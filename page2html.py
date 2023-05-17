import sys

page_path = sys.argv[1]

with open(page_path, 'r') as f:
    content = f.read()

html = ""

content_split = content.split("IMAGES_DONE")

image_paths = content_split[0].split("\n")


for path in image_paths:
    html += f'<img src="{path}"></img>'

html += content_split[1]

with open(sys.argv[2],'w') as f:
    f.write(html)