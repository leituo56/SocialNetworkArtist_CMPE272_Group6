Documentation and APIs
CMPE272, Group 6, Photography Social Network
Page
Home - done, could improve the links in nav bar
Home
Content
Note
Path
GET: <root>/


Template
@when login
feed.html


Template
@when not login
explore.html



Explore - done - could improve the filter icons, filter.active, minor bug w/ active->inactive of filter icon/button-fixed (Jennifer)
Explore
Content
Note
Path
GET: <root>/explore/


Template
explore.html



Feed - done, but more info could be added/shown(Jennifer), crop photo issue
Feed
Content
Note
requirement
@login required


Path
GET: <root>/feed/


Template
feed.html



User - done - photo list design to a different style, style the user info panel (Jennifer)
User
Content
Note
Path
GET: <root>/user/<user_id>/


Template
user_page.html



User follows & followers -modal window in user page (xiaoli)
User
Content
Note
Path
GET: <root>/user/<user_id>/


Template
user_page.html



Photo-Detail - restyled, done - could improve style 
Photo-Detail
Content
Note
Path
GET: <root>/photo/<photo_id>/


Template
photo_page.html



Signup - done - could improve style with bootstap
Signup
Content
Note
Path
GET: <root>/signup/


Template
registration/signup.html



Login - done - could improve style with bootstap
Login
Content
Note
Path
GET: <root>/login/


Template
registration/login.html



Upload Photo- almost done - need to deal with process exposure time 1/200 (xiaoli)
Upload Photo
Content
Note
requirement
@login required


Path
GET: <root>/upload/


Template
upload.html



Edit Photo - working on
*TO_DO
Edit Profile -- done basic function, need modal window for change headshot (xiaoli)
Edit Profile
Content
Note
requirement
@login required


Path
GET: <root>/edit_profile


Template
profile.html



Find Friends done basic fucntions and styles, improve styling(Jennifer)
Find Friends
Content
Note
requirement
@login required


Path
GET: <root>/find/


Template
find_friends.html



Site Statistics - done basic show data,visualization(sammie)
Site Statistics
Content
Note
Path
GET: <root>/stat/


Template
site_stat.html





Page_Block
Base
Template: base.html
Comment
*TO_DO


API
Signup
@If Loggedin
Redirect Page(Home)
POST: <host>/signup/
Param
Validation
Description
username
<30, [a-z][0-9]@/./+/-/_ 


password1
<30


password2
same as password1


.Success: Redirect Page(Home)
.Failed: Redirect Page(Signup)
Login
@If Loggedin
Redirect Page(Home)
POST: <host>/login/

Param
Validation
Description
username
<30, [a-z][0-9]@/./+/-/_ 


password
<30


.Success: Redirect Page(Home)
.Failed: Redirect Page(Login)

Logout
GET: <host>/logout/
Return Redirect Page(Home)

Profile -- working on
*TO_DO
Follow (AJAX)
Allow: GET, POST, OPTIONS
GET or POST: /api/users/<user_id>/follow
Unfollow (AJAX)
Allow: GET, POST, OPTIONS
GET or POST: /api/users/<user_id>/unfollow

Comment
*TO_DO
Like
*TO_DO
Photo (Restful API)
Allow: GET, POST, HEAD, OPTIONS
GET /api/photos/
Description: get a list of photos with filtering.

Parameter
Example
Description
me
/api/photos/?me
photos by me
feed
/api/photos/?feed
photos user following
page
/api/photos/?page=2
specify page number
ordering
/api/photos/?ordering=title, /api/photos/?ordering=-iso // ‘-’ to reverse
specify ordering
author
/api/photos/?author=1
filter author by id
make
/api/photos/?make=Canon
filter by camera make
portrait
/api/photos/?portrait=True
show only portrait
landscape
/api/photos/?landscape=True
show only landscape
telephoto
/api/photos/?telephoto=True
show only telephoto
low_light
/api/photos/?low_light=True
show only low_light
high_speed
/api/photos/?high_speed=True
show only high_speed
long_exposure
/api/photos/?long_exposure=True
show only long_exposure

