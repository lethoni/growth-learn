import os

from fabric.api import local
from fabric.decorators import task
from fabric.operations import run, sudo, put
from fabric.state import env
from fabric.context_managers import settings, hide, cd, prefix


circus_file_path = os.path.realpath('deploy/circus.ini')
circus_upstart_file_path = os.path.realpath('deploy/circus.conf')
nginx_config_path = os.path.realpath('deploy/Nginx')
nginx_avaliable_path = "/etc/nginx/sites-available/"
nginx_enable_path = "/etc/nginx/sites-enabled/"
app_path = "~"
virtual_env_path = "~/venv/bin/activate"

env.hosts = ['192.168.3.1']
env.user = 'root'
env.password = '123456'


# 使用task装饰器会在fab --list时显示
# 如不增加装饰器则全部显示
@task
def install():
    """Install requirements packages"""
    local("pip install -r requirements.txt")


@task
def freeze():
    """Freeze requirements packages"""
    local("pip freeze > requirements.txt")


@task
def runserver():
    """Run server"""
    local("python manage.py runserver")


@task
def git_deploy(para="add file"):
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
    local("python manage.py test blog")


@task
def pep8():
    """Check the project for PEP8 compliance using pep8"""
    local('pep8 .')


@task
def e2e():
    """Run E2E Test"""
    local("python manage.py test e2e")

    
@task
def host_type():
    """Get server info"""
    run('uname -a')


@task
def setup():
    """Setup the Ubantu Env"""
    sudo('apt-get update')
    APT_GET_PACKAGES=[
    'build-essential',
    'git',
    'python3-dev',
    'python3-pip',
    'nginx',
    'virtualenv',
    ]
    sudo("apt-get install -y " + " ".join(APT_GET_PACKAGES))
    sudo('pip3 install circus')
    run('virtualenv --distribute -p /usr/bin/python3.5 venv')


@task
def deploy(version):
    """depoly app to cloud"""
    with cd(app_path):
        get_app(version)
        setup_app(version)
        config_app()
        
    nginx_config()
    nginx_enable_site('growth-studio.conf')
    
    circus_config()
    circus_upstart_config()
    
    circus_start()
    nginx_restart()
    

def get_app(version):
    run(('wget ' + "https://codeload.github.com/lethoni/growth-learn/tar.gz/v%s") % version)
    run('tar -xvf v%s' % version)
    

def setup_app(version):
    with cd('~/growth-learn-%s' % version):
        with prefix('source ' + virtual_env_path):
            run('pip3 install -r requirements.txt')
            run('rm -f ../growth-studio')
            run('ln -s growth-learn-%s/growth_studio ../growth-studio' % version)


def config_app():
    with cd('growth-studio'):
        with prefix('source ' + virtual_env_path):
            run('python manage.py collectstatic --noinput')
            run('python manage.py migrate')


def nginx_restart():
    "Reset nginx"
    run("service nginx restart")


def nginx_start():
    "Start nginx"
    run("service nginx start")


def nginx_config(nginx_config_path=nginx_config_path):
    "Send nginx configuration"
    for file_name in os.listdir(nginx_config_path):
        put(os.path.join(nginx_config_path, file_name), nginx_avaliable_path, use_sudo=True)


def circus_config():
    "Send Circus configuration"
    sudo('mkdir -p /etc/circus/')
    put(circus_file_path, '/etc/circus/', use_sudo=True)


def circus_upstart_config():
    "Send Circus Upstart configuration"
    put(circus_upstart_file_path, '/etc/init/', use_sudo=True)


def circus_start():
    "Send Circus Upstart configuration"
    sudo('(/usr/local/bin/circusd /etc/circus/circus.ini --daemon) && sleep 1')


def nginx_enable_site(nginx_config_file):
    "Enable nginx site"
    with cd(nginx_enable_path):
        sudo('rm -f default')
        sudo('rm -f ' + nginx_config_file)
        sudo('ln -s ' + nginx_avaliable_path + nginx_config_file)
