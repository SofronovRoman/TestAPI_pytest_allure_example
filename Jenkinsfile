pipeline {
  agent { dockerfile { filename 'Dockerfile' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install --user -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python -m pytest Tests'
      }   
    }
  }
}