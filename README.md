# Real-Time Streaming ETL OpenWeatherMap
![Untitled Diagram(6)](https://user-images.githubusercontent.com/89646884/160747396-b7befe0b-e311-4299-8c87-3e95e9f6a851.jpg)



## Description

To start this project, we use a data source from https://openweathermap.org/ to load data from OpenWeatherMap API using Postman to detect region accuracy to go to Apache Kafka using python script. After that, the data is loaded into HDFS via SparkStreaming. This process takes place on the Google Cloud Platform. The areas that will be collected weather data are in Indonesia, especially in Bali, Lombok, Labuan Bajo, Berau, and Raja Ampat. After collecting, the data is processed using Apache spark. This data collection aims to find out the accurate and real-time weather data owned by the sensor service provider. This process lasts for seven days.



## OpenWeather API

OpenWeather platform is a set of elegant and widely recognisable APIs. Powered by convolutional machine learning solutions, it is capable of delivering all the weather information necessary for decision-making for any location on the globe. The API key is all you need to call any of our weather APIs. Once you sign up using your email, the API key (APPID) will be sent to you in a confirmation email. Your API keys can always be found on your account page, where you can also generate additional API keys if needed.
## Example on how to make an API call using API key

#### Example of API call Bali

```http
  http://api.openweathermap.org/data/2.5/weather?id=1650535&appid=6afa72ee728492b6960489dfba7a472a
```

| Parameter |     |                 |
| :-------- | :------- | :------------------------- |
| `appid` | `required` | Your unique API key (you can always find it on your account page under the "API key" tab)


## 🔗 Links
[![kaggle](https://img.shields.io/badge/kaggle-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://www.kaggle.com/pingkivila)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pingki-vila-9a1a27226/)

