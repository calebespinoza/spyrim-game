pipeline {
    agent { label 'automation' }
    stages {
        stage ('Static Code Analysis') {
            steps {
                script {
                    def scannerHome = tool 'sonarqube-scanner-at'
                    withSonarQubeEnv('sonarqube-automation') { // If you have configured more than one global server connection, you can specify its name
                        sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectName=spyrim-game"
                    }
                }
            }
        }
    }
}