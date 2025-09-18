📡 Project Title: IoT Predictive Maintenance Demo
🎯 Objective

This project demonstrates predictive maintenance using IoT sensor data and Recurrent Neural Networks (RNNs).
It predicts future device behavior so maintenance can be performed before failures occur, reducing downtime and improving operational efficiency.

🛠️ Tools & Technologies

Programming Language: Python 3.5

Frameworks & Libraries:

PySpark – Distributed data processing

TensorFlow – Deep learning model development

Plotly – Interactive visualization

Requests – HTTP library for API interactions

Data Platform: MapR Converged Data Platform

📁 Project Structure
IoT_Predictive_Maintenance_Demo/
├── demo_data.zip
├── mapr_kafka_rest.py
├── Sensor_ETLsparksubmit.py
├── Sensor_Historical_Data_Analysis.py
├── Sensor_XML2MaprStreams_producer.py
├── Stream_IoT_Prediction_Dashboard_plotly.py
├── predictive_maintenance_gui.py
└── README.md

⚙️ Setup Instructions
1. Clone the Repository
git clone https://github.com/marthanjoel/IoT_Predictive_Maintenance_Demo-.git
cd IoT_Predictive_Maintenance_Demo-

2. Install Dependencies
pip install pyspark tensorflow plotly requests

3. Configure MapR Sandbox

Download and install the MapR Sandbox
 in VirtualBox.

Add port forwarding for Kafka REST and Jupyter:

Kafka_REST TCP 127.0.0.1 8082 8082
jupyter TCP 127.0.0.1 9999 9999


SSH into the sandbox and install Kafka REST:

ssh -p 2222 root@localhost
yum install mapr-kafka-rest
echo 'streams.buffer.max.time.ms=100' >> /opt/mapr/kafka-rest/kafka-rest-2.0.1/config/kafka-rest.properties
service mapr-warden restart
exit

4. Create MapR Stream and Topic
ssh -p 2222 user01@localhost
maprcli stream create -path /user/user01/iot_stream -produceperm p -consumeperm p -topicperm p
maprcli stream topic create -path /user/user01/iot_stream -topic sensor_record
exit

5. Run the Prediction Dashboard
python Stream_IoT_Prediction_Dashboard_plotly.py

6. Launch the Tkinter GUI
python predictive_maintenance_gui.py


Click Run Prediction to execute the model and visualize results.

📊 Simulation Details

Sensor Data: Historical IoT device data in XML / .dat files

Prediction Logic: RNN predicts next time period values

Visualization: Plotly interactive plots for real-time monitoring

🖼️ Screenshots
1 <img width="1366" height="768" alt="Screenshot from 2025-09-18 14-40-28" src="https://github.com/user-attachments/assets/eb30f0ce-669e-49be-8ab1-657285407697" />

1 <img width="1346" height="654" alt="Screenshot from 2025-09-18 15-04-15" src="https://github.com/user-attachments/assets/30933d51-6d62-4153-b67f-c749bf805738"  />


---


📝 Observations

Prediction accuracy depends on sensor data quality

Visualization helps identify trends and anomalies

Real-time streaming with MapR enables continuous monitoring


---

🔮 Future Improvements

Integrate cloud storage for historical data

Add automated alerting system for maintenance

Upgrade to latest TensorFlow / Python versions

Embed plots directly in GUI for real-time visualization
