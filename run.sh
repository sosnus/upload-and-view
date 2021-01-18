docker rm -f fileuploader
cd ./app
docker build -t fileuploader .
# docker build --no-cache  -t opencvtest .

# docker run -d -p 8080:8080 -it -v /Users/stanislawpulawski/data/dockervolumes/minio/photo:/data/minio/photo --name=opencvtestcontainer --restart=always opencvtest
# FOLDER=/home/zombie/data/minio/stom
FOLDER=/home/metis/data/miniostom

# FOLDER=/Users/stanislawpulawski/data/test/dev/null
docker run -d -p 6001:8080 -it -v $FOLDER:/data/minio/stom --name=fileuploader --restart=always fileuploader
sudo docker run -d -p 6002:9000 --restart=always --name minio-storage   -e "MINIO_ACCESS_KEY=miniouseradmin"   -e "MINIO_SECRET_KEY=b083d1bbe7b74f8eb610bcdbc0dd1036"   -v $FOLDER:/data/minio   minio/minio server /data/minio