pipeline {
    agent any
    triggers {
        pollSCM('* * * * *')
    }
    parameters {
        string(name: 'FIRST_PARAM', defaultValue: 'Hello', description: 'First param')
    }
    stages {
        stage('Prepare venv') {
            steps {
                sh'''
                set -ex
                python -m venv .venv
                source $WORKSPACE/.venv/Scripts/activate
                python -m pip install --upgrade pip
                '''
            }
        }
        stage('Test') {
            steps {
                sh'''
                source $WORKSPACE/.venv/Scripts/activate
                bash make install
                bash make lint-ci
                '''
            }
        }
    }
}
