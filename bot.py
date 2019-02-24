"""codo-bot begins here"""

import os
import shutil
import subprocess
import re

target = "codo-bot"


PARDIR = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
TARDIR = os.path.abspath(os.path.join(PARDIR, target))
DEST = os.path.abspath(os.path.join(PARDIR, "codo-temp"))

FILES = []

G_DIR = ['cd', DEST]
#G_COMMIT = ['git','commit','-am',"WIP:get me codogram"]
G_COMMIT = ['git', 'commit', '-am', "WIP:Test"]
G_STAT = ['git', 'status']
G_PULL = ['git','pull']
G_STASH = ['git', 'stash']
G_PUSH = ['git', 'push']


def bot_struct():
    if(os.path.isdir(DEST)):
        shutil.rmtree(DEST, ignore_errors=True)
        print("Deleted file")
    shutil.copytree(TARDIR, DEST)
    print("Copy created")


def _get_files():
    os.chdir(TARDIR)
    files = os.listdir()
    files.remove('.git')
    return files


# _______FILES list_____
FILES = _get_files()
# _______FILES list_____


def __pwd():
    return subprocess.check_output('pwd')


def git_ops():
    os.chdir(DEST)
    subprocess.check_output(G_STAT)


def _mod_files():
    __mod = "modified"
    mod_files = []
    add_files = []

    os.chdir(TARDIR)
    stat_str = "{}".format(subprocess.check_output(G_STAT))
    mod_cnt = stat_str.count(__mod)
    print("Modified file count is {}".format(mod_cnt))
    status = stat_str.split('Untracked files')

    if mod_cnt > 0:
        for file in FILES:
            if file in status[0]:
                mod_files.append(file)
    if len(status) > 1:
        for file in FILES:
            if file in status[1]:
                add_files.append(file)
    return {'mod_files': mod_files, 'add_files': add_files}


def _read_file(file_name):
    f = open(file_name, "r")
#    print(f.read())
    return f.read()


def _write_file(file_name, txt):
    f = open(file_name, "w")
    f.write(txt)


def _dest_stash():
    __cd_dest()
    subprocess.check_output(G_PULL)
    subprocess.check_output(G_STASH)

def _git_diff(filename):
    __cd_dest(False)
    src_txt = subprocess.check_output(['git','diff',filename])
    return src_txt.decode('utf-8')

def _proc_diff(txt):
    re_pat = r'\@@(.+?)\@@'
#    pattern = r'^@@(.+?)@@$'
    txt = _read_file('src_txt.py')
    txt =  re.split(re_pat, txt)
    txt = txt.reverse()
    txt = txt[0]
    txt.split('')
    res_txt = []
    for line in txt.splitlines():
        if line[0] != '-':
            res_txt.append(line)
    res_txt = '\n'.join(res_txt)
    _write_file('res_txt.py',res_txt)
    
def _conti_write(dst_file_path, src_txt, splitter='\n'):
    dst_txt = _read_file(dst_file_path)
    if dst_txt != src_txt:
        delta_txt = src_txt.replace(dst_txt, '')
        txt_split = delta_txt.split(splitter)
        chunk = '\n' if txt_split[0] == '' else txt_split[0]
        res_txt = "{}{}".format(dst_txt, chunk)
        _write_file(dst_file_path, res_txt)
        git_comm_push()
        _conti_write(dst_file_path, src_txt)

def __cd_dest(bool_dst=True):
    if not bool_dst:
        if __pwd() != TARDIR:
            os.chdir(TARDIR)
    else:    
        if __pwd() != DEST:
            os.chdir(DEST)
    

def git_comm_push():
    __cd_dest()
    subprocess.check_output(G_COMMIT)
    print("Commit and push to git")
    subprocess.check_output(G_PUSH)


def bot_start():
#    _splitter = '\n'
#    bot_struct()
    files = _mod_files()
    mod_files = files['mod_files']
    _dest_stash()
    for file in mod_files:
        src_file_path = os.path.abspath(os.path.join(TARDIR, file))
        src_txt = _read_file(src_file_path)
        dst_file_path = os.path.abspath(os.path.join(DEST, file))
#        _conti_write(dst_file_path, src_txt)


bot_start()
