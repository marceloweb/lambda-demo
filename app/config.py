import os

def get_config():
    env = os.getenv('ENV', 'dev')
    
    config = {
        'dev': {
            'db_host': 'dev-db.example.com',
            'db_name': 'dev_db',
            'api_url': 'https://api.dev.example.com'
        },
        'hml': {
            'db_host': 'hml-db.example.com',
            'db_name': 'hml_db',
            'api_url': 'https://api.hml.example.com'
        },
        'prd': {
            'db_host': 'prd-db.example.com',
            'db_name': 'prd_db',
            'api_url': 'https://api.prd.example.com'
        }
    }
    
    return config.get(env, config['dev'])
