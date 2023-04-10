import React from "react";
import { Navigate, Outlet } from "react-router-dom";

export const CapacityPrivateRoute = () => {
  const accessToken = window.localStorage.getItem("accessToken");
  return accessToken ? <Outlet /> : <Navigate to="/capacity-planner/login" />;
};
