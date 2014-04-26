SocialNetworkArtist_CMPE272_Group6
==============

> This is a team project for CMPE272 (Spring 2014)
> at San Jose State University
 - Team 6 project
 - Field: Web Development - Social Network
 - Title: Social Network for Professional Photographers

Directory
-----------
 - Design: Product documentation Link
 - src:	source code
 - script: update script for Tuo Lei's amazon ec2

Installation
-----------
 - Check your Python Version, 2.7.* would be best
```
Python -V
```
 - Install Django 1.6.2, see [django]
 - install Django Rest Framework
 - install Markdown
 - install django-filter
```
pip install Django==1.6.2
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```
 - Check your Django version
```
python -c "import django; print(django.get_version())"
```
 - Modify <your path>/src/SocialNwk/SocialNwk/setting.py if needed, you can use a custome setting. There's no need to commit setting.py unless it's needed.
 - Sync your database. Notice Django do not provide migration, alter table manually if table already exist
```
python manage.py syncdb
```
 - Set a super user for your db
 - You can also run a init data script. This will add 3 sample users: tuolei, xiaolijiang and wenjiazhang, automaticly add 12 sample photos in media/upload/init/
```
python init_data.py
```
 - Run your server
```
python manage.py runserver
```
 - Visit http://127.0.0.1:8000/

Tech
-----------
This work uses a number of open source projects to work properly:

* [django] - The Web framework for perfectionists with deadlines.
* [jQuery] - The Write Less, Do More, JavaScript Library. 
* [django rest framework] -  A powerful and flexible toolkit that makes it easy to build Web APIs.

Team Member
--------------
* Xiaoli Jiang <jiangxiaoli1104@gmail.com>
* Tuo Lei <leituo56@gmail.com>
* Xiumei Lu <sammiexiu@gmail.com>
* Jennifer Wu <jenn.j.wu@gmail.com>
* Wenjia ZHANG <wenjiazhang519@gmail.com>

License
----

MIT

[django]:https://www.djangoproject.com
[jQuery]:http://jquery.com
[django rest framework]:http://www.django-rest-framework.org/
