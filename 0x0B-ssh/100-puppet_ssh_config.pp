# Client configration file (w/ Puppet)

$myfile = '/etc/ssh/ssh_config'

file { $myfile:
  ensure  => present,
  content => 'Hostname 54.157.143.24\nPasswordAuthentication no\nHostbasedAuthentication no',
}
