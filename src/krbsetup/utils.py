from typing import Literal
from dataclasses import dataclass
import argparse
from pathlib import Path

Status = Literal["success", "error", "warning"]
mark = ""

# color section
green  = "\033[32m"
blue   = "\033[34m"
yellow = "\033[33m"
red    = "\033[31m"
reset  = "\033[0m"

DEBUG = False

def debugMsg(status: Status, msg : str) -> None:
    
    colors = {
        "success": green,
        "log": blue,
        "debug": "",
        "error": red,
        "warning": yellow
    }
    match status:
        case "debug":
            mark = "[DEBUG]"
        case "log":
            mark = "*"
        case "success":
            mark = "+"
        case "error":
            mark = "-"
        case "warning":
            mark = "!"
    print(f"{colors[status]}[{mark}]{reset} {msg}")


@dataclass
class Host:
    ip: str
    fqdn: str
    lower_realm: str
    upper_realm: str
    hostname: str

def prepareData(args: argparse.Namespace) -> Host:
    
    host, realm = args.fqdn.split(".", 1)
    
    return Host(
        ip = args.ip,
        fqdn = args.fqdn,
        lower_realm = realm.lower(),
        upper_realm = realm.upper(),
        hostname = host,
    )
    
def print_summary(h: Host, files: list[Path], root_cmds: list[str]) -> None:
    debugMsg("log", "Target")
    print(f"    IP       : {h.ip}")
    print(f"    FQDN     : {h.fqdn}")
    print(f"    Hostname : {h.hostname}")
    print(f"    Realm    : {h.upper_realm}")
    print()
    
    debugMsg("log", "Generated files")

    debugMsg("log", "Generated files")
    for f in files:
        print(f"    {f}")
    print()

    debugMsg("log", "Run the following commands as root:")
    for c in root_cmds:
        print(f"    {c}")
    print()
