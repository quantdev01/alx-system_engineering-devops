# Installing a package

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask',
  path    => '/usr/local/bin',
  creates => '/usr/local/lib/python3.8/site-packages/flask',
}
