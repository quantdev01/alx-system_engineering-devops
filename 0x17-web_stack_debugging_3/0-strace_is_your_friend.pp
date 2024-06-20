# 0-strace_is_your_friend.pp
#
# This Puppet manifest ensures Apache and PHP are installed and configures the server to fix the 500 error.

package { 'apache2':
  ensure => installed,
}

package { 'php5':
  ensure => installed,
}

service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => Package['apache2'],
}

file { '/var/www/html/index.php':
  ensure  => file,
  content => '<?php echo "Hello, World!"; ?>',
  require => Package['apache2'],
}

service { 'apache2':
  ensure => running,
  enable => true,
}
