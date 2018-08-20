from fabric.api import local
from fabric.decorators import task


# 使用task装饰器会在fab --list时显示
# 如不增加装饰器则全部显示
@task
def install():
    """Install requirements packages"""
    local("pip install -r ../requirements.txt")


@task
def freeze():
    """Freeze requirements packages"""
    local("pip freeze > ../requirements.txt")


@task
def runserver():
    """Run server"""
    local("python manage.py runserver")


@task
def deploy(para="add file"):
    """upload packages for git"""
    local("git add . && git commit -m \"%s\"" % para)
    local("git push -u origin master")


@task
def tag_version(version):
    """Tag New Version"""
    local("git tag %s" % version)
    local("git push origin %s" % version)


@task
def test():
    """Run Test"""
    local("python manage.py test")


@task
def pep8():
    """Check the project for PEP8 compliance using pep8"""
    local('pep8 .')
