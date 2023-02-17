import zipfile

def extractor(filebrowse,dest_folder):
    with zipfile.ZipFile(filebrowse,'r') as archive:
        archive.extractall(dest_folder)

if __name__ =="__main__":
    extractor("C:/python/app1/dest/compresses.zip","C:/python/app1/dest")
