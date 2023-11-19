import React from "react";
import BreadcrumbComponent from "./BreadcrumbComponent";
import RequirementTable from "./RequirementTable";
import { AgGridReact } from "ag-grid-react";
import { axiosClient } from "../../hooks/api";

const Requirement = () => {
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
  const rowStyle = { textAlign: "center" };
  const [columnDefs] = React.useState([
    { headerName: "ID", field: "id" },
    { headerName: "Build", field: "build" },
    {
      headerName: "Name",
      field: "name",
    },
  ]);
  React.useEffect(() => {
    axiosClient.get("/execution/api/runs/").then((response) => {
      setRequirements(response.data.results);
    });
  }, []);
  return (
    <div>
      <BreadcrumbComponent />
      <div className="ag-theme-alpine" style={{ height: "450px" }}>
        <AgGridReact
          rowStyle={rowStyle}
          rowData={requirements}
          columnDefs={columnDefs}
          defaultColDef={defaultColDef}
        ></AgGridReact>
      </div>
    </div>
  );
};

export default Requirement;
