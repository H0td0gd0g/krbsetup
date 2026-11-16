#! /usr/bin/env python3

import argparse
from utils import debugMsg

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
    parser = KrbParser(description="Kerberos Environment Setup Tool")
    
    sub = parser.add_subparsers(dest="command")
    sub.required = True
    
    p_setup = sub.add_parser("setup")
    p_setup.add_argument("-i", help="host IP")
    p_setup.add_argument("--FQDN", help="Fully Qualified Domain Name")
    
    
    
    p_clean = sub.add_parser("cleanup")
    
    
    
        
    args = parser.parse_args()
    
    # body
    
    debugMsg("success", "this is success")
    debugMsg("error", "this is error")
    debugMsg("warning", "this is warning")
    
    
    
if __name__ == "__main__":
    main()