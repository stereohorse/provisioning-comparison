#!/usr/bin/env fab

from __future__ import with_statement

from fabric.api import env
from fabric.api import run
from fabric.api import roles


# define hosts groups
# in fabric's terminology they are called 'roles'
env.roledefs = {
    'masters': ['vm1', 'vm2', 'vm3']
}


# setup vagrant machines ssh keys
# fabric will try all keys until success
# http://docs.fabfile.org/en/latest/usage/env.html#key-filename
env.key_filename = [
    '../vagrant/.vagrant/machines/vm%d/virtualbox/private_key'
    % (i + 1)
    for i in range(3)
]

# ssh user
env.user = 'vagrant'


# tasks can be constrained to specific roles
@roles('masters')
def hello():
    run('echo hi!')
