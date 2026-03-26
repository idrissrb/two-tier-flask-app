pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url:  'https://github.com/idrissrb/two-tier-flask-app.git'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Run Containers') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Integration Test') {
            steps {
                sh 'curl -f http://localhost:5000 || exit 1'
            }
        }
    }
}
