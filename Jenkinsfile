pipeline {
    agent any

    stages {
        stage('GET SCM') {
            steps {
                git 'https://github.com/andreygering/aws_state_app'
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running pylint and unittests" 
                sh 'docker-compose up -d '
            }
        }
    }
}


