import shutil
from importlib.resources import files
from pathlib import Path
from string import Template



def editKrb5conf(args) -> None:
    
    out = Path.cwd() / "krbsetup"
    out.mkdir(parents=True, exist_ok=True)
    
    dst = render_template
    
    
    
    
    