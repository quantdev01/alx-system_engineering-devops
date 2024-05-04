# Installing a package

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => '/usr/local/bin',
  user    => 'root',
  group   => 'root',
  creates => '/usr/local/lib/python3.8/site-packages/flask',
}

