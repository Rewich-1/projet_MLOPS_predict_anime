How to use the back-end as a standalone application (for testing purposes)):

Use the following commands :
- First we build the docker image
    docker build -t back_end .
- Then we make sure that the container is not running
    docker stop b_e
    docker rm b_e
- Then we run the container with the path to the models folder
    docker run -v {ABSOLUTE_PATH_TO_THE_MODELS_FOLDER}:/usr/app/models -p 5000:5000 --name=b_e back_end
    ex : docker run -v C:/Users/Glueg/Documents/GitHub/projet_MLOPS_predict_anime/back/models:/usr/app/models -p 5000:5000 --name=b_e back_end