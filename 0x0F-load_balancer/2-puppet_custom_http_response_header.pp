#Automate task: Add a custom HTTP header with Puppet
exec { 'command':
   comand => 'apt-get -y update;
   apt-get -y install nginx;
   sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
   sudo service restatrt',
   provider => shell,
}
