pipeline {
    agent any

    stages {
        stage("Initialize") {
            steps{
                bat'''
                pip install -r requirements.txt
                '''
            }
        }

        stage("Test"){
            steps {
            //Running the unit tests
            bat '''python --version
            python .\build.py --jenkins --compile_test --clean --build_executable
            '''
            }
        }

        stage('compile_build') {
            steps {
                bat'''
                python .\build.py --jenkins --clean --build_executable
                ''' 
            }
        }

        stage("deploy"){
            steps{
            // Building the Docker image
                script {
                    script {
                        // Using Docker command to build the image
                        bat 'docker build -t my-calc-image .'
                        }
                }
                /*// Pushing the Docker image to a registry
                script {
                    docker.withRegistry('https://docker.registry.com', 'my-docker-credentials') {
                        docker.image('calc-build-image').push('latest')
                    }*/
            }
        }
    }
}