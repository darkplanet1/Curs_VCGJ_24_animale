pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                    cd app;
                    ls -l;
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip3 install flask
                    pip3 install pylint
                    pip3 install pytest
                '''
            }
        }
        
        stage('pylint - calitate cod') {
            steps {
                echo 'Pylint...'
                sh '''
                    cd app;
                    . .venv/bin/activate
                    if [ $? -eq 0 ]
                    then
                        echo "SUCCESS: venv was activated."
                    else
                        echo "FAIL: cannot activate venv"
                        python3 -m venv .venv
                        . .venv/bin/activate
                    fi
                    
                    pylint --exit-zero librarie/*.py
                    pylint --exit-zero 442_vulture.py
                '''
            }
        }
        
        stage('Unit Testing') {
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    cd app;
                    . .venv/bin/activate
                    flask --app 442_vulture test;
                '''
            }
        }
        
        stage('Deploy') {
            agent any
            steps {
                echo "Build ID: ${BUILD_NUMBER}"
                echo "Creare imagine docker"
                sh '''
                    docker build -t curs_vcgj_2024_vulture:v${BUILD_NUMBER} .
                    '''
         
            }
        }
    }
}
