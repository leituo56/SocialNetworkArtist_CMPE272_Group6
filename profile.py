from django.http import HttpResponse
from django.template import RequestContext, Template, loader
import MySQLdb

def GetDict(user_id):  
  db = MySQLdb.connect(host="127.0.0.1", # your host, usually localhost
                       user="root", # your username
                        passwd="root", # your password
                        db="cmpe272") # name of the data base 
  cur = db.cursor()
  sql_str1 = "SELECT * FROM profile where id=" + user_id
  print(sql_str1)
  num_rows = cur.execute(sql_str1)# one-row result
  if num_rows != 1:
    pass  # TODO: handle error
  
  row = cur.fetchall()[0]
  # set deault picture
  default = "https://googledrive.com/host/0B8ssFBiAAmi-cUdQMUV5am9nSnc/IMG_7932.JPG"
  dict = {'ID': str(row[0]),
          'name': row[1],
          'career': row[2],
          'sex': row[3],
          'style': row[4],
          'weblink': row[5],
          'profilepic': default if not row[6] else row[6]
         }

  #sql_str_followers='SELECT UserName from profile where ID IN (select Fler_ID from following where USR_ID= %d)' % user_id
  #sql_str_following='SELECT UserName from profile where ID IN (selec USR_ID from following where Fler_ID= %d)' % user_id

  return dict
  
def Index(request):
  t = loader.get_template('profile.html')

  c = RequestContext(request, GetDict(request.GET['user_id']))
  return HttpResponse(t.render(c))
