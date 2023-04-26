# Cliente-Servidor

Implementação de um servidor e clientes de troca de mensagens similar ao serviço da plataforma Twitter. Clientes enviam mensagens para o servidor informando em quais mensagens estão interessados. O servidor recebe mensagens de clientes e repassa cada mensagem para todos os clientes que estão interessados naquela mensagem. O tópico de uma mensagem é definido pelos tags que ela contém. Cada cliente envia ao servidor em quais tags está interessado, e o servidor irá repassar ao cliente todas as mensagens que contém pelo menos uma tag de seu interesse. Esse paradigma de comunicação é conhecido como publish/subscribe.