.Success
{
    "count": 2, 
    "next": null, 
    "previous": null, 
    "results": [
        {
            "url": "http://127.0.0.1:8000/api/photos/2/", 
            "id": 2, 
            "author": 1, 
            "authorName": "leituo56", 
            "title": "Ohlone Trail", 
            "file": "/media/uploads/20140422/bb6615f4cfb34e38b378cdd0cfa8a163.jpg", 
            "upload_time": "2014-04-22T09:17:01.460Z", 
            "make": "", 
            "model": "", 
            "exposure_time": 0.0, 
            "fnumber": 0.0, 
            "focal_length": 0.0, 
            "iso": 0, 
            "processing_software": "", 
            "portrait": false, 
            "landscape": false, 
            "telephoto": false, 
            "low_light": false, 
            "high_speed": false, 
            "long_exposure": false
        }, 
        {
            "url": "http://127.0.0.1:8000/api/photos/1/", 
            "id": 1, 
            "author": 1, 
            "authorName": "leituo56", 
            "title": "thanksgiving", 
            "file": "/media/uploads/20140422/7c8f7e660c47497c9320bcbe0d4d1a19.jpg", 
            "upload_time": "2014-04-22T08:41:00.197Z", 
            "make": "Canon", 
            "model": "Canon 400D", 
            "exposure_time": 100.0, 
            "fnumber": 1.4, 
            "focal_length": 150.0, 
            "iso": 8000, 
            "processing_software": "Photoshop", 
            "portrait": true, 
            "landscape": false, 
            "telephoto": true, 
            "low_light": true, 
            "high_speed": false, 
            "long_exposure": true
        }
    ]
}

GET /api/photos/<photo_id>/
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS

{
    "url": "http://localhost:8000/api/photos/1085/", 
    "id": 1085, 
    "author": 35, 
    "authorName": "test_user30", 
    "title": "My Pic Title 999", 
    "file": "/media/init/3.jpg", 
    "upload_time": "2014-04-27T11:34:42.282Z", 
    "make": "Olympas", 
    "model": "D50", 
    "exposure_time": 10.0, 
    "fnumber": 10.0, 
    "focal_length": 20.0, 
    "iso": 100, 
    "processing_software": "Photoshop", 
    "portrait": false, 
    "landscape": true, 
    "telephoto": false, 
    "low_light": false, 
    "high_speed": false, 
    "long_exposure": true
}


POST: /api/photos/
PUT or PATCH: /api/photos/<photo_id>/
@login_required
{
    "title": "", 
    "file": "", 
    "make": "", 
    "model": "", 
    "exposure_time": 0, 
    "fnumber": 0, 
    "focal_length": 0, 
    "iso": 0, 
    "processing_software": ""
}

Site Statistics (AJAX)
GET /api/photos/stat
Allow: OPTIONS, GET
.Success
{
    "category_stat": [
        {
            "name": "low_light", 
            "pct": 0.535483870967742
        }, 
        {
            "name": "long_exposure", 
            "pct": 0.5225806451612903
        }, 
        {
            "name": "telephoto", 
            "pct": 0.5050691244239631
        }, 
        {
            "name": "landscape", 
            "pct": 0.49400921658986174
        }, 
        {
            "name": "high_speed", 
            "pct": 0.47649769585253454
        }, 
        {
            "name": "portrait", 
            "pct": 0.24608294930875577
        }
    ], 
    "make_stat": [
        {
            "count": 394, 
            "make": "Canon", 
            "pct": 0.3631336405529954
        }, 
        {
            "count": 354, 
            "make": "Nikon", 
            "pct": 0.3262672811059908
        }, 
        {
            "count": 337, 
            "make": "Olympas", 
            "pct": 0.3105990783410138
        }
    ], 
    "fav_category": "low_light", 
    "fav_model": "400D", 
    "total": 1085, 
    "fav_make": "Canon", 
    "model_stat": [
        {
            "count": 547, 
            "model": "400D", 
            "pct": 0.504147465437788
        }, 
        {
            "count": 537, 
            "model": "D50", 
            "pct": 0.4949308755760369
        }, 
        {
            "count": 1, 
            "model": "Canon 400D", 
            "pct": 0.0009216589861751152
        }
    ]
}


User Statistics (AJAX)
GET /api/users/<user_id>/stat/
Allow: OPTIONS, GET

