from fabric import task, Connection

@task
def deploy(c):
    c = Connection(
        host="167.99.162.3",
        user="fransonal",
    )
    result = c.run('make -C /home/fransonal/src deploy', pty=True)
