pipeline {
    agent any

    stages {
        stage('compile_build') {
           sh'''
               pip install -r requirements.txt
           ''' 
        }

        stage("Test"){
            //Running the unit tests
            sh 'python -m unittest test_calc.py'
        }

        stage("deploy"){
            // Building the Docker image
        script {
            docker.build('calc-build-image') {
                sh 'pyinstaller --onefile calc.py'
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