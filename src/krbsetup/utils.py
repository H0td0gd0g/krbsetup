from typing import Literal
from dataclasses import dataclass

Status = Literal["success", "error", "warning"]
mark = ""

# color section
green  = "\033[32m"
blue   = "\033[34m"
yellow = "\033[33m"
red    = "\033[31m"
reset  = "\033[0m"


def debugMsg(status: Status, msg : str) -> None:
    colors = {
        "success": green,
        "log" : "",
        "error": red,
        "warning": yellow
    }
    match status:
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
    higher_realm: str
    hostname: str

def prepareData(args) -> Host: