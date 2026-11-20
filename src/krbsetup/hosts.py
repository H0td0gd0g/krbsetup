import shlex
from krbsetup.utils import debugMsg, Host


def printHostCmd(h: Host) -> None:
    line = f"{h.ip}\t{h.fqdn} {h.lower_realm} {h.hostname}"
    printf_cmd = ["printf", "%s", line]
    tee_cmd = ["sudo", "tee", "-a", "/etc/hosts"]
    cmd = shlex.join(printf_cmd) + "|" + shlex.join(tee_cmd)
    print(cmd)