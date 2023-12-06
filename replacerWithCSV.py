import csv
import os
import re

def main():
    try:
        # Configurações
        MATCH_CASE = True
        MATCH_WHOLE_WORD = True
        CSV_CONTAINS_HEADER = False

        # Função para realizar a substituição em um único arquivo
        def replace_in_file(file_path, de, para):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
            except UnicodeDecodeError:
                # Arquivo não é texto ou não está em UTF-8, ignorando...
                return 0

            # Preparar o padrão de pesquisa dependendo das configurações
            flags = 0 if MATCH_CASE else re.IGNORECASE
            word_boundary = r'\b' if MATCH_WHOLE_WORD else ''
            pattern = word_boundary + re.escape(de) + word_boundary

            # Substituir e contar
            new_content, num_subs = re.subn(pattern, para, content, flags=flags)

            # Escrever o novo conteúdo no arquivo se houve alguma substituição
            if num_subs > 0:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(new_content)

            return num_subs

        # Solicitar ao usuário o caminho do arquivo CSV
        csv_path = input("Digite o caminho completo para o arquivo CSV com os dados de substituição: ").strip().strip('"')

        # Solicitar ao usuário o caminho da pasta do projeto
        project_path = input("Digite o caminho da pasta do projeto onde as substituições devem ser feitas: ").strip().strip('"')

        # Ler o arquivo CSV
        replacements = []
        with open(csv_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=';')
            if CSV_CONTAINS_HEADER:
                next(csv_reader)  # Pular cabeçalho se houver
            replacements = [(row[0], row[1]) for row in csv_reader]

        # Ordenar as substituições do maior para o menor
        replacements = sorted(replacements, key=lambda x: len(x[0]), reverse=True)

        # Realizar substituições em cada arquivo da pasta do projeto
        replacement_counts = {de: 0 for de, para in replacements}
        for root, dirs, files in os.walk(project_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                for de, para in replacements:
                    count = replace_in_file(file_path, de, para)
                    replacement_counts[de] += count

        # Exibir o total de substituições
        print("\nSubstituições completas. Resumo de substituições feitas:")
        for de, para in replacements:
            print(f"'{de}' substituído por '{para}': {replacement_counts[de]} vezes")

    except Exception as e:
        print(f"Ocorreu um erro durante a execução do script: {e}")
    finally:
        input("Pressione Enter para sair...")

if __name__ == "__main__":
    main()
