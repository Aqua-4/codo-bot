"""codo-bot begins here"""
import os
import shutil
import subprocess

PWD = os.getcwd()
PARDIR = os.path.abspath(os.path.join(PWD, os.pardir))
DEST = os.path.abspath(os.path.join(PARDIR , "codo-temp"))


G_DIR  = ['cd',DEST]
G_COMMIT = ['git','commit','-am','"WIP:get me codogram"']
G_STAT = ['git','status']
G_STASH = ['git','stash']


def bot_init():
    if(os.path.isdir(DEST)):
        shutil.rmtree(DEST,ignore_errors=True)
        print("Deleted file")
    shutil.copytree(PWD,DEST)
    print("Copy created")
    
def __pwd():
    subprocess.check_output('pwd')
    
def git_ops():
    os.chdir(DEST)
    x = subprocess.check_output(G_STAT)
    print(x)
    
def git_commit():
    subprocess.check_output(G_COMMIT)
    
#bot_init()
#git_ops()