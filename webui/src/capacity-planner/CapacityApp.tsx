import { MantineProvider } from "@mantine/core";
import { theme } from "./theme";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CapacityHome from "./pages/CapacityHome";
import Capacity from "./pages/Capacity";
import EngineerAvailability from "./pages/EngineerAvailability";
import Leaves from "./pages/Leaves";
import Login from "../pages/Login";
import CapacityLayout from "./components/CapacityLayout";
import { RecoilRoot } from "recoil";
import { PrivateRoute } from "../hooks/PrivateRoute";
import { transitions, positions, Provider as AlertProvider } from "react-alert";
import AlertTemplate from "./components/AlertTemplate";

const options = {
  // you can also just use 'bottom center'
  position: positions.TOP_RIGHT,
  timeout: 5000,
  offset: "30px",
  // you can also just use 'scale'
  transition: transitions.SCALE,
};
export default function CapacityApp() {
  return (
    <>
      <AlertProvider template={AlertTemplate} {...options}>
        <MantineProvider theme={theme} withGlobalStyles withNormalizeCSS>
          <RecoilRoot>
            <Router>
              <Routes>
                <Route path="/" element={<PrivateRoute />}>
                  <Route
                    path="/"
                    element={
                      <CapacityLayout page={<CapacityHome />} auth={true} />
                    }
                  />
                </Route>
                <Route path="/capacity" element={<PrivateRoute />}>
                  <Route
                    path="/capacity"
                    element={<CapacityLayout page={<Capacity />} auth={true} />}
                  />
                </Route>
                <Route path="/engineer-availability" element={<PrivateRoute />}>
                  <Route
                    path="/engineer-availability"
                    element={
                      <CapacityLayout
                        page={<EngineerAvailability />}
                        auth={true}
                      />
                    }
                  />
                </Route>
                <Route path="/leaves" element={<PrivateRoute />}>
                  <Route
                    path="/leaves"
                    element={<CapacityLayout page={<Leaves />} auth={true} />}
                  />
                </Route>
                <Route
                  path="/login"
                  element={<CapacityLayout page={<Login />} auth={false} />}
                />
              </Routes>
            </Router>
          </RecoilRoot>
        </MantineProvider>
      </AlertProvider>
    </>
  );
}
