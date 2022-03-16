import os 
import subprocess

class JetsonUtils:
    def __init__(self):
        pass
    
    def getJetsonEnv(self)-> dict:
        env_jetson = subprocess.check_output("env | grep JETSON", shell=True)
        foo = env_jetson.decode()
        env_list = foo.split("\n")
        env_dict = {}
        for i in env_list:
            if i:
                i_items = i.split("=")
                print(i_items)
                env_dict[i_items[0]] = i_items[1]
        return env_dict