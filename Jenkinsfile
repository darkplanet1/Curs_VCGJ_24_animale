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
                    pip install flask
                    pip install pylint
                    pip install pytest
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
                    pylint --exit-zero 442_urspanda.py
                '''
            }
        }
        
        stage('Unit Testing') {
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    cd app;
                    . .venv/bin/activate
                    flask --app 442_urspanda test;
                '''
            }
        }
        
        stage('Deploy') {
            agent any
            steps {
                echo "Build ID: ${BUILD_NUMBER}"
                echo "Creare imagine docker"
                sh '''
                    docker build -t curs_vcgj_2024_urspanda:v${BUILD_NUMBER} .
                    '''
         
            }
        }
    }
}
