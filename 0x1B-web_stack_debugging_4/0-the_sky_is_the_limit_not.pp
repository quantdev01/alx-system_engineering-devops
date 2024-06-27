# 0-the_sky_is_the_limit_not.pp

exec { 'increase-nginx-limits':
  command => '/bin/sed -i "s/worker_connections [0-9]*/worker_connections 2048/" /etc/nginx/nginx.conf && /bin/sed -i "s/keepalive_timeout [0-9]*/keepalive_timeout 65/" /etc/nginx/nginx.conf',
  onlyif  => '/usr/bin/grep -q "worker_connections 768" /etc/nginx/nginx.conf',
  notify  => Exec['restart-nginx'],
}

exec { 'restart-nginx':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
}
