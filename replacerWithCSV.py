import csv
import os
import re

def main():
    try:
        MATCH_CASE = True
        MATCH_WHOLE_WORD = True

        def replace_in_file(file_path, de, para):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
            except UnicodeDecodeError:
                return 0

            flags = 0 if MATCH_CASE else re.IGNORECASE
            word_boundary = r'\b' if MATCH_WHOLE_WORD else ''
            pattern = word_boundary + re.escape(de) + word_boundary

            new_content, num_subs = re.subn(pattern, para, content, flags=flags)

            if num_subs > 0:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(new_content)

            return num_subs

        csv_path = input("Digite o caminho completo para o arquivo CSV com os dados de substituição: ").strip('"')

        project_path = input("Digite o caminho da pasta do projeto onde as substituições devem ser feitas: ").strip('"')

        replacements = []
        with open(csv_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=';')
            next(csv_reader)
            for de, para, _ in csv_reader:
                replacements.append((de, para, 0))

        for root, dirs, files in os.walk(project_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                for i, (de, para, count) in enumerate(replacements):
                    total_subs = replace_in_file(file_path, de, para)
                    replacements[i] = (de, para, count + total_subs)

        print("\nSubstituições completas. Resumo de substituições feitas:")
        for de, para, count in replacements:
            print(f"'{de}' substituído por '{para}': {count} vezes")

    except Exception as e:
        print(f"Ocorreu um erro durante a execução do script: {e}")
    finally:
        input("Pressione Enter para sair...")

if __name__ == "__main__":
    main()
