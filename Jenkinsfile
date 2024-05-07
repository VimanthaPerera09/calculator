pipeline {
    agent any

    stages {
        stage('compile_build') {
            steps {
                bat'''
                    pip install -r requirements.txt
                ''' 
            }
        }

        stage("Test"){
            steps {
            //Running the unit tests
            bat 'python -m unittest test_calc.py'\
            }
        }

        stage("deploy"){
            steps{
            // Building the Docker image
                script {
                    docker.build('calc-build-image') {
                        bat 'pyinstaller --onefile calc.py'
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