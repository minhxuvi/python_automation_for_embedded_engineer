pipeline {
    agent any
    triggers {
        pollSCM('* * * * *')
    }
    parameters {
        string(name: 'FIRST_PARAM', defaultValue: 'Hello', description: 'First param')
    }
    stages {
        stage('Greeting') {
            steps {
                sh "echo ${FIRST_PARAM}"
            }
        }
    }
}
