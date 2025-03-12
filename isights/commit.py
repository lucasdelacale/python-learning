'''
#-----------------------------------------------------------------------------------------------#
->  Atualizando o Github
#-----------------------------------------------------------------------------------------------#
->  Para caso de trabalho externo, puxe as atualizações antes de trabalhar
    git pull origin main

->  Caso seja o primeiro push do repositório
    git branch -M main

->  Saber o status do repositório (caso precise)
    git status

->  Adicionar todas as alterações
    git add .

->  Cria um commit com descrição      
    git commit -m "Atualização do código"

->  Enviar atualizações para o GitHub    
    git push origin main

->  Caso o Vscode não esteja na pasta do projeto
    cd /Users/seu-usuario/caminho/do/projeto    

->  Caso de erro por mudanças externas
    git pull origin main --rebase
    git push origin main
    
#-----------------------------------------------------------------------------------------------#

->  Trabalhando com os arquivos do github (Opção que permite excluir os arquivos locais)

->  Acesse a pasta onde deseja salvar o clone do github
    cd /caminho/para/sua/pasta

->  Clone o repositório
    git clone https://github.com/SeuUsuario/SeuRepositorio.git

->  Entre na pasta
    cd SeuRepositorio

->  Pronto.

* Importante! *
->  Você pode apagar os arquivos locais e trabalhar apenas com os do GitHub.
->  Mas sempre que precisar editar, terá que clonar o repositório novamente.

#-----------------------------------------------------------------------------------------------#
->  Alias
->  Criando um alias (apelido) para baixar as atualizações do github
    git config --global alias.save '!git add . && git commit -m "update" && git push origin main'
->  Agora, basta rodar: git update


->  Criando um alias (apelido) para salvar updates no Github
    git config --global alias.save "add . && commit -m 'update' && push origin main"
->  Agora, sempre que quiser salvar, basta rodar: git save

#-----------------------------------------------------------------------------------------------#
'''