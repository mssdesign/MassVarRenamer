## MASS VAR RENAMER

Este projeto contém um script Python que realiza substituições de texto em massa em arquivos de um diretório especificado pelo usuário.

## Como Usar

Para usar este script, você deve fornecer um arquivo CSV contendo os pares de strings de "DE" e "PARA" que você deseja substituir. O script lerá este arquivo e realizará as substituições correspondentes em todos os arquivos do diretório de projeto que você especificar.

## Transformando o Script em um Executável

Para converter este script Python em um executável, siga as instruções abaixo:

1. Instale o PyInstaller (se ainda não estiver instalado):
    ```bash
    pip install pyinstaller
    ```

2. Navegue até o diretório que contém seu script Python no terminal.

3. Use o PyInstaller para criar o executável a partir do seu script Python:
    ```bash
    pyinstaller --onefile replacerWithCSV.py
    ```
    Isso irá gerar um arquivo executável na pasta `dist` no diretório atual.

4. O arquivo executável pode então ser distribuído e executado sem a necessidade de uma instalação do Python.

## Execução Como Administrador

Note que, dependendo das permissões de arquivo no diretório de destino, pode ser necessário executar o script como administrador. Para fazer isso, clique com o botão direito no executável e selecione "Executar como administrador".

## Contribuições

Contribuições são bem-vindas. Sinta-se à vontade para forkar o repositório, fazer suas alterações e abrir um pull request.
