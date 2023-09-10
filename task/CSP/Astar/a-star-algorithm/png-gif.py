import os
import glob
import imageio


res=[]

def getFile(path):
    for infile in glob.glob(os.path.join(path, '*.png')):
            res.append(infile)
 
def deleteFile(path):
    for infile in glob.glob(os.path.join(path, '*.png')):
            os.remove(infile)
 
if __name__ == '__main__':
    path = os.path.join(os.getcwd(), 'res_png')
    getFile(path)

    if eval(input("generate gif by all the png in cur_path?(1/0):\n")) == True:
        with imageio.get_writer(uri='png.gif', mode='I', fps=35) as writer:
            for i in res:
                writer.append_data(imageio.imread(i))
    
    if eval(input("delte all the png in cur_path?(1/0):\n")) == True:
        deleteFile(path)
