pipeline {
    agent any
    parameters {
        // booleanParam(name: 'stop_process', defaultValue: false, description: 'Kill process or not')
        choice(name: 'stop_process', choices: ['true', 'false'], description: 'Kill process or not')
    }
    stages {
        stage('Top 5 CPU usage') {
            steps {
                script {
                    sh '''
                        set +x
                        source ~/.bashrc
                        python top_cpu_usage.py 1 "${stop_process}"
                        git tag ${BUILD_ID}
                        git push origin ${BUILD_ID}
                    '''
                }
            }
        }
    }
}