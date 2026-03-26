pipeline {
    agent any

    stages {
	stage('Clean Workspace') {
	   steps {
	        cleanWs()
	    }
	}

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
                sh 'docker compose up -d'
            }
        }

        stage('Integration Test') {
            steps {
		sh 'sleep 15'
                sh 'curl -f http://165.227.129.1:5000 || exit 1'
            }
        }
    }
}
