import React from "react";
import BreadcrumbComponent from "./BreadcrumbComponent";
import RequirementTable from "./RequirementTable";
import { AgGridReact } from "ag-grid-react";
import { axiosClientBasic } from "../../hooks/api";
import "ag-grid-community/dist/styles/ag-grid.css";
import "ag-grid-community/dist/styles/ag-theme-alpine.css";
import { useNavigate, useParams } from "react-router-dom";
import Heading from "../../capacity-planner/components/Heading";
import TreeComponent from "../../components/TreeComponent";
import json from "../../components/TreeComponent/data/json";
import { Col, Row } from "react-bootstrap";
import IndividualReqComponent from "./IndividualReqComponent";

const options = [
  {
    name: "Enable body scrolling",
    scroll: true,
    backdrop: false,
  },
];

const Requirement = () => {
  const { orggroup, reqcatid } = useParams();
  const navigate = useNavigate();

  const defaultColDef = {
    sortable: true,
    filter: true,
    resizable: true,
    flex: 1,
    cellStyle: {
      borderColor: "black",
      borderWidth: "1px",
      borderStyle: "solid",
    },
  };
  const [mData, setMData] = React.useState([]);
  const [indiData, setIndiData] = React.useState(null);
  const rowStyle = { textAlign: "center" };
  const getRowStyle = (params) => {
    if (params.data.type == "category") {
      return { background: "#99e6ff" };
    }
  };

  const [columnDefs] = React.useState([
    { headerName: "ID", field: "id" },

    {
      headerName: "Name",
      field: "name",
    },
    { headerName: "Summary", field: "summary" },
    // { headerName: "Description", field: "description" },
    { headerName: "Org group", field: "org_group" },
  ]);
  let myData = [];
  React.useEffect(() => {
    axiosClientBasic
      .get(
        "/requirements/api/browse_requirements_category?org_group=" +
          (orggroup === "default" ? "" : orggroup) +
          "&requirement_category_id=" +
          (reqcatid === undefined ? "" : reqcatid),
        {
          headers: {
            authorization:
              "Bearer " + window.localStorage.getItem("accessToken"),
          },
        }
      )
      .then((response) => {
        response.data.sub_categories.map((item) =>
          myData.push({
            id: item.id,
            name: item.name,
            summary: item.summary,
            org_group: item.org_group,
            type: "category",
          })
        );
        response.data.requirements.map((item) =>
          myData.push({
            id: item.id,
            name: item.name,
            summary: item.summary,
            org_group: item.org_group,
            type: "requirement",
          })
        );
        setMData(myData);
      });
  }, []);
  console.log(indiData);
  return (
    <div>
      <BreadcrumbComponent />

      <Row className="justify-content-md-center">
        <Col style={{ border: "1px solid black" }}>
          <div className="ag-theme-alpine" style={{ height: "150px" }}>
            <AgGridReact
              rowStyle={rowStyle}
              getRowStyle={getRowStyle}
              rowData={mData}
              columnDefs={columnDefs}
              defaultColDef={defaultColDef}
              onRowDoubleClicked={(data) => {
                if (data.data.type == "category") {
                  window.location =
                    window.location.origin +
                    "/requirements/" +
                    (data.data.org_group === null
                      ? "default"
                      : data.data.org_group) +
                    "/" +
                    data.data.id;
                } else {
                  navigate("/requirement/" + data.data.id);
                }
              }}
              onRowClicked={(data) => {
                setIndiData({ id: data.data.id, type: data.data.type });
              }}
            ></AgGridReact>
          </div>
        </Col>
        <Col style={{ border: "1px solid black" }}>
          <IndividualReqComponent data={indiData} />
        </Col>
        {/* <TreeComponent data={json} /> */}
      </Row>
    </div>
  );
};

export default Requirement;
