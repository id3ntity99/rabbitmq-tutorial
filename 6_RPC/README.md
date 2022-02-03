# RPC Tutorial

## Introduction to project
- If we need to run a function on a remote computer and wait for the reulst, then we need to consider using RPC Pattern(Remote Procedure Call)

- In this tutorial, we're going to use RabbitMQ to build an RPC system, a client and a scalable RPC sever.

- As we don't have any time-consuming tasks that are worth distributing, we're going to create a dummy RPC service that simply returns Fibonacci numbers.

## Note
### Callback queue
- In order to receive a response the client needs to send a 'callback' queue address with the request.

### Correlation ID
- Along with callback queue, it's not clear to which request the response belongs.

- That's when the correlation_id property is used. When we receive a message in the callback queue, we'll look at the CID and based on that we'll be able to match a response with a request.

- If we see an unknown CID value, we may safely discard the message since it doesn't belong to our requests.

