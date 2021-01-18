import web
import os 
import time

urls = ('/upload', 'Upload')

class Upload:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head></head><body>
<form method="POST" enctype="multipart/form-data" action="">
<input type="file" name="myfile" />
<br/>
<input type="text" name="folder" />
<br/>
<input type="submit" />
</form>
</body></html>"""

    def POST(self):
        x = web.input(myfile={})
        timestamp = web.input().folder 
        print(type(timestamp))
        print(timestamp)
        print(x.myfile.filename)
        print(x.myfile.filename.split('/')[-1])
        # filedir = '/Users/stanislawpulawski/data/test/dev/null/stom' # change this to the directory you want to store the file in.
        # filedir = '/home/zombie/data/minio/stom' # change this to the directory you want to store the file in.
        filedir = '/data/minio/stom' # change this to the directory you want to store the file in.
        os.system("cd {} && mkdir {}".format(filedir, timestamp))
        if 'myfile' in x: # to check if the file-object is created
            filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
            filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
            fout = open(filedir + '/' + timestamp + '/' + filename,'wb') # creates the file where the uploaded file should be stored
            fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.
        return str("DONE: " + filedir + '/'+ timestamp +'/'+ filename)
        # raise web.seeother('/upload')


if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()