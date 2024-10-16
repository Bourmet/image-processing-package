from setuotools import setup, find_packeges

with open("READ.md","r") as f:
  page_description = f.read()

with open("requirements.txt") as f:
  requirements = f.read().splitlines()

setup(
  name = "img_process_DIO",
  version = "0.0.1",
  author = "Bourmet",
  author_email = "my_email",
  description = "first archive about",
  long_description = page_description,
  long_description_content_type = "text/markdown",
  url = "https://github.com/Bourmet/image-processing-package/blob/master/setup.py"
  packeges = find_packages(),
  install_requires = requirements
  python_requires = '>-3.8',
)
  
