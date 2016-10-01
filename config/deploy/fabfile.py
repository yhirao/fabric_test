from fabric.api import *
from fabric.contrib import project, console

myroot = '/path/to/local_project'

def deploy():
    local_path = myroot + '/myapp'
    project_path = '/path/to/remote_project'
    with cd(project_path):
        exclude = ['*.pyc', '*~', '.DS*', '*.swp']
        project.rsync_project(project_path, local_dir=local_path, exclude=exclude)


def develop():
    env.hosts = ['host']
    env.key_filename = ['key_path']
    env.user = 'username'
    env.password = 'pwd'
