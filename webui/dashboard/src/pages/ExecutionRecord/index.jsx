import React from "react";
import { axiosClient } from "../../api/AxiosInstance";
import { AgGridReact } from "ag-grid-react";

import "ag-grid-community/dist/styles/ag-grid.css";
import "ag-grid-community/dist/styles/ag-theme-alpine.css";

const ExecutionRecords = () => {
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
  const [executionRecords, setExecutionRecords] = React.useState([]);
  const [columnDefs] = React.useState([
    { headerName: "ID", field: "id" },
    { headerName: "Name", field: "name" },
    { headerName: "Summary", field: "summary" },
    { headerName: "Status", field: "status" },
    { headerName: "Defects", field: "defects" },
  ]);
  React.useEffect(() => {
    axiosClient.get("/execution/api/execution_records/").then((response) => {
      setExecutionRecords(response.data.results);
    });
  }, []);

  return (
    <div className="ag-theme-alpine" style={{ height: "450px" }}>
      <AgGridReact
        rowData={executionRecords}
        columnDefs={columnDefs}
        defaultColDef={defaultColDef}
      ></AgGridReact>
    </div>
  );
};

export default ExecutionRecords;
