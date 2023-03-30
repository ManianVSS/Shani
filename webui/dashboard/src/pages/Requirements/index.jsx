import React from "react";
import { axiosClient } from "../../api/AxiosInstance";
import { AgGridReact } from "ag-grid-react";

import "ag-grid-community/dist/styles/ag-grid.css";
import "ag-grid-community/dist/styles/ag-theme-alpine.css";

const Requirements = () => {
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
  const [columnDefs] = React.useState([
    { headerName: "ID", field: "id" },
    { headerName: "Name", field: "name" },
    { headerName: "Summary", field: "summary" },
  ]);
  React.useEffect(() => {
    axiosClient.get("/requirements/").then((response) => {
      setRequirements(response.data.results);
    });
  }, []);

  return (
    <div className="ag-theme-alpine" style={{ height: "450px" }}>
      <AgGridReact
        rowData={requirements}
        defaultColDef={defaultColDef}
        columnDefs={columnDefs}
      ></AgGridReact>
    </div>
  );
};

export default Requirements;
