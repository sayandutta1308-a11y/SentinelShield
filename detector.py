import re


def detect_attack(data):

    attacks = {

        "SQL Injection": [
            r"union",
            r"select",
            r"drop",
            r"insert",
            r"delete",
            r"--",
            r"' OR '1'='1"
        ],


        "XSS Attack": [
            r"<script>",
            r"</script>",
            r"alert",
            r"javascript:"
        ],

        "Command Injection": [
            r"cmd",
            r"powershell",
            r"&&",
            r";"
        ]
    }


    for attack_type, patterns in attacks.items():

        for pattern in patterns:

            if re.search(
                pattern,
                data,
                re.IGNORECASE
            ):
                return attack_type


    return "Safe"