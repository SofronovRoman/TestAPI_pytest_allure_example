pipeline {
  agent { docker { image 'python:alpine' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install --upgrade pip'
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