with open("rose.jpg", "rb") as src_file:
  image_bytes = src_file.read()

with open("copy_rose1.jpg", "wb") as dest_file:
  dest_file.write(image_bytes)