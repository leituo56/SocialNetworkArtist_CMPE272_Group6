#!  /bin/bash
# Run source update.sh to execute

sudo service httpd stop
cd /home/ec2-user/repo/cmpe272/src/
sudo cp -r SocialNwk /var/www/
cd /var/www/SocialNwk

sudo rm db.sqlite3
cd media/uploads/
sudo rm -rf *
cd /var/www/SocialNwk

sudo python manage.py syncdb
sudo chown apache db.sqlite3
sudo python init_data.py
sudo service httpd start