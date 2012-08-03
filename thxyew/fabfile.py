from fabric.api import local

def test():
    local("./manage.py test thxyew_note")

def commit():
    local("git add -p && git commit")

def push():
    local("git push")

def deploy():
    test()
    commit()
    push()