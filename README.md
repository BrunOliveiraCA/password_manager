# 🔐 Gerenciador de Senhas com Criptografia

Este é um simples gerenciador de senhas em Python que utiliza a biblioteca `cryptography` para armazenar senhas de forma segura usando criptografia simétrica com `Fernet`.

## 📦 Funcionalidades

- 🔐 Criptografia das senhas utilizando chave única (`Fernet`)
- ➕ Adição de novas senhas criptografadas
- 👀 Visualização de senhas descriptografadas
- 💾 Armazenamento local em arquivo `.txt`

## ⚙️ Pré-requisitos

- Python 3.6+
- Biblioteca `cryptography`

Instale a biblioteca com o pip:

```bash
pip install cryptography
```

🚀 Como usar
1. Gerar a chave de criptografia
Antes de rodar o programa, é necessário gerar a chave que será usada para criptografar e descriptografar as senhas. Descomente o trecho abaixo no código e execute uma única vez:

```bash
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()
```
Isso criará o arquivo key.key, que será utilizado posteriormente.

2. Executar o programa
Após gerar a chave, comente novamente o trecho write_key() e rode o programa normalmente:

```bash
python main.py
```

Você verá o seguinte menu:

```bash
Would you like to add a new password, view existing ones or quit? (add/view/quit)?
```

#### add: adiciona uma nova conta e senha

#### view: exibe todas as contas com suas senhas descriptografadas

#### quit: encerra o programa

<br>

## 📁 Estrutura de Arquivos

#### main.py: código principal da aplicação

#### key.key: chave de criptografia gerada (NUNCA compartilhe este arquivo publicamente)

#### passwords.txt: arquivo onde as senhas são armazenadas de forma criptografada

<br>

## 🛡️ Aviso de Segurança
Este projeto é apenas para fins educacionais. Não use este gerenciador para armazenar senhas reais ou sensíveis, pois ele não possui proteção contra acesso físico ao arquivo nem gerenciamento avançado de segurança.

<br>

## 🧠 Aprendizados
Este projeto demonstra:

Leitura e escrita de arquivos com Python

Criptografia simétrica usando Fernet

Estrutura de menus via terminal

<br>

## 📄 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e compartilhar.
