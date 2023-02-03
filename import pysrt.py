import pysrt


def change_charset(file_name):
    subs = pysrt.open(file_name)

    dictionar = {"º": "s", "ª": "S", "ş": "s", "Ş": "S",
                 "ţ": "t", "Ţ": "T", "þ": "t", "Þ": "T", "ã": "a", "Ã": "A",
                 "õ": "o", "Õ": "O", "ç": "c", "Ç": "C", "ñ": "n", "Ñ": "N",
                 "á": "a", "Á": "A", "é": "e", "É": "E", "í": "i", "Í": "I",
                 "ó": "o", "Ó": "O", "ú": "u", "Ú": "U", "ý": "y", "Ý": "Y",
                 "à": "a", "À": "A", "è": "e", "È": "E",
                 "Î": "I", "î": "i", "Â": "A", "â": "a"}

    for sub in subs:
        for key, value in dictionar.items():
            sub.text = sub.text.replace(key, value)
    print(subs.text)
    subs.save(file_name, encoding="utf-8")
