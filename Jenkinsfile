pipeline {
    agent any
    
    parameters {
        string defaultValue: '500', name: 'INTERVAL',
        string defaultValue: '500', name: 'ID',
        string defaultValue: '500', name: 'ACCESS'
    }
    
    
    stages {
        
        
        stage('CREATE ENV') {
            steps {
               sh "echo $ID >> .env"
               sh "echo $ACCESS >> .env"
            }
        }
    
        stage('GET SCM') {
            steps {
               git branch: 'main', url: 'https://github.com/andreygering/aws_state_app/'
            }
        }

        stage('Build and Test') {
            steps {
                sh 'docker build -t aws_state_app:v-0.1.0.${BUILD_NUMBER} .'
            }
        }

        stage('Tag Image') {
            steps {
                sh 'docker tag aws_state_app:v-0.1.0.${BUILD_NUMBER} andreygering/aws_state_app:v-0.1.0.${BUILD_NUMBER}'
            }
        }

        stage('Docker Login') {
            steps {
                sh 'docker login -u ${USERNAME} -p ${PASSWORD} '
            }
        }
        
        
        stage('Push Image') {
            steps {
                sh 'docker push andreygering/aws_state_app:v-0.1.0.${BUILD_NUMBER}'
            }
        }
     }
}
