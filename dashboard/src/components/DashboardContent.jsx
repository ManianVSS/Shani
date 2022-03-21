import { useStyletron } from "baseui";
import React from "react";
import { Table } from "baseui/table-semantic";
import Filter from "baseui/icon/filter";
import { Label2, Paragraph4 } from "baseui/typography";

import { data, tableTitles } from "../assets/constants";
import { axiosClient } from "../api/AxiosInstance";
import Usecases from "../pages/Usecases";
import Home from "../pages/Home";
import Testcases from "../pages/Testcases";
import Requirements from "../pages/Requirements";
import Features from "../pages/Features";
import Runs from "../pages/Runs";
import ExecutionRecords from "../pages/ExecutionRecord";
import IndividualUsecase from "../pages/IndividualUsecase";
import IndividualFeature from "../pages/IndividualFeature";
import IndividualTest from "../pages/IndividualTestcase";

const DashboardContent = () => {
  const componentMetaData = window.location.pathname;
  let componentToRender = <></>;
  if (componentMetaData === "/usecases") {
    componentToRender = <Usecases />;
  } else if (componentMetaData === "/") {
    componentToRender = <Home />;
  } else if (componentMetaData === "/testcases") {
    componentToRender = <Testcases />;
  } else if (componentMetaData === "/requirements") {
    componentToRender = <Requirements />;
  } else if (componentMetaData === "/features") {
    componentToRender = <Features />;
  } else if (componentMetaData === "/runs") {
    componentToRender = <Runs />;
  } else if (componentMetaData === "/executionrecords") {
    componentToRender = <ExecutionRecords />;
  } else if (componentMetaData.indexOf("/usecases/") !== -1) {
    componentToRender = <IndividualUsecase />;
  } else if (componentMetaData.indexOf("/features/") !== -1) {
    componentToRender = <IndividualFeature />;
  } else if (componentMetaData.indexOf("/testcases/") !== -1) {
    componentToRender = <IndividualTest />;
  }
  const [css] = useStyletron();
  return (
    <div
      className={css({
        width: "100%",
        borderRadius: "0.5rem",
        background: "#fff",
        border: "1px solid #DFE0EB",
        overflow: "hidden",
        "@media (max-width: 768px)": {
          margin: "0 1.5rem",
        },
      })}
    >
      <div
        className={css({
          padding: "2rem",
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
        })}
      >
        <Label2>
          <b>{componentMetaData.toUpperCase().replace("/", "")}</b>
        </Label2>
        <div
          className={css({
            display: "flex",
            alignItems: "center",
            cursor: "pointer",
          })}
        >
          {/* <Paragraph4
            className={css({
              display: "flex",
              alignItems: "center",
            })}
          >
            <Filter
              size="2rem"
              className={css({
                marginRight: "0.3rem",
              })}
            />
            Filter
          </Paragraph4> */}
        </div>
      </div>
      {componentToRender}
    </div>
  );
};
export default DashboardContent;
