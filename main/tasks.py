from django.core.mail import send_mail

# отправка письма заказчику
def long_send_customer_email(fullname, phone, to_email, count):
    subject = 'Ваш заказ'
 
    message = f'{fullname}, Ваш заказ составляет: в количестве {count}'
    from_email = 'ubbelousov@yandex.ru'
    # redis_conn = Redis(host='127.0.0.1', port=6379)
    
    # q = Queue(connection=redis_conn)
    # job = q.enqueue(send_email, subject, message, from_email, [to_email])
    print(f'отправка начата long_send_customer_email')
    send_mail(subject, message, from_email, [to_email])
    print(f'отправка закончена long_send_customer_email')
    
# отправка письма исполнителю
def long_send_order_email(to_email, icons, count):
    subject = 'Новый заказ'
    
    message = f'Пришел заказ на {icons} в количестве {count} '
    from_email = 'ubbelousov@yandex.ru'
    # redis_conn = Redis(host='127.0.0.1', port=6379)
    
    # q = Queue(connection=redis_conn)
    # job = q.enqueue(send_email, subject, message, from_email, [to_email])
    send_mail(subject, message, from_email, [to_email])