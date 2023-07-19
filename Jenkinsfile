pipeline {
  agent { docker { image 'python:alpine' } }
  stages {
    stage('build') {
      steps {
        sh 'sudo pip install --upgrade pip'
        sh 'sudo pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python -m pytest Tests'
      }   
    }
  }
}