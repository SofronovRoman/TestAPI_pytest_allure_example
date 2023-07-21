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
      	   properties: [],
      	   reportBuildPolicy: 'ALWAYS',
      	   results: [[path: 'allure_report']]
    	   ])

         }
     }





  }
}