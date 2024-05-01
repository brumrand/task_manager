import axios from 'axios';

    const path = "localhost:8000/api/v1.0/tasks";
    const taskApi = axios.create({
            baseUrl: path
    });

