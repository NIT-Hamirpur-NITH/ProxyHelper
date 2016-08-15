#!/usr/bin/python3
import argparse
import subprocess


if __name__ == '__main__':
    home = subprocess.os.environ.get('HOME')

    parser = argparse.ArgumentParser(description='A simple command-line tool to manage proxy settings')
    main_args = parser.add_argument_group()

    main_args.add_argument('-S','--setProxy',action='store_true', 
                        help='Set best proxy automatically')
    main_args.add_argument('-T',
                        '--torPing',
                        help='Perform ping via tor'\
                        +', Helps to keep connection alive',
                        action='store_true')
    main_args.add_argument('-C',
                        '--customProxy',
                        nargs=1,
                        help='Set your own proxy. eg. -C 172.16.24.3:3128') 
    main_args.add_argument('-N',
                        '--clearProxy',
                        action='store_true',
                        help='Reset the system proxy') 
    parser.add_argument('-U',
                        '--update',
                        action='store_true', 
                        help='Update ProxyHelper package')
    main_args.add_argument('-G',
                        '--getProxy',
                        action='store_true', 
                        help='Print the best proxy, but don\'t set it.')
    parser.add_argument('--configure',
                        action='store_true', 
                        help='Configure defaults in proxyhelper')
    parser.add_argument('--manual',
                        action='store_true',
                        help='Enable manual mode')
    parser.add_argument('--auto',
                        action='store_true',
                        help='Enable automatic mode')
    arg = parser.parse_args()

    if arg.setProxy:
        subprocess.call(['bash',
                        '{}/.proxyhelper/zetproxy'.format(home)])
    elif arg.torPing:
        subprocess.call(['python3',
                        '{}/.proxyhelper/torpinger'.format(home)])
    elif arg.customProxy:
        subprocess.call(['bash',
                        '{}/.proxyhelper/zetproxy'.format(home)
                        ,'Proxy',arg.customProxy[0]])
    elif arg.clearProxy:
        subprocess.call(['bash',
                        '{}/.proxyhelper/zetproxy'.format(home),
                        'None'])
    elif arg.getProxy:
        subprocess.call(['python3',
                        '{}/.proxyhelper/surely_parallel.py'.format(home)])
    elif arg.manual:
        subprocess.call('sudo rm /etc/network/if-up.d/zetproxy', shell=True)
        subprocess.call('sudo rm /etc/network/if-up.d/torpinger', shell=True)
    elif arg.auto:
        subprocess.call('sudo cp {}/.proxyhelper/zetproxy /etc/network/if-up.d/'.format(home),shell=True)
        subprocess.call('sudo cp {}/.proxyhelper/torpinger /etc/network/if-up.d/'.format(home),shell=True)
    elif arg.update:
        print('Updating ProxyHelper.')
        # To implement !!
        # Here !!
    else:
        parser.print_help()

