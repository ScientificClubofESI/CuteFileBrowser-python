
CuteFileBrowser-python
======

What is this ?
------

This is the same app as CuteFileBrowser written in Python instead of PHP with some improvements

https://tutorialzine.com/2014/09/cute-file-browser-jquery-ajax-php

Why Python instead of PHP?
------
Look at the image provided:
![before_after_image](https://github.com/delneg/noteshrinker-django/blob/master/example/before_after.jpg?raw=true "Before-After")
Better resolution is available in the "example" folder of this repo. It is not perfect example, it is the one done with the defaults,
yet it can be made better by tweaking settings.

How does it look like?
------
![ui](https://github.com/delneg/noteshrinker-django/blob/master/example/ui.jpg?raw=true "UI")
How do i launch it?
------

First of all, get python 3 & then get pip.

1. [Python 3](https://www.python.org/downloads/)
2. [Pip](https://pip.pypa.io/en/stable/installing/)
3. Then, ```pip install flask```
4. Then, clone this repo (attention! it will be cloned to the current directory, so make sure you do it in some kinda documents or special one) ```git clone https://github.com/ScientificClubofESI/CuteFileBrowser-python/ ```
5. Then, ```cd CuteFileBrowser-python```
6. Tweak the path inside the ```Assets/js/script.js``` in line :
```http://127.0.0.1:5000/Program Files``` means ```C:\Program Files```
7. Finally,  from the root directory of the project ```python folder.py```
8. Open the index.html file


Improvements
------
.Added the ability to call the script multiple times in the same page
.Ignores hidden files and ```desktop.ini``` file
.Can go throw protected folders 

Future features
------
.PDF, JPG viewer
.Fixing folder items number
.Folder size
.Downloading full folder

License
------
MIT

Contribution
------
Feel free to contribute.
