def task_build_monkeysign():
    '''Build and tag a docker image - usage: build_monkeysign -t:0.0.1 (default: "latest")'''
    return {
        'actions': [
            'docker build --rm --tag monkeysign:%(tag)s ./monkeysign/.',
            'docker build --rm --tag monkeysign:latest ./monkeysign/.',
        ],
        'params': [
            {
                'name': 'tag',
                'short': 't',
                'default': 'latest'
            },
        ],
        'verbosity': 2
    }

def task_run_monkeysign():
    '''Run the container of a monkey sign, available at localhost:8081 - usage: run_monkey_sign -t:0.0.1 (default: "latest")'''
    return {
        'actions': [
            'docker run --rm -it -p 8081:80 --name monkeysign monkeysign:%(tag)s',
        ],
        'params': [
            {
                'name': 'tag',
                'short': 't',
                'default': 'latest'
            },
        ],
        'verbosity': 2
    }

def task_run_two_monkeys():
    '''Run the two monkeys, available at localhost:8081 and 8082 - usage: run_two_monkeys -t 0.0.1 (default: "latest")'''
    return {
        'actions': [
            'TAG=%(tag)s docker compose -f ./monkeysign/docker-compose.yml up',
        ],
        'params': [
            {
                'name': 'tag',
                'short': 't',
                'default': 'latest'
            },
        ],
        'verbosity': 2
    }
