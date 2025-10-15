pipeline {
    agent any

    stages {
        stage('GIT CHECKOUT') {
            steps {
                git https://github.com/maheshdk4/Digi-Clock
            }
        }
        stage('BUILDING') {
            steps {
                echo 'BUILDING APP'
            }
        }
        stage('TEST') {
            steps {
                echo 'TESTING APP'
            }
        }
        stage('DEPLOY') {
            steps {
                echo 'DEPLOYING APP'
            }
        }
        
    }
}
