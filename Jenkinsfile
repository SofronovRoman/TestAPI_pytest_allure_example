pipeline {
  agent { dockerfile { filename 'Dockerfile' } }
  stages {



    stage('test') {
      steps {
        sh 'python -m pytest Tests'
      }   
    }

    stage('Reports') {
        steps {
           allure([
      	   includeProperties: false,
      	   jdk: '',
      	   properties: [],
      	   reportBuildPolicy: 'ALWAYS',
      	   results: [[path: 'report']]
    	   ])

         }
     }





  }
}