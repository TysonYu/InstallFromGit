# pylint: disable = C0111
from setuptools import setup

with open("README.md", "r") as f:
    DESCRIPTION = f.read()

setup(name="test",
      version="1.0.0",
      author="YU",
      description="CORD-19 Analysis",
      long_description=DESCRIPTION,
      long_description_content_type="text/markdown",
      url="https://github.com/neuml/cord19q",
      project_urls={
          "Documentation": "https://github.com/neuml/cord19q",
          "Issue Tracker": "https://github.com/neuml/cord19q/issues",
          "Source Code": "https://github.com/neuml/cord19q",
      },
      license="MIT License: http://opensource.org/licenses/MIT",
      packages=["cord19q"],
      package_dir={"": "src/python/"},
      keywords="python search embedding machine-learning",
      python_requires=">=3.5",
      entry_points={
          "console_scripts": [
              "cord19q = cord19q.shell:main",
          ],
      },
      install_requires=[
          "tqdm>=4.40.2"
      ],
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3",
          "Topic :: Software Development",
          "Topic :: Text Processing :: Indexing",
          "Topic :: Utilities"
      ])
