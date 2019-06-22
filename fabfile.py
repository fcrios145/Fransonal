from fabric import task, Connection

@task
def deploy(c):
    c = Connection(
        host="206.189.216.180",
        user="kriz",
    )
    result = c.run('make -C /home/kriz/src deploy', pty=True)
