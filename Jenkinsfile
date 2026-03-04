pipeline {
    agent any

    environment {
        APACHE_PATH = '/var/www/html'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/prasadA7989/carweb-static-test.git'
            }
        }

        stage('Deploy to Apache') {
            steps {
                sh '''
                    echo "Deploying to Apache..."
                    sudo rm -rf /var/www/html/*
                    sudo cp -r * /var/www/html/
                '''
            }
        }
    }
}
