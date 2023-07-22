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
        always{
//             unstash '/var/lib/jenkins/workspace/TestAPI_pytest_allure_example/allure_report' //unpack test results
            script {
                allure results: [[path: '/var/lib/jenkins/workspace/TestAPI_pytest_allure_example/allure-results']]
            }
        }
    }






}