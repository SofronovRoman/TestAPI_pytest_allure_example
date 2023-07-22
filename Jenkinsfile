pipeline {
  agent any
  stages {
    stage('test') {
        agent { dockerfile { filename 'Dockerfile' } }
        steps {
        sh 'pytest --alluredir=allure-results'
      }   
    }

  }

  post {
        always {
               allure([
               includeProperties: false,
               jdk: '',
               reportBuildPolicy: 'ALWAYS',
               results: [[path: 'allure-results']]
               ])


         }
     }

}