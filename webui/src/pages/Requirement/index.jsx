import React from "react";
import BreadcrumbComponent from "./BreadcrumbComponent";
import RequirementTable from "./RequirementTable";
import { AgGridReact } from "ag-grid-react";
import { axiosClientBasic } from "../../hooks/api";
import "ag-grid-community/dist/styles/ag-grid.css";
import "ag-grid-community/dist/styles/ag-theme-alpine.css";
import { useNavigate } from "react-router-dom";

const Requirement = () => {
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
  const [requirements, setRequirements] = React.useState([]);
  const [requirementCategories, setRequirementCategories] = React.useState([]);
  const rowStyle = { textAlign: "center" };
  const [columnDefs] = React.useState([
    { headerName: "ID", field: "id" },

    {
      headerName: "Name",
      field: "name",
    },
    { headerName: "Summary", field: "summary" },
    { headerName: "Description", field: "description" },
    { headerName: "Status", field: "status" },
    { headerName: "External ID", field: "external_id" },
    { headerName: "Cost", field: "cost" },
    { headerName: "Org group", field: "org_group" },
  ]);
  const [columnDefsReqCat] = React.useState([
    { headerName: "ID", field: "id" },

    {
      headerName: "Name",
      field: "name",
    },
    { headerName: "Summary", field: "summary" },
    { headerName: "Description", field: "description" },
    { headerName: "Org group", field: "org_group" },
  ]);
  React.useEffect(() => {
    axiosClientBasic
      .get("/requirements/api/browse_requirements_category?org_group=1", {
        headers: {
          authorization: "Bearer " + window.localStorage.getItem("accessToken"),
        },
      })
      .then((response) => {
        setRequirements(response.data.requirements);
        setRequirementCategories(response.data.sub_categories);
      });
  }, []);
  return (
    <div>
      <BreadcrumbComponent />
      <div className="ag-theme-alpine" style={{ height: "150px" }}>
        <AgGridReact
          rowStyle={rowStyle}
          rowData={requirementCategories}
          columnDefs={columnDefsReqCat}
          defaultColDef={defaultColDef}
        ></AgGridReact>
      </div>
      <div className="ag-theme-alpine" style={{ height: "150px" }}>
        <AgGridReact
          rowStyle={rowStyle}
          rowData={requirements}
          columnDefs={columnDefs}
          defaultColDef={defaultColDef}
          onRowDoubleClicked={(data) => {
            navigate("/requirements/" + data.data.id);
          }}
        ></AgGridReact>
      </div>
    </div>
  );
};

export default Requirement;
