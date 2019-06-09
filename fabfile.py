from fabric import task, Connection

@task
def deploy(c):
    c = Connection(
        host="155.138.213.155",
        user="kriz",
    )
    result = c.run('make -C /home/kriz/src deploy', pty=True)
