import "./App.css";
import { Routes, Route } from "react-router-dom";
import { Client as Styletron } from "styletron-engine-atomic";
import { Provider as StyletronProvider } from "styletron-react";
import { LightTheme, BaseProvider } from "baseui";
import Dashboard from "./components/Dashboard";
import "../node_modules/slick-carousel/slick/slick.css";
import "../node_modules/slick-carousel/slick/slick-theme.css";

const engine = new Styletron();
function App() {
  return (
    <div className="App">
      <Routes>
        <Route
          path="/"
          element={
            <StyletronProvider value={engine}>
              <BaseProvider theme={LightTheme}>
                <Dashboard />
              </BaseProvider>
            </StyletronProvider>
          }
        />
        <Route
          path="usecases"
          element={
            <StyletronProvider value={engine}>
              <BaseProvider theme={LightTheme}>
                <Dashboard />
              </BaseProvider>
            </StyletronProvider>
          }
        />
        <Route
          path="testcases"
          element={
            <StyletronProvider value={engine}>
              <BaseProvider theme={LightTheme}>
                <Dashboard />
              </BaseProvider>
            </StyletronProvider>
          }
        />
        <Route
          path="requirements"
          element={
            <StyletronProvider value={engine}>
              <BaseProvider theme={LightTheme}>
                <Dashboard />
              </BaseProvider>
            </StyletronProvider>
          }
        />
        <Route
          path="runs"
          element={
            <StyletronProvider value={engine}>
              <BaseProvider theme={LightTheme}>
                <Dashboard />
              </BaseProvider>
            </StyletronProvider>
          }
        />
        <Route
          path="executionrecords"
          element={
            <StyletronProvider value={engine}>
              <BaseProvider theme={LightTheme}>
                <Dashboard />
              </BaseProvider>
            </StyletronProvider>
          }
        />
        <Route
          path="features"
          element={
            <StyletronProvider value={engine}>
              <BaseProvider theme={LightTheme}>
                <Dashboard />
              </BaseProvider>
            </StyletronProvider>
          }
        />
        <Route
          path="features/:featureid"
          element={
            <StyletronProvider value={engine}>
              <BaseProvider theme={LightTheme}>
                <Dashboard />
              </BaseProvider>
            </StyletronProvider>
          }
        />
        <Route
          path="usecases/:usecaseid"
          element={
            <StyletronProvider value={engine}>
              <BaseProvider theme={LightTheme}>
                <Dashboard />
              </BaseProvider>
            </StyletronProvider>
          }
        />
        <Route
          path="testcases/:testcaseid"
          element={
            <StyletronProvider value={engine}>
              <BaseProvider theme={LightTheme}>
                <Dashboard />
              </BaseProvider>
            </StyletronProvider>
          }
        />
        {/* <Route path="usecase/:usecaseid" element={<IndividualUsecase />} /> */}
      </Routes>
    </div>
  );
}

export default App;
