import os
import yaml
from github import Github

# Carregar configuração
with open('dyno-badges.config.yml', 'r') as file:
    config = yaml.safe_load(file)

# Inicializar GitHub
g = Github(os.environ['GITHUB_TOKEN'])
repo = g.get_repo(os.environ['GITHUB_REPOSITORY'])
user = os.environ['GITHUB_ACTOR']

# Atualizar perfil com badges dinâmicas
def update_profile_with_badges():
    readme_path = 'ReadMe.md'
    with open(readme_path, 'r') as file:
        content = file.read()
    
    # Aqui você pode adicionar lógica para inserir badges dinâmicas
    # Por enquanto, vamos apenas salvar o arquivo como está
    with open(readme_path, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    update_profile_with_badges()