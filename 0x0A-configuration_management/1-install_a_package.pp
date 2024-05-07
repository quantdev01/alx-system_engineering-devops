# Installing a package

package { ['Flask', 'Werkzeug']:
	ensure => '2.1.0',
	provider => 'pip3',
}
