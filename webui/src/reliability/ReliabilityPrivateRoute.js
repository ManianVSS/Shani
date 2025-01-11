import React from "react";
import { Navigate, Outlet } from "react-router-dom";

export const ReliabilityPrivateRoute = () => {
  const accessToken = window.localStorage.getItem("accessToken");
  return accessToken ? <Outlet /> : <Navigate to="/login" />;
};
