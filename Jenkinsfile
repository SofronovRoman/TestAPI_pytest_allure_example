pipeline {
  agent any
  stages {
    stage('test') {
        agent { dockerfile { filename 'Dockerfile' } }
        steps {
        sh 'pytest --alluredir=./allure-results'
      }   
    }

  }
  post {
        always {
            script{
               allure([
               includeProperties: false,
               jdk: '',
          	   report: './allure-results',
               reportBuildPolicy: 'ALWAYS',
               results: [[path: './allure-results']]
               ])
               }

         }
     }

}