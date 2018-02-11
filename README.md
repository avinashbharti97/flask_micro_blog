# flask_micro_blog

:heavy_check_mark: Idea
----

* After a user logs in they are presented with all of the blog posts.
* Users can add new, text-only blog entries from the	same screen, read the entries themselves, or logout.

## Getting Started
### Prerequisites
    - python3
    - pip3
    - virtualenv
    - flask
### installing Prerequisites
```
$ sudo apt-get install python3 python3-pip virtualenvwrapper
```
### Creating Virtual Enviornment
    * move to the project directory *

```
$ virtualenv -p /usr/bin/python3 env
$ source env/bin/activate
$ pip install flask==0.11.1
```
### Running Project
```
$ python blog.py
```