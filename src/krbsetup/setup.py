from krbsetup.utils import debugMsg
from krbsetup.hosts import editHost
from krbsetup.krb5conf import editKrb5conf



def setup_local(args) -> None:
    debugMsg("log", "start setup local")
    editKrb5conf()
    editHost()


def setup_remote(args) -> None:
    
    editKrb5conf()
    editHost()
    

def cleanup(args) -> None:
    pass