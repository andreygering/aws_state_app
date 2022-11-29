pipeline {
    agent any
    
    parameters {
        string defaultValue: '500', name: 'INTERVAL'
        string defaultValue: '', name: 'ID'
        string defaultValue: '', name: 'ACCESS'
        string defaultValue: '', name: 'USERNAME'
        string defaultValue: '', name: 'PASSWORD'

    }
    
    
    stages {
        
        
        stage('CREATE ENV') {
            steps {
               sh "echo KEY_ID=$ID >> .env"
               sh "echo ACCESS_KEY=$ACCESS >> .env"
            }
        }
        
        stage('Install YQ') {
            steps {
               sh 'apt install wget && wget https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -O /usr/bin/yq && chmod +x /usr/bin/yq'
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

        stage('Merge to Main') {
            steps {
                sh 'git add .'
                sh 'git commit -m "Commit annotation: aws_state_app:v-0.1.0.${BUILD_NUMBER}"'
                sh 'git merge origin/stage'
            }
        }
     }
}
