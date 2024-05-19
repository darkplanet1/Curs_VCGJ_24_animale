pipeline {
    agent none

    stages {
        stage('Build') {
            agent any
            steps {
                echo 'Building...'
                sh '''
                    cd app;
                    pwd;
                    ls -l;
                    . ./activeaza_venv_jenkins
                    '''
            }
        }

        stage('pylint - calitate cod') {
            agent any
            steps {
            	echo 'Pylint...'
                sh '''
                    cd app;
                    . ./activeaza_venv;
                    

                    pylint --exit-zero librarie/*.py;
                    
                    pylint --exit-zero ./test_*.py;
                    
                    pylint --exit-zero 442D_vultur.py;
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            agent any
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    cd app;
                    . ./activeaza_venv;
                    python3 -m pytest -v;
                '''
            }
        }
        /*    }
        }*/
        stage('Deploy') {
            agent any
            steps {
                echo "Build ID: ${BUILD_NUMBER}"
                echo "Creare imagine docker"
                sh '''
                	docker build -t curs_vcgj_2024_vultur:v${BUILD_NUMBER} .
                	'''
            }
        }
    }
}
