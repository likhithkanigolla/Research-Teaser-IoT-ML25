# College Affiliate Program: Air Quality Workshop

Welcome to the College Affiliate Program: Air Quality Workshop! In this workshop, we will work with datasets containing air quality parameters such as PM10 and PM2.5. Below is the structure of the files and their purposes:

## File Structure

```
.
├── Readme.md
├── airquality-calibration
│   └── Sensor Calibration Linear Regression.ipynb
├── datasets
│   ├── Aero_IoT_Workshop_Batch_4.csv
│   ├── Team_01.csv
│   ├── Team_02.csv
│   ├── Team_03.csv
│   ├── Team_04.csv
│   ├── Team_05.csv
│   ├── Team_06.csv
│   ├── Team_07.csv
│   ├── Team_08.csv
│   ├── Team_09.csv
│   ├── Team_10.csv
│   ├── Team_11.csv
│   ├── Team_12.csv
│   ├── Team_13.csv
│   ├── Team_14.csv
│   ├── Team_15.csv
│   ├── Team_16.csv
├── general_scripts
│   ├── demo_dataset.py
│   ├── demo_dataset_with_time.py
│   ├── download_dataset.py
│   └── ingest_to_postgres.py
├── ml-model
└── requirements.txt

5 directories, 26 files
```

1. **/airquality**
    - **coefficients_calculation_notebook.ipynb**: Notebook for calculating coefficients by comparing data from Sensor 1 with high-end sensor data. Participants can use these coefficients in their code for Sensor 1.
    - **sensor_data.csv**: Contains air quality parameters collected from Sensor 1.
    - **high_end_sensor_data.csv**: Contains air quality parameters collected from a high-end sensor.

2. **/ml-model**
    - **model_building_notebook.ipynb**: Notebook for building a machine learning model to predict air quality values.

3. **/general_scripts**
    - **download_dataset.py**: Script to download the dataset from ThingSpeak.
    - **ingest_to_postgres.py**: Script to ingest data from ThingSpeak into a PostgreSQL database.

## Getting Started

1. **Clone the Repository**
    ```bash
    git clone https://github.com/likhithkanigolla/Research-Teaser-IoT-ML25.git
    cd Research-Teaser-IoT-ML25
    ```

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Scripts**
    - To download the dataset:
      ```bash
      python general_scripts/download_dataset.py <channel-id> <APIKEY>
      ```
    - To ingest data into PostgreSQL:
      ```bash
      python general_scripts/ingest_to_postgres.py <channel-id> <APIKEY>
      ```
    - To generate a demo dataset:
      ```bash
      python general_scripts/demo_dataset.py
      ```
    - To generate a demo dataset with time:
      ```bash
      python general_scripts/demo_dataset_with_time.py
      ```
    - To Generate the randomdata to the thingspeak:
      ```bash
      python general_scripts/thingspeak_datagenerator.py <APIKEY>
      ```

1. **Run the Notebooks**
    - Open the `Sensor Calibration Linear Regression.ipynb` in the `/airquality-calibration` folder and follow the instructions to calculate the coefficients.

## Conclusion

By the end of this workshop, you will have learned how to process air quality data, calculate necessary coefficients, and build a predictive model using machine learning techniques. Happy coding!

