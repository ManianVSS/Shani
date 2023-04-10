import axios from "axios";

// const accessToken = localStorage.getItem("accessToken");
export const axiosClient = axios.create({  
  // baseURL: "http://localhost:8000",
  baseURL: "",
  headers: { "Content-Type": "application/json" },
});

axiosClient.interceptors.response.use(
  (res) => {
    return res;
  },
  async (err) => {
    const originalConfig = err.config;
    if (err.response) {
      if (err.response.status === 401) {
        if (window.localStorage.getItem("accessToken")) {
          localStorage.clear();
          window.location = window.location.origin + "/login";
          return Promise.reject(err.response.data);
        }
      }
      if (err.response.status === 403 && err.response.data) {
        return Promise.reject(err.response.data);
      }
    }
    return Promise.reject(err);
  }
);
