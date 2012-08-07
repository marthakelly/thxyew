from fabric.api import *
from fabric.colors import green as _green, yellow as _yellow
import boto
import boto.ec2
from config import *
import time

def test():
    with settings(warn_only=True):
        result = local('./manage.py test thxyew_note')
    if result.failed and not confirm('Tests failed. Continue anyway?'):
        abort('Aborting at user request.')

def check():
    local('./manage.py test thxyew_note')

def commit():
    local('git add -p && git commit')

def push():
    local('git push')
    
def pull():
    local('git pull')

def prepare_deploy():
    test()
    commit()
    push()
    
def deploy():
    pass

def create_server():
    """
    Creates EC2 Instance
    """
    print(_green("Started..."))
    print(_yellow("...Creating EC2 instance..."))
    
    conn = boto.ec2.connect_to_region('us-west-2', aws_access_key_id=ec2_key, aws_secret_access_key=ec2_secret)
    image = conn.get_all_images(ec2_amis)
    
    group = conn.get_all_security_groups(groupnames=['quicklaunch-2'])[0]
    group.authorize(ip_protocol='tcp', from_port='22', to_port='22', cidr_ip='0.0.0.0/0')
    group.authorize(ip_protocol='tcp', from_port='80', to_port='80', cidr_ip='0.0.0.0/0')
    
    reservation = image[0].run(1, 1, key_name=ec2_key_pair, security_groups=ec2_security,
        instance_type=ec2_instancetype)
    instance = reservation.instances[0]
    conn.create_tags([instance.id], {"Name":config['INSTANCE_NAME_TAG']})

    while instance.state == u'pending':
        print(_yellow("Instance state: %s" % instance.state))
        time.sleep(10)
        instance.update()

    print(_green("Instance state: %s" % instance.state))
    print(_green("Public dns: %s" % instance.public_dns_name))

    return instance.public_dns_name
    
# install the things
# deploy with github