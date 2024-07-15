from django.core.mail import send_mail


def long_send_order_email(fullname, phone, email):
    subject = 'Ваш заказ'
 
    message = f'{fullname}, Ваш заказ составляет: '
    from_email = 'ubbelousov@yandex.ru'
    to_email = email
    # redis_conn = Redis(host='127.0.0.1', port=6379)
    
    # q = Queue(connection=redis_conn)
    # job = q.enqueue(send_email, subject, message, from_email, [to_email])
    send_mail(subject, message, from_email, [to_email])