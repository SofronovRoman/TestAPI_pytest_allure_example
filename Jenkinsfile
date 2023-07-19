pipeline {
  agent { docker { image 'python:alpine' } }
  stages {
    stage('build') {
      steps {
        sh 'virtualenv TestAPI -p python3'
        sh 'source TestAPI/bin/activate'
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python -m pytest Tests'
      }   
    }
  }
}