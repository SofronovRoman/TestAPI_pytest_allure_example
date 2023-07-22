pipeline {
  agent any
  stages {
    stage('test') {
        agent { dockerfile { filename 'Dockerfile' } }
        steps {
        sh 'pytest --alluredir=allure-report'
      }   
    }
    stage('reports'){
        steps {
            script {
                allure([ includeProperties: false,
                 jdk: '',
                 properties: [],
                 reportBuildPolicy: 'ALWAYS',
                 results: [[path: '/var/lib/jenkins/workspace/TestAPI_pytest_allure_example/allure-report']] ]) }
                 }
    }
  }
  post {
        always {
            script{
               allure([
               includeProperties: false,
               jdk: '',
    //       	   report: '/var/lib/jenkins/workspace/TestAPI_pytest_allure_example/allure-report',
               reportBuildPolicy: 'ALWAYS',
               results: [[path: '/var/lib/jenkins/workspace/TestAPI_pytest_allure_example/allure-report']]
               ])
               }

         }
     }

}