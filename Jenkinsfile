pipeline {
    agent none  // No default agent; specifies more granular agent settings later

    environment {
        APP_DIR = 'app'  // Set the application directory
    }

    stages {
        stage('Setup Environment') {
            agent any
            steps {
                echo 'Setting up the environment...'
                dir("${APP_DIR}") {  // Ensures commands run in the app directory
                    script {
                        sh '''
                        echo "Current working directory:";
                        pwd;
                        echo "Listing directory contents:";
                        ls -l;
                        echo "Activating Python virtual environment...";
                        . ./activeaza_venv;
                        '''
                    }
                }
            }
        }

        stage('Build') {
            agent any
            steps {
                echo 'Building...'
                dir("${APP_DIR}") {
                    script {
                        sh '''
                        echo "Current working directory:";
                        pwd;
                        echo "Listing directory contents:";
                        ls -l;
                        '''
                    }
                }
            }
        }

        stage('pylint - Code Quality') {
            agent any
            steps {
                echo 'Running Pylint...'
                dir("${APP_DIR}") {
                    script {
                        sh '''
                        echo "Running Pylint on library files...";
                        pylint --exit-zero librarie/*.py;
                        echo "Running Pylint on test files...";
                        pylint --exit-zero ./test_*.py;
                        echo "Running Pylint on main Python script...";
                        pylint --exit-zero 442D_Rinocer.py;
                        '''
                    }
                }
            }
        }

        stage('Unit Testing with pytest') {
            agent any
            steps {
                echo 'Unit testing with Pytest...'
                dir("${APP_DIR}") {
                    script {
                        sh '''
                        echo "Running pytest for unit testing...";
                        python3 -m pytest -v;
                        '''
                    }
                }
            }
        }
        
        stage('Deploying') {
            agent any 
            steps {
                echo 'Deploying the app...'
                dir("${APP_DIR}") {
                    script {
                        sh '''
                        echo "Building Docker image...";
                        docker build . -t rinocer_app;
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            dir("${APP_DIR}") {
                script {
                    sh '''
                    echo "Running Docker system prune...";
                    docker system prune -f;
                    '''
                }
            }
        }
        success {
            echo 'Build and deployment succeeded!'
        }
        failure {
            echo 'An error occurred!'
        }
    }
}
