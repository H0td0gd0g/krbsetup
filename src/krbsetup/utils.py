from typing import Literal

Status = Literal["success", "error", "warning"]
mark = ""

# color section
blue   = "\033[34m"
yellow = "\033[33m"
red    = "\033[31m"
reset  = "\033[0m"


def debugMsg(status: Status, msg : str) -> None:
    colors = {
        "success": blue,
        "error": red,
        "warning": yellow
    }
    match status:
        case "success":
            mark = "+"
        case "error":
            mark = "-"
        case "warning":
            mark = "!"
    print(f"{colors[status]}[{mark}]{reset} {msg}")