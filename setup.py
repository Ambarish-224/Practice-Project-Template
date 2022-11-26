from setuptools import setup

with open("README.md", 'r', encoding= "utf-8") as f:
    long_description = f.read()
    ## IN README.md file we describe detail projects longs describtions )
 
REPO_NAME = "Practice-Project-Template"
AUTHOR_USER_NAME = "Ambarish-224"   
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = []

setup(name = SRC_REPO,
      version = "0.0.1",
      author = AUTHOR_USER_NAME,
      description= "This is our first release",
      long_description= long_description,
      url= f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
      author_email= "ambarish.gaya224@gmail.com",
      packages= [SRC_REPO],
      python_required = ">=3.6",
      install_requires  = LIST_OF_REQUIREMENTS
      )    
    