{
    "category_stat": [
        {
            "name": "landscape", 
            "pct": 0.5454545454545454
        }, 
        {
            "name": "low_light", 
            "pct": 0.5454545454545454
        }, 
        {
            "name": "long_exposure", 
            "pct": 0.5454545454545454
        }, 
        {
            "name": "telephoto", 
            "pct": 0.45454545454545453
        }, 
        {
            "name": "high_speed", 
            "pct": 0.45454545454545453
        }, 
        {
            "name": "portrait", 
            "pct": 0.18181818181818182
        }
    ], 
    "make_stat": [
        {
            "count": 8, 
            "make": "Nikon", 
            "pct": 0.7272727272727273
        }, 
        {
            "count": 3, 
            "make": "Canon", 
            "pct": 0.2727272727272727
        }
    ], 
    "fav_category": "landscape", 
    "fav_model": "D50", 
    "total": 11, 
    "fav_make": "Nikon", 
    "model_stat": [
        {
            "count": 8, 
            "model": "D50", 
            "pct": 0.7272727272727273
        }, 
        {
            "count": 3, 
            "model": "400D", 
            "pct": 0.2727272727272727
        }
    ]
}

User List (Restful API)

Parameter
Example
Description
username
/api/users/?username=tuolei
find specific user
find
/api/users/?find
find user
fav_make
/api/photos/?find&fav_make
use with find
fav_model
/api/photos/?find&fav_model
use with find
fav_category
/api/photos/?find&fav_category
use with find

GET /api/users/
{
    "count": 104, 
    "next": "http://localhost:8000/api/users/?page=2", 
    "previous": null, 
    "results": [
        {
            "url": "http://localhost:8000/api/users/1/", 
            "id": 1, 
            "username": "leituo56", 
            "works": [
                "http://localhost:8000/api/photos/85/"
            ], 
            "follows": [
                {
                    "about": "This guy is to lazy to introduce him/her self", 
                    "user_id": 2, 
                    "fav_category": "telephoto", 
                    "fav_model": "400D", 
                    "fav_make": "Nikon", 
                    "id": 3
                }, 
                {
                    "about": "This guy is to lazy to introduce him/her self", 
                    "user_id": 15, 
                    "fav_category": "telephoto", 
                    "fav_model": "D50", 
                    "fav_make": "Canon", 
                    "id": 53
                }
            ], 
            "followers": [], 
            "is_follow": false, 
            "fav_make": "Canon", 
            "fav_model": "Canon 400D", 
            "fav_category": "portrait"
        }, 
        {
            "url": "http://localhost:8000/api/users/5/", 
            "id": 5, 
            "username": "test_user0", 
            "works": [
                "http://localhost:8000/api/photos/908/", 
                "http://localhost:8000/api/photos/813/", 
                "http://localhost:8000/api/photos/586/", 
                "http://localhost:8000/api/photos/141/", 
                "http://localhost:8000/api/photos/100/"
            ], 
            "follows": [
                {
                    "about": "This guy is to lazy to introduce him/her self", 
                    "user_id": 6, 
                    "fav_category": "landscape", 
                    "fav_model": "D50", 
                    "fav_make": "Nikon", 
                    "id": 16
                }
            ], 
            "followers": [], 
            "is_follow": false, 
            "fav_make": "Canon", 
            "fav_model": "D50", 
            "fav_category": "landscape"
        }
    ]
}
GET /api/users/<user_id>/
{
    "url": "http://localhost:8000/api/users/5/", 
    "id": 5, 
    "username": "test_user0", 
    "works": [
        "http://localhost:8000/api/photos/908/", 
        "http://localhost:8000/api/photos/813/", 
        "http://localhost:8000/api/photos/586/", 
        "http://localhost:8000/api/photos/141/", 
        "http://localhost:8000/api/photos/100/"
    ], 
    "follows": [
        {
            "about": "This guy is to lazy to introduce him/her self", 
            "user_id": 6, 
            "fav_category": "landscape", 
            "fav_model": "D50", 
            "fav_make": "Nikon", 
            "id": 16
        }
    ], 
    "followers": [], 
    "is_follow": false, 
    "fav_make": "Canon", 
    "fav_model": "D50", 
    "fav_category": "landscape"
}


