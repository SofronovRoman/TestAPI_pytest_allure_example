pipeline {
  agent { dockerfile { filename 'Dockerfile' } }
  stages {



    stage('test') {
      steps {
        sh 'pytest --alluredir=allure-report'
      }   
    }

    stage('Reports') {
        steps {
           allure([
      	   includeProperties: false,
      	   jdk: '',
      	   report: '/var/lib/jenkins/workspace/TestAPI_pytest_allure_example/allure-report',
      	   reportBuildPolicy: 'ALWAYS',
      	   results: [[path: '/var/lib/jenkins/workspace/TestAPI_pytest_allure_example/allure-report']]
    	   ])

         }
     }





  }
}