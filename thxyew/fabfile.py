from fabric.api import local, settings, abort
from fabric.contrib.console import confirm

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
    code_dir = '/srv/django/myproject'
    with cd(code_dir):
        run("git pull")
        run("touch app.wsgi")
