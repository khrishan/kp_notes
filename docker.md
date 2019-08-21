docker run -it -v /home/khrishan/Dropbox/Coding/jupyter:/home/jovyan -p 8888:8888 jupyter/scipy-notebook

docker run -it -v /home/khrishan/Dropbox/Coding/notes:/home/jovyan -p 8888:8888 jupyter/scipy-notebook

docker run --name website_db -e MYSQL_ROOT_PASSWORD=password -v /home/khrishan/Dropbox/website/KPS_DB.sql:/kp.sql -d mysql


docker run --name myadmin -d --link website_db:db -p 8080:80 phpmyadmin/phpmyadmin
