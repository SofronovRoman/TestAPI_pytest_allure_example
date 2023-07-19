FROM python:alpine

RUN mkdir /home/jenkins
RUN groupadd -g 999 jenkins
RUN useradd -r -u 999 -g jenkins -d /home/jenkins jenkins
RUN chown jenkins:jenkins /home/jenkins
USER jenkins
WORKDIR /home/jenkins

CMD ["/bin/bash"]