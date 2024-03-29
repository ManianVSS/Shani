import { MantineProvider } from "@mantine/core";
import { theme } from "./theme";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Capacity from "./pages/Capacity";
import EngineerAvailability from "./pages/EngineerAvailability";
import Leaves from "./pages/Leaves";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Layout from "./components/Layout";
import { RecoilRoot } from "recoil";
import { PrivateRoute } from "./hooks/PrivateRoute";
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
export default function App() {
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
                    element={<Layout page={<Home />} auth={true} />}
                  />
                </Route>
                <Route path="/capacity" element={<PrivateRoute />}>
                  <Route
                    path="/capacity"
                    element={<Layout page={<Capacity />} auth={true} />}
                  />
                </Route>
                <Route path="/engineer-availability" element={<PrivateRoute />}>
                  <Route
                    path="/engineer-availability"
                    element={
                      <Layout page={<EngineerAvailability />} auth={true} />
                    }
                  />
                </Route>
                <Route path="/leaves" element={<PrivateRoute />}>
                  <Route
                    path="/leaves"
                    element={<Layout page={<Leaves />} auth={true} />}
                  />
                </Route>
                <Route
                  path="/login"
                  element={<Layout page={<Login />} auth={false} />}
                />
                {/* <Route
                path="/register"
                element={<Layout page={<Register />} auth={false} />}
              /> */}
              </Routes>
            </Router>
          </RecoilRoot>
        </MantineProvider>
      </AlertProvider>
    </>
  );
}
