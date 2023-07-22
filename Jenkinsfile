pipeline {
  agent any
  stages {
    stage('test') {
        agent { dockerfile { filename 'Dockerfile' } }
        steps {
        sh 'pytest --alluredir=./allure-report'
      }   
    }

  }
  post {
        always {
            script{
               allure([
               includeProperties: false,
               jdk: '',
          	   report: './allure-report',
               reportBuildPolicy: 'ALWAYS',
               results: [[path: './allure-report']]
               ])
               }

         }
     }

}