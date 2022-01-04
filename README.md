# RabbiMQ tutorial with python pika.

### Start: 2022/01/01

# Source

Original tutorial: https://www.rabbitmq.com/getstarted.html

# 왜 메시징을 사용하는가? (Why should I use this?)

1. 성능 (Performance)

- 비동기 메시징을 통한 대용량 트래픽 처리
  (Handling high-volume of network traffic with asyncronous messaging.)

- 프로듀서와 컨슈머가 직접 소통하지 않고 메시지 큐를 통해 소통하므로 프로듀서는 컨슈머의 작업이 끝날때까지 기다릴 필요가 없음.
  (Producers don't communicate directly to consumer but using queue, producers don't need to wait untill process of consumer is done.)

2. 신뢰성 (Reliability)

- 프로세서가 다운되거나 네트워크 연결이 끊어져도 메시지가 큐에 보관되므로 어느 정도의 신뢰성과 내고장성 확보 가능
  (By saving messages in queue, we create reliability and fault tolerence even if the processers go down or network connection fail occurs)

3. 확장성 (Scalability)

- 컨슈머 프로세서가 오버로드 될경우 다수의 컨슈머 인스턴스를 생성, 큐와 연결함으로써 안전하게 프로듀서와 연결 가능
  (When a consumer processor is overloaded, we can create multiple consumer instances and connect them to the existing queue safely.)

- Round robin 등을 이용하여 메시지를 다수의 컨슈머 인스턴스에 분산시킴으로써 로드 밸런싱이 가능
  (Enabling load balancing using round robin, etc.)
