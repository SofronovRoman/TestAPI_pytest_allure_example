pipeline {
  agent { dockerfile { filename 'Dockerfile' } }
  stages {



    stage('test') {
      steps {
        sh 'pytest --alluredir=allure_report'
      }   
    }

    stage('Reports') {
        steps {
           allure([
      	   includeProperties: false,
      	   jdk: '',
      	   report: '/var/lib/jenkins/workspace/TestAPI_pytest_allure_example/allure_report',
      	   reportBuildPolicy: 'ALWAYS',
      	   results: [[path: '/var/lib/jenkins/workspace/TestAPI_pytest_allure_example/allure_report']]
    	   ])

         }
     }





  }
}