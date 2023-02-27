/* A chaque fois qu'une branche non dev ou main est push on test les features de la dite branche.
    Ex : si un push est effectué sur la branche "front" un test est fait pour vérifier que le front marche*/
pipeline {
    agent any
    stages {
        // build and run unit tests on feature branches
        stage('Testing the front end') {
            when {
                branch 'front'
            }
            steps {
                // Run stress 
                // To be done with Selenium for example
            }
        }
        stage('Testing the back end') {
            when {
                branch 'back'
            }
            steps {
                bat 'cd back & conda activate jenkins & pip install -r requirements.txt & python -m unittest'
            }
        }

        // stress test and push to release on the develop branch
        stage('Testing the dev') {
            when {
                branch 'dev'
            }
            steps {
                bat 'conda activate jenkins & pip install -r requirements.txt & python -m unittest'
            }
        }

        // wait for user acceptance on the release branch before pushing to main
        stage('User Acceptance') {
            when {
                branch 'release'
            }
            steps {
                input {
                    message "Does the release candidate look good?"
                    ok "Yes, release it!"
                }
                // Deploy to production if user accepts
            }
        }
        // on merging with main, push to Dockerhub.
        stage('Push to Dockerhub') {
            when {
                branch 'main'
            }
            steps {
                // Push to Dockerhub
            }
        }
    }
}