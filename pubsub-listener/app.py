from google.cloud import pubsub_v1
import time

project_id = "MAGA_LOCAL"
subscription_id = "promo3p.worker.core.sync_status_promotion.sub"

def callback(message):
    print("Iniciando processamento...")
    print(f"Recebendo mensagem: {message.data.decode('utf-8')}")
    time.sleep(30)
    print(f"finalizado mensagem: {message.data.decode('utf-8')}")
    message.ack()

def listen_for_messages():
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, subscription_id)

    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f"Escutando em {subscription_path}...\n")

    try:
        streaming_pull_future.result()
    except KeyboardInterrupt:
        print("Cancelando a inscrição...")
        streaming_pull_future.cancel() 
        streaming_pull_future.result()

if __name__ == "__main__":
    listen_for_messages()
