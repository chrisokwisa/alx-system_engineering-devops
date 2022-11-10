# fixes ApacheBench to simulate HTTP requests to a web server
exec {'fixes failed requests':
    command => 'sed -i "s/15/2000/g" /etc/nginx/default',
    path    => '/bin/:sbin/:/usr/bin/:/usr/sbin/',
    onlyif  => 'test -f /etc/default/nginx'
}
