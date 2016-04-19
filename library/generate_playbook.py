#!/usr/bin/python

import datetime
import json
import paramiko
import subprocess
import os
import sys

main_directories = ['group_vars','host_vars','library','filter_plugins','roles']
role_directories = ['tasks','handlers','templates','files','vars','defaults','meta']

def generate_playbook(playbook):
    # playbook_path = directory + '/' + name 
    # inventory_path = path + '/' + inventory 
    # role_path = path + '/roles/' + role
    # role_directories = role_path + '/' + role_directories
    name,directory,inventory,role = playbook
    if not role:
        role = "common"
    if not inventory:
        inventory = "inventory"
    if  os.path.exists(path):
        os.makedirs(os.path.join(path,inventory))
    else:
	os.makedirs(path)

    return {"changed" : True}

def main():
    module = AnsibleModule(
        # not checking because of daisy chain to file module
        argument_spec = dict(
            path = dict(required=True, type='path'),
	    name = dict(required=True, type='str'),
	    inventory = dict(required=False, type='str'),
	    role = dict(required=False,type='list'),
        ),
        add_file_common_args = True,
    )
    path = module.params['path']
    inventory = module.params['inventory']
    role = module.params['role']
    name = module.params['name']
    file_args = module.load_file_common_arguments(module.params)
    #if configuration file does not exists
    #    module.fail_json(msg="Source file '%s' is a" % src)
    #else:
    #    playbook = path,inventory,role
    #    module.exit_json(**generate_playbook(playbook))
    playbook = path,name,inventory,role
    module.exit_json(**generate_playbook(playbook))

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *
if __name__ == '__main__':
    main()
