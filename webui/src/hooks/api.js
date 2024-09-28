import axios from "axios";
import { baseURL } from "./baseURL";

export const axiosClient = axios.create({
  baseURL: baseURL + "/siteconfig/api/",
  headers: {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Credentials": true,
  },
});

export const axiosClientBasic = axios.create({
  baseURL: baseURL + "",
  headers: {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Credentials": true,
  },
});

axiosClient.interceptors.response.use(
  (res) => {
    return res;
  },
  async (err) => {
    const originalConfig = err.config;
    if (err.response.status === 401 && !originalConfig._retry) {
      originalConfig._retry = true;

      try {
        const refreshToken = localStorage.getItem("refreshToken");
        const response = await axiosClient.post("/auth/jwt/refresh", {
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

axiosClientBasic.interceptors.response.use(
  (res) => {
    return res;
  },
  async (err) => {
    const originalConfig = err.config;
    // if (err.response) {
    //   if (err.response.status === 401) {
    //     if (window.localStorage.getItem("accessToken")) {
    //       localStorage.clear();
    //       window.location = window.location.origin + "/login";
    //       return Promise.reject(err.response.data);
    //     }
    //   }
    //   if (err.response.status === 403 && err.response.data) {
    //     return Promise.reject(err.response.data);
    //   }
    // }

    if (err.response.status === 401 && !originalConfig._retry) {
      originalConfig._retry = true;

      try {
        const refreshToken = localStorage.getItem("refreshToken");
        const response = await axiosClientBasic.post("/auth/jwt/refresh", {
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
