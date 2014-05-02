

StartFragment**
# Documentation and APIs
CMPE272, Group 6, Photography Social Network


# Page

## Home - done, could improve the links in nav bar

<table><tbody><tr><td>Home

</td><td>Content

</td><td>Note

</td></tr><tr><td>Path

</td><td>GET: <root>/

</td><td>  
</td></tr><tr><td>Template

@when login

</td><td>feed.html

</td><td>  
</td></tr><tr><td>Template

@when not login

</td><td>explore.html

</td><td>  
</td></tr></tbody></table>

  

## Explore - done - could improve the filter icons, filter.active, minor bug w/ active->inactive of filter icon/button-fixed (Jennifer)

<table><tbody><tr><td>Explore

</td><td>Content

</td><td>Note

</td></tr><tr><td>Path

</td><td>GET: <root>/explore/

</td><td>  
</td></tr><tr><td>Template

</td><td>explore.html

</td><td>  
</td></tr></tbody></table>

  

## Feed - done, but more info could be added/shown(Jennifer), crop photo issue

<table><tbody><tr><td>Feed

</td><td>Content

</td><td>Note

</td></tr><tr><td>requirement

</td><td>@login required

</td><td>  
</td></tr><tr><td>Path

</td><td>GET: <root>/feed/

</td><td>  
</td></tr><tr><td>Template

</td><td>feed.html

</td><td>  
</td></tr></tbody></table>

  

## User - done - photo list design to a different style, style the user info panel (Jennifer)

<table><tbody><tr><td>User

</td><td>Content

</td><td>Note

</td></tr><tr><td>Path

</td><td>GET: <root>/user/<user_id>/

</td><td>  
</td></tr><tr><td>Template

</td><td>user_page.html

</td><td>  
</td></tr></tbody></table>

  

## User follows & followers -modal window in user page (xiaoli)

<table><tbody><tr><td>User

</td><td>Content

</td><td>Note

</td></tr><tr><td>Path

</td><td>GET: <root>/user/<user_id>/

</td><td>  
</td></tr><tr><td>Template

</td><td>user_page.html

</td><td>  
</td></tr></tbody></table>

  

## Photo-Detail - restyled, done - could improve style 

<table><tbody><tr><td>Photo-Detail

</td><td>Content

</td><td>Note

</td></tr><tr><td>Path

</td><td>GET: <root>/photo/<photo_id>/

</td><td>  
</td></tr><tr><td>Template

</td><td>photo_page.html

</td><td>  
</td></tr></tbody></table>

  

## Signup - done - could improve style with bootstap

<table><tbody><tr><td>Signup

</td><td>Content

</td><td>Note

</td></tr><tr><td>Path

</td><td>GET: <root>/signup/

</td><td>  
</td></tr><tr><td>Template

</td><td>registration/signup.html

</td><td>  
</td></tr></tbody></table>

  

## Login - done - could improve style with bootstap

<table><tbody><tr><td>Login

</td><td>Content

</td><td>Note

</td></tr><tr><td>Path

</td><td>GET: <root>/login/

</td><td>  
</td></tr><tr><td>Template

</td><td>registration/login.html

</td><td>  
</td></tr></tbody></table>

  

## Upload Photo- almost done - need to deal with process exposure time 1/200 (xiaoli)

<table><tbody><tr><td>Upload Photo

</td><td>Content

</td><td>Note

</td></tr><tr><td>requirement

</td><td>@login required

</td><td>  
</td></tr><tr><td>Path

</td><td>GET: <root>/upload/

</td><td>  
</td></tr><tr><td>Template

</td><td>upload.html

</td><td>  
</td></tr></tbody></table>

  

## Edit Photo - working on
*TO_DO


## Edit Profile -- done basic function, need modal window for change headshot (xiaoli)

<table><tbody><tr><td>Edit Profile

</td><td>Content

</td><td>Note

</td></tr><tr><td>requirement

</td><td>@login required

</td><td>  
</td></tr><tr><td>Path

</td><td>GET: <root>/edit_profile

</td><td>  
</td></tr><tr><td>Template

</td><td>profile.html

</td><td>  
</td></tr></tbody></table>

  

## Find Friends done basic fucntions and styles, improve styling(Jennifer)

<table><tbody><tr><td>Find Friends

</td><td>Content

</td><td>Note

</td></tr><tr><td>requirement

</td><td>@login required

</td><td>  
</td></tr><tr><td>Path

</td><td>GET: <root>/find/

</td><td>  
</td></tr><tr><td>Template

