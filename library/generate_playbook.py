#!/usr/bin/python

import os

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *

main_directories = ['group_vars', 'host_vars', 'library', 'filter_plugins',
                    'roles']
role_directories = ['tasks', 'handlers', 'templates', 'files', 'vars',
                    'defaults', 'meta']

def generate_playbook(playbook):
    # playbook_path = directory + '/' + name
    # inventory_path = playbook_path + '/' + inventory
    # role_path = path + '/roles/' + role
    # role_directories = role_path + '/' + role_directories
    name, directory, inventory, role = playbook
    if not role:
        role = 'common'
    if not inventory:
        inventory = 'inventory'
    playbook_path = os.path.join(directory, name)
    inventory_path = os.path.join(playbook_path, inventory)
    role_path = os.path.join(playbook_path, 'roles', role)
    if not os.path.exists(inventory_path):
        os.makedirs(inventory_path)
    if not os.path.exists(role_path):
        os.makedirs(role_path)
    else:
        return {"changed": False}

    return {"changed": True}

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

if __name__ == '__main__':
    main()
