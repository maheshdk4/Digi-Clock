pipeline {
    agent any

    stages {
        stage('GIT CHECKOUT') {
            steps {
                git branch: 'main', url: 'https://github.com/maheshdk4/Digi-Clock'
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
    post {
        success {
             echo 'build pass'
        }
        failure  {
             echo 'build fail'
        }
}
}
