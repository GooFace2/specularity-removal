from distutils.core import setup

setup(
    name='specularity_removal',
    packages=['specularity_removal'],
    version='0.1',
    description='The package is an open source utility to remove specularity in Images captured from multiple viewpoints',
    author='Michael Jaison Gnanasekar, Shreyas Joshi',
    author_email='gmichaeljaison@gmail.com, shreyasvj25@gmail.com',
    url='https://github.com/gmichaeljaison/specularity-removal',
    download_url='https://github.com/gmichaeljaison/specularity-removal/tarball/0.1',
    keywords=['computer vision', 'image processing', 'specularity-removal',
              'highlights', 'homography'],
    classifiers=[],
    requires=['numpy', 'cv2']
)
