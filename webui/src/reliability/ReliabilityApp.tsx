import { MantineProvider } from "@mantine/core";
import { theme } from "./theme";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CapacityHome from "./pages/ReliabilityHome";
import Login from "../pages/Login";
import CapacityLayout from "./components/ReliabilityLayout";
import { RecoilRoot } from "recoil";
import { PrivateRoute } from "../hooks/PrivateRoute";
import { transitions, positions, Provider as AlertProvider } from "react-alert";
import AlertTemplate from "./components/AlertTemplate";
import ReliabilityHome from "./pages/ReliabilityHome";
import ReliabilityLayout from "./components/ReliabilityLayout";

const options = {
  // you can also just use 'bottom center'
  position: positions.TOP_RIGHT,
  timeout: 5000,
  offset: "30px",
  // you can also just use 'scale'
  transition: transitions.SCALE,
};
export default function ReliabilityApp() {
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
                      <ReliabilityLayout
                        page={<ReliabilityHome />}
                        auth={true}
                      />
                    }
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
