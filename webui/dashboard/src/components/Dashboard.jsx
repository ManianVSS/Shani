import React from "react";
import { styled } from "baseui";
import Sidebar from "./Sidebar";
import DashboardHeader from "./DashboardHeader";
import DashboardContent from "./DashboardContent";
const Dashboard = () => {
  const [open, setOpen] = React.useState(false);
  return (
    <DashboardWrapper>
      <Sidebar open={open} setOpen={setOpen} />
      <DashboardHeader open={open} setOpen={setOpen} />
      <DashboardContent />
    </DashboardWrapper>
  );
};
export default Dashboard;
const DashboardWrapper = styled("section", {
  display: "flex",
  flexDirection: "column",
  alignItems: "flex-start",
  background: "#F7F8FC",
  position: "relative",
  paddingLeft: "285px",
  paddingRight: "2rem",
  width: "100%",
  minHeight: "100vh",
  maxWidth: "100vw",
  boxSizing: "border-box",
  "@media (max-width: 768px)": {
    paddingLeft: "0",
  },
});
