#! /usr/bin/env python3
import os
import sys
import tomllib
import argparse 
from pathlib import Path
from krbsetup.setup import setup_local, setup_remote, cleanup
from krbsetup.utils import Host, prepareData, debugMsg

# /etc/hosts 編集
# /etc/krb5.conf編集
# ~/.zshsrcに書き込み　
# 書き込みをクリーンアップする

# 現在いるディレクトリの下にkrbsetupディレクトリを作成
# 



def printBanner():
    Banner = r"""
    __          __                 __                  / \__
    |  |--.----.|  |--.-----.-----.|  |_.--.--.-----.  (    @\___
    |    <|   _||  _  |__ --|  -__||   _|  |  |  _  |  /         O
    |__|__|__|  |_____|_____|_____||____|_____|   __| /   (_____/
                                            |__|     /_____/   U

    Kerberos Environment Setup Tool
    Author : H0td0gd0g
    Version : 1.0.0
    =============================================
    """
    print(Banner)

class KrbParser(argparse.ArgumentParser):
    def print_help(self):
        printBanner()
        super().print_help()


def main():
    # argment
    
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--debug", action="store_true",default=argparse.SUPPRESS, help="Show debug messages")
    
    parser = KrbParser(description="Kerberos Environment Setup Tool")
    parser.add_argument("--debug", action="store_true", help="Show debug messages")
    
    sub = parser.add_subparsers(dest="command")
    sub.required = True
    
    p_setup = sub.add_parser("setup", help="Set up enviroment")
    setup_mode = p_setup.add_subparsers(dest="mode", required=True)
    
    # local setup
    p_setup_local = setup_mode.add_parser("local", parents=[common], help="Set up locally")
    p_setup_local.add_argument("-i", "--ip", help="IP address", required=True)
    p_setup_local.add_argument("-d", "--fqdn", help="Fully Qualified Domain Name", required=True)
    p_setup_local.set_defaults(func=setup_local)
    
    # remote setup
    p_setup_remote = setup_mode.add_parser("remote", parents=[common], help="Set up remote")
    p_setup_remote.add_argument("-i", "--ip", help="IP address", required=True)
    p_setup_remote.set_defaults(func=setup_remote)
    
    p_clean = sub.add_parser("cleanup", parents=[common], help="clean up settings")
    p_clean.set_defaults(func=cleanup)
    
    args = parser.parse_args()
    DEBUG = args.debug
    
    if os.getuid() == 0:
        debugMsg("error", "Running as root is not recommended. Run as a normal user.")
        sys.exit(1)
    
    host: Host = prepareData(args)
    
    # load config file
    configPath = Path(__file__).resolve().parent / "config.toml"
    
    try:
        with open(configPath, "rb") as f:
            config = tomllib.load(f)
    except FileNotFoundError:
        debugMsg("error", "config file not found")
        sys.exit(1)
    except tomllib.TOMLDecodeError as e:
        debugMsg("error", f"Invalid TOML in {configPath}: {e}")
        sys.exit(1)
    debugMsg("debug", f"Loaded config: {configPath}")
    
    
    
    
    args.func(args)
    
    
    
if __name__ == "__main__":
    main()