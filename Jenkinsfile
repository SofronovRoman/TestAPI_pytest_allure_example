pipeline {
  agent any
  stages {
    stage('test') {
        agent { dockerfile { filename 'Dockerfile' } }
        steps {
        sh 'pytest --alluredir=allure_report'
      }   
    }

  }

  post {
        always {
               allure([
               includeProperties: false,
               jdk: '',
               report: '/var/lib/jenkins/workspace/TestAPI_pytest_allure_example/allure-report',
               reportBuildPolicy: 'ALWAYS',
               results: [[path: '/var/lib/jenkins/workspace/TestAPI_pytest_allure_example@2/allure_report']]
               ])


         }
     }

}