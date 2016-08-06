sudo apt-get install apache2 php5 mysql-server php5-mysql php-pear
sudo apt-get install php5-curl php5-gd php5-intl php5-xmlrpc
sudo /etc/init.d/apache2 restart
sudo mysql_secure_installation
cd /var/www
wget http://icvc-science.tk/Moodle.tar.gz
tar -xvf Moodle.tar.gz
cd ..
sudo chmod -R 777 www/
cd www/html/
vi config.php