from twilio.rest import Client
import openai

openai.api_key = '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'

mensagem = ''
while True:
    account_sid = 'AC06395e09aa7ca0eeae7fe6b86aeb1711'
    auth_token = '302a79f6d18d56b9b491f54353301425'
    openai.api_key = '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'
    client = Client(account_sid, auth_token)
    messages = client.messages.list(limit=10)
    most_recent_message = messages[0]
    for message in messages[1:]:
        if message.date_created > most_recent_message.date_created:
            most_recent_message = message
    pergunta = (most_recent_message.body)
    print(pergunta)

    if pergunta != mensagem or '':
        openai.api_key = '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'
        response = openai.Image.create(
            prompt=f'{pergunta}',
            n=1,
            size="1024x1024"
        )
        link = response['data'][0]['url']
        print(link)

        message = client.messages.create(
            from_='whatsapp:+14155238886',
            media_url=[f'{link}'],
            to='whatsapp:+5511944424926'

        )

        print(message.sid)
    else:
        print('mensagem igual a ultima')
        continue
