import smtplib

text1 = "ovbmixoksmpivxoy"
text2 = "abdusalomabduvaliyev07@gmail.com"

password = text1
sender = text2
server = "smtp.gmail.com"
port = 465
receiver = "absaitovdev@gmail.com"
message = """
From: {}
To: {}
subject:
    https://github.com/PyAbdusalom/Module_4_exam.git
    
    docker pull pyabdusalom/4_module_exam_img:latest
    
    docker compose file git.hubda bor
""".format(sender, receiver)

with smtplib.SMTP_SSL(server, port) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message)
    print("Sending email")