</td><td>find_friends.html

</td><td>  
</td></tr></tbody></table>

  

## Site Statistics - done basic show data,visualization(sammie)

<table><tbody><tr><td>Site Statistics

</td><td>Content

</td><td>Note

</td></tr><tr><td>Path

</td><td>GET: <root>/stat/

</td><td>  
</td></tr><tr><td>Template

</td><td>site_stat.html

</td><td>  
</td></tr></tbody></table>

  
  
  

# Page_Block

## Base
Template: base.html


## Comment
*TO_DO

  
  

# API

## Signup
@If Loggedin

Redirect Page(Home)


### POST: <host>/signup/

<table><tbody><tr><td>Param

</td><td>Validation

</td><td>Description

</td></tr><tr><td>username

</td><td><30, [a-z][0-9]@/./+/-/_ 

</td><td>  
</td></tr><tr><td>password1

</td><td><30

</td><td>  
</td></tr><tr><td>password2

</td><td>same as password1

</td><td>  
</td></tr></tbody></table>

.Success: Redirect Page(Home)

.Failed: Redirect Page(Signup)


## Login
@If Loggedin

Redirect Page(Home)


### POST: <host>/login/
  

<table><tbody><tr><td>Param

</td><td>Validation

</td><td>Description

</td></tr><tr><td>username

</td><td><30, [a-z][0-9]@/./+/-/_ 

</td><td>  
</td></tr><tr><td>password

</td><td><30

</td><td>  
</td></tr></tbody></table>

.Success: Redirect Page(Home)

.Failed: Redirect Page(Login)

  

## Logout
GET: <host>/logout/

Return Redirect Page(Home)

  

## Profile -- working on
*TO_DO


## Follow (AJAX)
Allow: GET, POST, OPTIONS

GET or POST: /api/users/<user_id>/follow


## Unfollow (AJAX)
Allow: GET, POST, OPTIONS

GET or POST: /api/users/<user_id>/unfollow

  

## Comment
*TO_DO


## Like
*TO_DO


## Photo (Restful API)
Allow: GET, POST, HEAD, OPTIONS


### GET /api/photos/
Description: get a list of photos with filtering.

  

<table><tbody><tr><td>Parameter

</td><td>Example

</td><td>Description

</td></tr><tr><td>me

</td><td>/api/photos/?me

</td><td>photos by me

</td></tr><tr><td>feed

</td><td>/api/photos/?feed

</td><td>photos user following

</td></tr><tr><td>page

</td><td>/api/photos/?page=2

</td><td>specify page number

</td></tr><tr><td>ordering

</td><td>/api/photos/?ordering=title, /api/photos/?ordering=-iso // ‘-’ to reverse

</td><td>specify ordering

</td></tr><tr><td>author

</td><td>/api/photos/?author=1

</td><td>filter author by id

</td></tr><tr><td>make

</td><td>/api/photos/?make=Canon

</td><td>filter by camera make

</td></tr><tr><td>portrait

</td><td>/api/photos/?portrait=True

</td><td>show only portrait

</td></tr><tr><td>landscape

</td><td>/api/photos/?landscape=True

</td><td>show only landscape

</td></tr><tr><td>telephoto

</td><td>/api/photos/?telephoto=True

</td><td>show only telephoto

</td></tr><tr><td>low_light

</td><td>/api/photos/?low_light=True

</td><td>show only low_light

</td></tr><tr><td>high_speed

</td><td>/api/photos/?high_speed=True

</td><td>show only high_speed

</td></tr><tr><td>long_exposure

</td><td>/api/photos/?long_exposure=True

</td><td>show only long_exposure

</td></tr></tbody></table>

  

### .Success
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

  

## Site Statistics (AJAX)
GET /api/photos/stat

Allow: OPTIONS, GET


### .Success
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

  
  

## User Statistics (AJAX)
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

  

## User List (Restful API)
  

<table><tbody><tr><td>Parameter

</td><td>Example

</td><td>Description

</td></tr><tr><td>username

</td><td>/api/users/?username=tuolei

</td><td>find specific user

</td></tr><tr><td>find

</td><td>/api/users/?find

</td><td>find user

</td></tr><tr><td>fav_make

</td><td>/api/photos/?find&fav_make

</td><td>use with find

</td></tr><tr><td>fav_model

</td><td>/api/photos/?find&fav_model

</td><td>use with find

</td></tr><tr><td>fav_category

</td><td>/api/photos/?find&fav_category

</td><td>use with find

</td></tr></tbody></table>

  
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

  
  
**EndFragment

