FROM centos/python-36-centos7

MAINTAiNER Justin Brandenburg


RUN pip install --upgrade pip
RUN pip install flask
RUN pip install numpy
RUN pip install scikit-learn
RUN pip install pandas
RUN pip install joblib
RUN pip install -U Werkzeug

WORKDIR /app

COPY ./multioutput_rf_flask_app.py /app/multioutput_rf_flask_app.py
COPY ./multi_output_model.sav /app/multi_output_model.sav

ENTRYPOINT [ "python" ]

CMD [ "multioutput_rf_flask_app.py" ]