pipeline {
    agent any

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
        sudo rm -rf /var/www/html/*
        sudo cp -r * /var/www/html/
        '''
    }
}
        
        

        stage('Restart Apache') {
            steps {
                sh 'sudo systemctl restart apache2'
            }
        }
    }
}
