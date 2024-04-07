import os
def execute(arg:list):
    action = arg
    default_dir = os.getcwd()
    os.chdir(os.path.join("module", "esmodule"))
    loc = os.path.join("ES", "launcher.py")
    if action[0] == "start":
        if os.path.exists(loc):
            os.chdir("ES")
            os.system("python launcher.py")
            os.chdir(default_dir)
        else:
            if not os.path.exists("ES"):
                os.mkdir("ES")
            os.chdir("ES")
            import ssl
            import socket
            import platform
            import urllib.request

            BANNER =("""
 ######## ##     ## ######## ########   ######   ######## ##    ##  ######  ##    ## 
 ##       ###   ### ##       ##     ## ##    ##  ##       ###   ## ##    ##  ##  ##  
 ##       #### #### ##       ##     ## ##        ##       ####  ## ##         ####   
 ######   ## ### ## ######   ########  ##   #### ######   ## ## ## ##          ##    
 ##       ##     ## ##       ##   ##   ##    ##  ##       ##  #### ##          ##    
 ##       ##     ## ##       ##    ##  ##    ##  ##       ##   ### ##    ##    ##    
 ######## ##     ## ######## ##     ##  ######   ######## ##    ##  ######     ##    
  ######  ##    ##  ######  ######## ######## ##     ##                              
 ##    ##  ##  ##  ##    ##    ##    ##       ###   ###                              
 ##         ####   ##          ##    ##       #### ####                              
  ######     ##     ######     ##    ######   ## ### ##                              
       ##    ##          ##    ##    ##       ##     ##                              
 ##    ##    ##    ##    ##    ##    ##       ##     ##                              
  ######     ##     ######     ##    ######## ##     ##                              
  ┌─┐┌─┐┌┬┐┬ ┬┌─┐
  └─┐├┤  │ │ │├─┘
  └─┘└─┘ ┴ └─┘┴  
 """)

            system = platform.system()
            if system=="Windows":
                clear="cls"
            elif system =="Linux":
                clear ="clear"
            else:
                clear ="erreur"

            Help = ("""
installer emergency system(ES) : 
suivez les consignes et tout se passera bien
toolbox s'installe au meme emplacement que ES_setup
avec tout les requierments

""")

            def fetch_file(url, filename):
                urllib.request.urlretrieve(url, filename)

            def check_internet_connection():
                try:
                    socket.create_connection(("www.google.com", 443))
                    context = ssl.create_default_context()
                    with socket.create_connection(("www.google.com", 443)) as sock:
                        with context.wrap_socket(sock, server_hostname="www.google.com") as ssock:
                            return True, ssock.version()
                except OSError:
                    return False, None
            connected, ssl_version = check_internet_connection()

            def install():
                locat = os.getcwd()

                fetch_file("https://raw.githubusercontent.com/1ventorusdev/ES/main/launcher.py", "launcher.py")
                fetch_file("https://raw.githubusercontent.com/1ventorusdev/ES/main/ES.py", "ES.py")
                fetch_file("https://raw.githubusercontent.com/1ventorusdev/ES/main/version.txt", "version.txt")
                os.system("pip install colorama")
                os.system("pip install psutil")
                os.system("pip install wmi")
                os.mkdir("test")
                sys_apps_dir = os.path.join("test", "sys_apps")
                os.mkdir(sys_apps_dir)
                os.chdir(sys_apps_dir)
                fetch_file("https://raw.githubusercontent.com/1ventorusdev/ES/main/test/sys_apps/cmd.py", "cmd.py")
                fetch_file("https://raw.githubusercontent.com/1ventorusdev/ES/main/test/sys_apps/store.py", "store.py")
                fetch_file("https://raw.githubusercontent.com/1ventorusdev/ES/main/test/sys_apps/file_manager.py", "file_manager.py")
                fetch_file("https://raw.githubusercontent.com/1ventorusdev/ES/main/test/sys_apps/task_manager.py", "task_manager.py")
                fetch_file("https://raw.githubusercontent.com/1ventorusdev/ES/main/test/sys_apps/maj.py", "maj.py")
                os.chdir(os.path.join(locat, "test"))
                system_dir = os.path.join("system")
                os.mkdir(system_dir)
                os.chdir(system_dir)
                with open("logs.txt", "w+") as data:
                    data.write("test")

                with open("admin.txt", "w+") as data:
                    data.write("admin"+"\n"+"yes")

                with open("save_config.txt", "w+") as save:
                        save.write("lin\n"+ "vert\n"+ "rouge\n"+ "bleu\n")

                os.chdir(os.path.join(locat, "test"))
                programs_dir = os.path.join("programs")
                os.mkdir(programs_dir)
                games_dir = os.path.join(programs_dir, "games")
                os.mkdir(games_dir)
                tool_dir = os.path.join(programs_dir, "tool")
                os.mkdir(tool_dir)
                os.chdir(locat)
                print("installation terminé")
                print("vous pouvez lnacer ES via 'ES' ou le fermer l'installateur via 'n' ou 'close'")



            def hall():
                os.system(clear)
                print(BANNER)
                print(Help)
                print("lancer l'installation de ES o/n ou y/n ou close pour fermer l'installateur")

            hall()
            while True:
                launch=input(">>>")

                if launch=="o" or launch=="y":
                    hall()
                    if not os.path.exists("test"):
                        if connected:
                            install()
                        else:
                            print("vous n'étes pas connecté")
                    else:
                        print("vous posséder déjà ES")
                elif launch == "ES":
                    os.system("python launcher.py")
                    os.chdir(default_dir)

                elif launch=="n" or launch=="close":
                    os.system(clear)
                    break

    elif action[0] == "maj":
        os.chdir(os.path.join("ES", "test", "sys_apps"))
        os.system("python maj.py")
        os.chdir(default_dir)
        print("mise a jour effectué")