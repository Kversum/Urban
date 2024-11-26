def send_email(message, recipient, sender="university.help@gmail.com"):
    recipient_l = recipient.lower()
    sender_l = sender.lower()
    match = ('.com', '.ru', '.net')
    f = False
    count_rr = 0
    count_ss = 0
    if '@' in recipient_l and sender_l:
        for i in match:
            count_r = recipient_l.count(i)
            count_s = sender_l.count(i)
            if count_r == 1:
                count_rr = 1
            if count_s == 1:
                count_ss = 1
            if count_rr and count_ss == 1:
                f = True
                break
    if sender_l == recipient_l and f:
        print("Нельзя отправить письмо самому себе")
        return
    if sender_l != "university.help@gmail.com" and f:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ письмо с адреса {sender} на адрес {recipient}")
        return
    if f:
        print(f"Письмо успешно отправлено с адреса {sender_l} на адрес {recipient_l}")
    else:
        print(f"Невозможно отправить письмо с адреса {sender_l} на адрес {recipient_l}")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

