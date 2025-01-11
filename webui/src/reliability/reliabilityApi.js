import axios from "axios";
import { baseURL } from "../hooks/baseURL";

// const accessToken = localStorage.getItem("accessToken");
export const axiosClientForLogin = axios.create({
  baseURL: baseURL + "/api",
  headers: {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Credentials": true,
  },
});

export const axiosClientForReliability = axios.create({
  // baseURL: baseURL + "/people/api",
  baseURL: baseURL,
  headers: {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Credentials": true,
  },
});

axiosClientForLogin.interceptors.response.use(
  (res) => {
    return res;
  },
  async (err) => {
    const originalConfig = err.config;
    if (err.response.status === 401 && !originalConfig._retry) {
      originalConfig._retry = true;

      try {
        const refreshToken = localStorage.getItem("refreshToken");
        const response = await axiosClientForLogin.post("/auth/jwt/refresh", {
          refresh: refreshToken,
        });
        const { access } = response.data;

        localStorage.setItem("accessToken", access);

        // Retry the original request with the new token
        originalConfig.headers.Authorization = `Bearer ${access}`;
        return axios(originalConfig);
      } catch (error) {
        // Handle refresh token error or redirect to login
        window.location = window.location.origin + "/login";
        return Promise.reject(error.response.data);
      }
    }
    return Promise.reject(err);
  }
);

axiosClientForReliability.interceptors.response.use(
  (res) => {
    return res;
  },
  async (err) => {
    const originalConfig = err.config;
    if (err.response.status === 401 && !originalConfig._retry) {
      originalConfig._retry = true;

      try {
        const refreshToken = localStorage.getItem("refreshToken");
        const response = await axiosClientForLogin.post("/auth/jwt/refresh", {
          refresh: refreshToken,
        });
        const { access } = response.data;

        localStorage.setItem("accessToken", access);

        // Retry the original request with the new token
        originalConfig.headers.Authorization = `Bearer ${access}`;
        return axios(originalConfig);
      } catch (error) {
        // Handle refresh token error or redirect to login
        window.location = window.location.origin + "/login";
        return Promise.reject(error.response.data);
      }
    }
    return Promise.reject(err);
  }
);
