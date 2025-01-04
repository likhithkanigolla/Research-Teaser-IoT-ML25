# College Affiliate Program: Air Quality Workshop

Welcome to the College Affiliate Program: Air Quality Workshop! In this workshop, we will work with datasets containing air quality parameters such as PM10 and PM2.5. Below is the structure of the files and their purposes:

## File Structure

```
/airquality
    ├── coefficients_calculation_notebook.ipynb
    ├── sensor1_data.csv
    ├── high_end_sensor_data.csv
/demomodel
    ├── model_building_notebook.ipynb
/general_scripts
    ├── download_dataset.py
    ├── ingest_to_postgres.py
```

1. **/airquality**
    - **coefficients_calculation_notebook.ipynb**: Notebook for calculating coefficients by comparing data from Sensor 1 with high-end sensor data. Participants can use these coefficients in their code for Sensor 1.
    - **sensor1_data.csv**: Contains air quality parameters collected from Sensor 1.
    - **high_end_sensor_data.csv**: Contains air quality parameters collected from a high-end sensor.

2. **/demomodel**
    - **model_building_notebook.ipynb**: Notebook for building a machine learning model to predict air quality values.

3. **/general_scripts**
    - **download_dataset.py**: Script to download the dataset from ThingSpeak.
    - **ingest_to_postgres.py**: Script to ingest data from ThingSpeak into a PostgreSQL database.

## Getting Started

1. **Clone the Repository**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Scripts**
    - To download the dataset:
      ```bash
      python general_scripts/download_dataset.py
      ```
    - To ingest data into PostgreSQL:
      ```bash
      python general_scripts/ingest_to_postgres.py
      ```

4. **Run the Notebooks**
    - Open the `coefficients_calculation_notebook.ipynb` in the `/airquality` folder and follow the instructions to calculate the coefficients.
    - Open the `model_building_notebook.ipynb` in the `/demomodel` folder and follow the instructions to build and evaluate the predictive model.

## Conclusion

By the end of this workshop, you will have learned how to process air quality data, calculate necessary coefficients, and build a predictive model using machine learning techniques. Happy coding!

