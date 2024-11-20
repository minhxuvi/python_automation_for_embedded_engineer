pipeline {
    agent any
    triggers {
        pollSCM('* * * * *')
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
                # sed -i 's/\r$//' run.sh
                make install
                make lint-ci
                '''
            }
        }
    }
}
