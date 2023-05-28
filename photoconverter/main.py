import glob
import rawpy
import imageio
import time


def main():
    # Timer is optional
    print("Starting Now")
    start = time.time()

    # Sometimes the file ending can be .nef or .NEF, therefore I included both possibilities to save extra work.
    in_path = "E:/Full Sized Photo Storage/Camera NEF/"
    path_NEF = in_path+"*.NEF"
    out_path = "E:/Full Sized Photo Storage/Camera JPG/"
    path_JSON = out_path +"*.jpg"
    count = 0

    # Don't process the pictures that already have been processed
    in_pics = glob.glob(path_NEF)
    out_pics = glob.glob(path_JSON)
    
    sample = in_pics[0]
    in_names = [getNameFromPath(path) for path in in_pics]
    out_names = [getNameFromPath(path) for path in out_pics]
    unconverted_names = list(set(in_names) - set(out_names))

    
    for name in unconverted_names:
        path=in_path+name+".NEF"
        count = +1

        with rawpy.imread(path) as raw:
            rgb = raw.postprocess()
            imageio.imwrite(path.replace('.NEF', '.jpg'), rgb)
            count = count + 1
            print('image #', count, ' done')

    # Timer is optional
    end = time.time()
    minutes = (end - start) / 60
    seconds = (end - start) % 60

    print("Elapsed Time:", round(minutes), "minutes and ", round(seconds), "seconds")

def getNameFromPath(path:str = ""):
    name = path.split("\\")[-1].split(".")[0]
    return name

if __name__ == '__main__':
    main()