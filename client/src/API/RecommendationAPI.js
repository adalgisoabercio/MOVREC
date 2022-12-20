import axios from 'axios';
// import defaultConfig from '../Config/defaultConfig';

export default axios.create({

    baseURL: "http://mindestiny19.pythonanywhere.com/",  // -> Deployed Python Flask API
    // baseURL: "http://localhost:5000/", // LocalHost API

    headers: { "Content-Type": "multipart/form-data" },
    
  });
  
