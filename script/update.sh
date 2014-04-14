#!  /bin/bash
sudo service httpd stop
cd /home/ec2-user/repo/cmpe272/src/
sudo cp -r SocialNwk /var/www/
cd /var/www/SocialNwk
sudo rm db.sqlite3
sudo python manage.py syncdb
sudo chown apache db.sqlite3
sudo service httpd start