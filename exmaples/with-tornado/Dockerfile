FROM python:3

ADD server.py /
ADD data.py /

RUN pip3 install tornado
RUN pip3 install requests
RUN python3 -m pip install --index-url https://test.pypi.org/simple/ acrosure_sdk==0.9.2

ENV ENV test

CMD [ "python3", "./server.py" ]
