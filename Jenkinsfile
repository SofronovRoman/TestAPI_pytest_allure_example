pipeline {
  agent { docker { image 'python:alpine' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt --user'
      }
    }
    stage('test') {
      steps {
        sh 'python -m pytest Tests'
      }   
    }
  }
}