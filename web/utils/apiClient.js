import axios from 'axios';

const apiClient = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL,
  withCredentials: true,
});

apiClient.interceptors.request.use(function (config) {
  const token = localStorage.getItem('token');
  config.headers.Authorization =  token ? `Bearer ${token}` : '';
  return config;
});

apiClient.interceptors.response.use((response) => {
  return response;
}, (error) => {
  if (error.response.status === 401) {
    localStorage.removeItem('token');
    location.reload();
  }
  return Promise.reject(error);
});

export default apiClient;
