pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/prasadA7989/carweb-static-test.git'
            }
        }

        stage('Stop Old Containers') {
            steps {
                sh 'docker-compose down || true'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Deploy Containers') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Check Running Containers') {
            steps {
                sh 'docker ps'
            }
        }

        stage('Test Backend') {
            steps {
                sh 'curl -f http://localhost:5000/health'
            }
        }
    }
}
