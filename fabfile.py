from fabric import task, Connection

@task
def deploy(c):
    c = Connection(
        host="155.138.213.155",
        user="kriz",
        connect_kwargs={
            "key_filename": "/home/fcrios/.ssh/id_rsa.pub",
            "passphrase": "40718076",
        },
    )
    result = c.run('make -C /home/kriz/src deploy', pty=True)