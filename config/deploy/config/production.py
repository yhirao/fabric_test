from fabric.api import *

myroot = '/home/soiginta/test/fabric'
env.hosts = ['ec2-52-69-121-227.ap-northeast-1.compute.amazonaws.com']
env.key_filename = [myroot + '/ssh_key/ec2dev']
env.user = 'ec2-user'
env.password = ''
