#!  /bin/bash
sudo su - root
service httpd stop
cd /home/ec2-user/repo/cmpe272/src/
cp -r SocialNwk /var/www/
cd /var/www/SocialNwk
rm db.sqlite3
python manage.py syncdb
chown apache db.sqlite3
service httpd start
exit