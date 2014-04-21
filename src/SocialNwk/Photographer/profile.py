from django.http import HttpResponse
from django.template import RequestContext, Template, loader
import MySQLdb

def GetDict(user_id):  
  db = MySQLdb.connect(host="127.0.0.1", # your host, usually localhost
                       user="root", # your username
                        passwd="root", # your password
                        db="cmpe272") # name of the data base 
  cur = db.cursor()
  sql_str = "SELECT * FROM profile where id=" + user_id
  print(sql_str)
  num_rows = cur.execute(sql_str)# one-row result
  if num_rows != 1:
    pass  # TODO: handle error
  
  row = cur.fetchall()[0]

  dict = {'ID': str(row[0]),
          'name': row[1],
          'career': row[2],
          'sex': row[3],
          'style': row[4],
          'weblink': row[5],
          'profilepic': row[6]
         }
  return dict
  


def Index(request):
  t = loader.get_template('profile.html')

  c = RequestContext(request, GetDict(request.GET['user_id']))
  return HttpResponse(t.render(c))
