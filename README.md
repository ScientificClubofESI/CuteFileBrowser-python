
CuteFileBrowser-python
======

What is this ?
------

This is the same app as CuteFileBrowser written in Python instead of PHP with some improvements

https://tutorialzine.com/2014/09/cute-file-browser-jquery-ajax-php

Why Python instead of PHP?
------
Look at the image provided:
![before_after_image](https://github.com/ScientificClubofESI/CuteFileBrowser-python/raw/master/Preview/Speed_PHP_Python.png?raw=true "Before-After")

How does it look like?
------
![ui](https://github.com/ScientificClubofESI/CuteFileBrowser-python/raw/master/Preview/CuteFileBrowser.jpg "UI")


How do i launch it?
------

First of all, get python 3 & then get pip.

1. [Python 3](https://www.python.org/downloads/)
2. [Pip](https://pip.pypa.io/en/stable/installing/)
3. Then, ```pip install flask```
4. Then, clone this repo (attention! it will be cloned to the current directory, so make sure you do it in some kinda documents or special one) ```git clone https://github.com/ScientificClubofESI/CuteFileBrowser-python/ ```
5. Then, ```cd CuteFileBrowser-python```
6. Tweak the path inside the ```Assets/js/script.js``` in line :

Note: ```http://127.0.0.1:5000/Program Files``` means ```C:\Program Files```
7. Finally, ```python server.py```
8. Open the index.html file

Forcing files to download
------
Browsers open text files instead of downloading them. If you wish to force all files to download, place this .htaccess file in the files folder:
```
<Files *.*>
ForceType application/octet-stream
</Files>
```
It should be called .htaccess (with a leading dot). This file is only supported on Apache web servers.


Improvements
------
1. Added the ability to call the script multiple times in the same page
2. Ignores hidden files and ```desktop.ini``` file
3. Can go throw protected folders 
4. Showing Folder Size

Future features
------
1. Zipping and downloading Folder
2. Recently added Files

License
------
MIT

Contribution
------
Feel free to contribute.
