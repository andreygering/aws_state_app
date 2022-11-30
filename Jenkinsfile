pipeline {
    agent any
    
    parameters {
        string defaultValue: '500', name: 'INTERVAL'
        string defaultValue: '', name: 'ID'
        string defaultValue: '', name: 'ACCESS'
        string defaultValue: '', name: 'USERNAME'
        string defaultValue: '', name: 'PASSWORD'
        string defaultValue: '', name: 'TOKEN'
        

    }

    // environment { 
    //     config = readJSON file: 'aws_state_app/aws-state-app-helm/config.json'
    //     ACCESS = "${config.ACCESS}"
    //     SECRET = "${config.SECRET}"
    //     LOGIN = "${config.LOGIN}"
    //     PASSWORD = "${config.PASSWORD}"
    //     TOKEN = "${config.TOKEN}"
        
    //     }
    
    
    stages {
        
        
        stage('CREATE ENV') {
            steps {
               sh "pwd && ls && cd aws-state-app-helm && pwd && ls"
               sh "echo KEY_ID=$ID >> .env"
               sh "echo ACCESS_KEY=$ACCESS >> .env"
               sh "echo TOKEN=$TOKEN >> env_token.txt"
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

        stage('Install GH') {
            steps {
               sh 'apt install gh'
            }
        }
    

        stage('Merge to Main') {
            steps {
                sh 'gh auth login --with-token < env_token.txt'
                sh 'gh pr create --title "aws_state_app:v-0.1.0.${BUILD_NUMBER}" --body "aws_state_app:v-0.1.0.${BUILD_NUMBER}"'
                
            }
        }
     }
}
