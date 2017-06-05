'''
Synopsis:
This is an implementation of shutil.copytree() 

Created on Jun 1, 2017

@author: pneela
'''
import os
from shutil import copy2,Error, copystat

def copytree(src,dst,symlinks=False,execute=False):
    '''execute must be true to execute the copy commands'''
    
    names = os.listdir(src)
    print('Create destination dir: ',dst)
    if execute == True:
        os.makedirs(dst)
    errors = []
    
    for name in names:
        srcname = os.path.join(src,name)
        dstname = os.path.join(dst,name)
        print("Src: {} , Dest: {}".format(srcname,dstname))
        
        try:
            if symlinks and os.path.islink(srcname):
                #Get the path( string) to which the symbolic link point
                linkto = os.readlink(srcname)
                print('linkto :',linkto)
                if execute == True:
                    os.symlink(linkto,dstname)
            elif os.path.isdir(srcname):
                copytree(srcname, dstname, symlinks)
            else:
                print('Execute -> copy2(srcname,dstname)')
                if execute == True:
                    copy2(srcname,dstname)
        except OSError as why:
            #Convert the string for of the exception object
            errors.append(str(why))
        
        except Error as err:
            errors.append(err.args[0])
    
    try:
        print("copystat(src,dst)")
        if execute == True:
            copystat(src,dst)
    except OSError as why:
        if why.winerror is None:
            errors.extend((src,dst,str(why)))
    
    if errors:
        raise Error(errors)


if __name__ == '__main__':
    print('Execution Start')
    copytree('D:\\Python', 'D:\\PythonCopy', True)
