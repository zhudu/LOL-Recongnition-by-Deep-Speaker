import os

path = "./wav/"

def get_name():
    for hero in os.listdir(path):
        for idx in os.listdir(os.path.join(path,hero)):
            for wav in os.listdir(os.path.join(os.path.join(path,hero), idx)):
                oldname = os.path.join(os.path.join(os.path.join(path,hero), idx), wav)
                newname = os.path.join(os.path.join(os.path.join(path,hero), idx), "{}-{}-{}".format(hero, idx, wav))
                os.rename(oldname, newname)

get_name()
