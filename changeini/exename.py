#conding:utf-8
import os
def exename():
    config_dir = r"E:\Program Files (x86)\Jiangmin"
    for root, dirs, files in os.walk(config_dir):
            for iter_file in files:
               print("root:",root)
               print("dirs",dirs)
               print("files",iter_file)
               ff=str(iter_file)
               if ff.endswith(".exe"):
                   write_a(ff)


def write_a(files):
    with open("exename.txt","a") as f:
        f.writelines("{}\n".format(files))

if __name__ == '__main__':
    exename()
