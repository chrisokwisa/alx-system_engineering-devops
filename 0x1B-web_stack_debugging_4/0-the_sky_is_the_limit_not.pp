# 943 requests failed, let’s fix our stack so that we get to 0
exec {'sets file ulimite for nginx':
  command => 'sed -i "s/15/2000/g" /etc/default/nginx',
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/',
  onlyif  => 'test -f /etc/default/nginx'
}
