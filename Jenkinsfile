node{
        stage('Env Setup'){
            sh 'env | sort'
        }
        
        stage('Promote Code from dev to master'){
            build job: 'Promote Code - dev to master'; propogate=true; wait=true
        }

}
