pipeline {
  agent { docker { image 'python:alpine' } }
  stages {
    stage('build') {
      steps {
        sh ''
        sh 'pip3 install -r requirements.txt --user'
      }
    }
    stage('test') {
      steps {
        sh 'python -m pytest Tests'
      }   
    }
  }
}