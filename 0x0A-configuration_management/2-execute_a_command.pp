# execute a command to kill a process

exec { 'killmenow':
  command => '/usr/bin/pkill -f "killmenow"',
  path    => '/usr/bin',
}

