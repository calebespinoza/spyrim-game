pipeline {
    agent { label 'automation' }
    stages {
        stage ('Static Code Analysis') {
            steps {
                script {
                    def scannerHome = tool 'sonarqube-scanner-at'
                    withSonarQubeEnv('sonarqube-automation') {
                        sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectName=spyrim-game -Dsonar.projectKey=spyrim-game -Dsonar.sources=."
                    }
                }
            }
        }
    }
}