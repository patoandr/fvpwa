// comment
pipeline {
 agent any
 stages {
        stage('Checkout-git'){
               steps{
                git poll: true, url: 'git@github.com:Felipefloyd8/ProyectoFeriaVirtual.git'
               }
        }
        stage('CreateVirtualEnv') {
            steps {
                sh '''
                        bash -c "virtualenv myvenv && source myvenv/bin/activate"
                '''
            }
        }
        stage('InstallRequirements') {
            steps {
                sh '''
                        bash -c "source ${WORKSPACE}/myvenv/bin/activate && ${WORKSPACE}/myvenv/bin/python ${WORKSPACE}/myvenv/bin/pip install -r requirements.txt"
                '''
            }
        }

        stage('Running') {
            steps {
                sh '''
                        bash -c "source myvenv/bin/activate ; cd ${WORKSPACE}/ && python manage.py runserver &"
                '''
            }
        }

        stage('BuildDocker') {
            steps {
                sh '''
                        docker build -t apptest:latest .
                '''
            }
        }

                stage('PushDockerImage') {
            steps {
                sh '''
                        docker tag apptest:latest nemerdiaz/apptest:latest
                        docker push nemerdiaz/apptest:latest
                        docker rmi apptest:latest
                '''
            }
        }

        stage('Mail') {
            steps {
                emailext body: 'Prueba de Mail', subject: 'Mail', to: 'nemerdiaz@gmail.com'
            }
        }
  }
}
