How to use to launch the app ?

Go to /back and run the following commands :
    - docker build -t back_end .


Go to /front and run the following commands :
    - docker build -t front_end .

Go to the root of this repo and run the following commands :
    - docker-compose up

Go to http://localhost:8501/ to see the app


If you want to run the grafana dashboard :
    - Go to grafana/dockprom and run the following commands :
        - docker-compose up -d
    - Go to http://localhost:3000/ and use the following credentials :
        - login : admin
        - password : admin