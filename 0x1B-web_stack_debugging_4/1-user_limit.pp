# 1-user_limit.pp

exec { 'set_user_limits':
  command => 'echo "holberton soft nofile 4096" >> /etc/security/limits.conf && echo "holberton hard nofile 8192\
" >> /etc/security/limits.conf && mkdir -p /etc/systemd/system.conf.d/ && echo "[Manager]\nDefaultLimitNOFILE=8192\
" > /etc/systemd/system.conf.d/limits.conf && systemctl daemon-reload',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'test $(ulimit -n) -lt 8192',
}
