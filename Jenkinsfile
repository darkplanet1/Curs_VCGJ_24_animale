pipeline {
    agent none

    environment {
        APP_DIR = 'app'
    }

    stages {
        stage('Setup Environment') {
            agent any
            steps {
                echo 'Setting up the environment...'
                dir("${APP_DIR}") {
                    sh '''
                        pwd;
                        ls -l;
                        . ./activeaza_venv;
                    '''
                }
            }
        }

        stage('Build') {
            agent any
            steps {
                echo 'Building...'
                dir("${APP_DIR}") {
                    sh '''
                        pwd;
                        ls -l;
                    '''
                }
            }
        }

        stage('pylint - Code Quality') {
            agent any
            steps {
                echo 'Running Pylint...'
                dir("${APP_DIR}") {
                    sh '''
                        pylint --exit-zero librarie/*.py;
                        pylint --exit-zero ./test_*.py;
                        pylint --exit-zero 442D_Rinocer.py;
                    '''
                }
            }
        }

        stage('Unit Testing with pytest') {
            agent any
            steps {
                echo 'Unit testing with Pytest...'
                dir("${APP.COMMON_DIR}") {
                    sh 'python3 -m pytest -v'
                }
            }
        }
        
        stage('Deploying') {
            agent any 
            steps {
                echo 'Deploying the app...'
                dir("${APP_DIR}") {
                    sh 'docker build . -t rinocer_app'
                }
            }
        }
    }
}
