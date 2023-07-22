pipeline {
  agent any
  stages {
    stage('test') {
        agent { dockerfile { filename 'Dockerfile' } }
        steps {
        sh 'pytest --alluredir=allure-report'
      }   
    }
  }
  post {
        always{
            unstash 'allure-results' //unpack test results
            script {
                allure results: [[path: 'integration/allure-results']]
            }
        }
    }






}