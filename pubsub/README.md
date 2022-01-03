# Publish/Subscribe Tutorial

---

## Introduction to project

---

- Previous tutorial project, Work Queue, is that each task is delivered to exactly one worker.

- In this tutorial project, we'll deliver one message to multiple consuers using 'publish/subscribe pattern'.

- To illustrate the pattern, we're going to build a simple logging system that will consist of two programs - the first will emit log messages and the second will receive and print them.

- In the logging system, every running receiver program will get the messages. One receiver program will receive a log and direct the it to disk, and the other, at the same time, will display log on the screen.

- Essentially, published log messages are going to be broadcast to all the receivers.
