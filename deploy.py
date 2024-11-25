import json
import subprocess
import sys

# Função para carregar parâmetros de um arquivo JSON
def load_parameters(env):
    filename = f"{env}-params.json"
    try:
        with open(filename, 'r') as file:
            params = json.load(file)
            return " ".join([f"{key}={value}" for key, value in params.items()])
    except FileNotFoundError:
        print(f"Arquivo {filename} não encontrado.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Erro ao ler o arquivo {filename}. Verifique o formato do JSON.")
        sys.exit(1)

# Obter o ambiente (dev, hml, prd) passado como argumento
if len(sys.argv) < 2:
    print("Por favor, informe o ambiente: dev, hml ou prd.")
    sys.exit(1)

environment = sys.argv[1]
parameter_overrides = load_parameters(environment)

# Rodar o comando sam deploy com os parâmetros carregados
subprocess.run([
    "sam", "deploy", "--config-env", environment, "--parameter-overrides", parameter_overrides
])
