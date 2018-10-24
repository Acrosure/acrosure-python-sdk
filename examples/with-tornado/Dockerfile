FROM python:3

ADD server.py /
ADD data.py /

RUN pip3 install tornado
RUN python3 -m pip install acrosure_sdk==1.0.1

CMD [ "python3", "./server.py" ]
